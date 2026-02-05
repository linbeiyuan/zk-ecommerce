from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils import myjwt
from .models import Letter
from .serializers import LetterSer
from django.db.models import Q

@api_view(['GET'])
def query_msg(request):
    try:
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)
        receiver = user_info.get('data', {}).get('userid') or user_info.get('id')
        letters = Letter.objects.filter(Q(receiver=receiver) | Q(sender=receiver)).order_by('send_time')
        serializer = LetterSer(letters, many=True)
        return Response({'code': 0, 'data': serializer.data})
    except Exception as e:
        return Response({'code': 500, 'msg': str(e)})

@api_view(['GET'])
def query_somebody_msg(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    user_info = myjwt.jwt_decode(token)
    self_id = user_info.get('data', {}).get('userid') or user_info.get('id')
    sender = request.query_params.get('sender')
    letters = Letter.objects.filter(
        (Q(receiver=self_id) & Q(sender=sender)) |
        (Q(receiver=sender) & Q(sender=self_id))
    ).order_by('send_time')
    serializer = LetterSer(letters, many=True)
    return Response({'code': 0, 'data': serializer.data})

@api_view(['POST'])
def send_message(request):
    """发送消息"""
    try:
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)

        # 兼容两种token格式
        if 'data' in user_info:
            sender_id = user_info['data'].get('userid')
            sender_name = user_info['data'].get('nicheng') or user_info['data'].get('username') or '用户'
        else:
            sender_id = user_info.get('id')
            sender_name = user_info.get('nicheng') or user_info.get('username') or user_info.get('name') or '用户'

        receiver_id = request.data.get('receiver')
        receiver_name = request.data.get('receiverName', '商家')
        msg = request.data.get('msg')

        if not receiver_id or not msg:
            return Response({'code': 400, 'msg': '参数错误'})

        Letter.objects.create(
            sender=sender_id,
            sender_name=sender_name,
            receiver=receiver_id,
            receiver_name=receiver_name,
            msg=msg,
            read_status=0
        )
        return Response({'code': 0, 'msg': '发送成功'})
    except Exception as e:
        return Response({'code': 500, 'msg': f'发送失败: {str(e)}'})

@api_view(['POST'])
def update_read_status(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    user_info = myjwt.jwt_decode(token)
    self_id = user_info.get('data', {}).get('userid') or user_info.get('id')
    sender = request.data.get('sender')
    letters = Letter.objects.filter(sender=sender, receiver=self_id, read_status=0)
    letters.update(read_status=1)
    return Response({'code': 0, 'status': 'success'})

@api_view(['GET'])
def query_letter_list(request):
    token = request.META.get('HTTP_TOKEN', 'No token provided')
    user_info = myjwt.jwt_decode(token)
    self_id = user_info.get('data', {}).get('userid') or user_info.get('id')
    # 查询与当前用户相关的私信列表
    letters = Letter.objects.filter(Q(receiver=self_id) | Q(sender=self_id)).distinct()
    serializer = LetterSer(letters, many=True)
    return Response({'code': 0, 'data': serializer.data})