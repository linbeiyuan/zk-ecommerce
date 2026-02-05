import re
from django.db.models import Q, Value, F
from rest_framework.views import APIView
from rest_framework.response import Response



import time
import random
import datetime
from datetime import timedelta
from utils.myjwt import myjwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from address.models import *
from address.serializers import *
from orders.models import *
from orders.serializers import *
from cart.models import *
from cart.serializers import *
from news.models import *
from news.serializers import *
from messagess.models import *
from messagess.serializers import *
from crk.models import *
from crk.serializers import *
from shangpinguanli.models import *
from shangpinguanli.serializers import *
from discussshangpinguanli.models import *
from discussshangpinguanli.serializers import *
from shangpinfenlei.models import *
from shangpinfenlei.serializers import *
from dianpuxinxi.models import *
from dianpuxinxi.serializers import *
from discussdianpuxinxi.models import *
from discussdianpuxinxi.serializers import *
from jifenshangdian.models import *
from jifenshangdian.serializers import *
from yonghu.models import *
from yonghu.serializers import *
from shangjia.models import *
from shangjia.serializers import *
from tokens.models import *
from utils import *
from collections import defaultdict


# 保存
class DiscussdianpuxinxiSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            refid=data['refid']
            if refid == '':
                refid = None
        except KeyError:
            refid = None
        except ValueError:
            refid = None
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        try:
            nickname=data['nickname']
            if nickname == '':
                nickname = None
        except KeyError:
            nickname = None
        except ValueError:
            nickname = None
        try:
            content=data['content']
            if content == '':
                content = None
        except KeyError:
            content = None
        except ValueError:
            content = None
        try:
            reply=data['reply']
            if reply == '':
                reply = None
        except KeyError:
            reply = None
        except ValueError:
            reply = None
        Discussdianpuxinxi.objects.create(
            refid=refid,
            userid=userid,
            nickname=nickname,
            content=content,
            reply=reply,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class DiscussdianpuxinxiUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        refid=data['refid']
        userid=data['userid']
        nickname=data['nickname']
        content=data['content']
        reply=data['reply']
        id = data['id']
        Discussdianpuxinxi.objects.filter(id=id).update(
        id=id,
        refid=refid,
        userid=userid,
        nickname=nickname,
        content=content,
        reply=reply,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class DiscussdianpuxinxiDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Discussdianpuxinxi.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class DiscussdianpuxinxiInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Discussdianpuxinxi.objects.filter(id=int(id)).all()
        entityser = DiscussdianpuxinxiSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class DiscussdianpuxinxiList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return DiscussdianpuxinxiListNotPage(request)
        else:
            return DiscussdianpuxinxiListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return DiscussdianpuxinxiListNotPage(request)
        else:
            return DiscussdianpuxinxiListPage(request)

def DiscussdianpuxinxiListPage(request):
    userid = request.query_params.get('userid')
    shangjia_userid = request.query_params.get('shangjia_userid')  # 商家ID过滤
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'refid__icontains': request.query_params.get('refid'),
                                                'nickname__icontains': request.query_params.get('nickname'),
                                'content__icontains': request.query_params.get('content'),
                                'reply__icontains': request.query_params.get('reply'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    # 如果传入商家ID，只查询该商家店铺的评论
    if shangjia_userid is not None:
        dianpu_ids = Dianpuxinxi.objects.filter(userid=shangjia_userid).values_list('id', flat=True)
        q_objects.add(Q(refid__in=list(dianpu_ids)), Q.AND)

    queryset = Discussdianpuxinxi.objects.filter(q_objects).all()
    count = Discussdianpuxinxi.objects.filter(q_objects).count()

            # 第二步：创建分页器，每页10条数据
    paginator = Paginator(queryset, limit)
    try:
        # 获取当前页的数据
        items = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页
        items = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页
        items = paginator.page(paginator.num_pages)
    result = DiscussdianpuxinxiSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def DiscussdianpuxinxiListNotPage(request):
    userid = request.query_params.get('userid')
    refid = request.query_params.get('refid')  # 获取店铺ID参数
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                                'nickname__icontains': request.query_params.get('nickname'),
                                'content__icontains': request.query_params.get('content'),
                                'reply__icontains': request.query_params.get('reply'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    # 如果传入店铺ID，只查询该店铺的评论
    if refid is not None:
        q_objects.add(Q(**{'refid': refid}), Q.AND)

    queryset = Discussdianpuxinxi.objects.filter(q_objects).all()
    count = Discussdianpuxinxi.objects.filter(q_objects).count()
    result = DiscussdianpuxinxiSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class DiscussdianpuxinxiPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序
        shangjia_userid = request.query_params.get('shangjia_userid')  # 商家ID过滤

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'refid__icontains': request.query_params.get('refid'),
            'userid__icontains': request.query_params.get('userid'),
            'nickname__icontains': request.query_params.get('nickname'),
            'content__icontains': request.query_params.get('content'),
            'reply__icontains': request.query_params.get('reply'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        # 如果传入商家ID，只查询该商家店铺的评论
        if shangjia_userid is not None:
            dianpu_ids = Dianpuxinxi.objects.filter(userid=shangjia_userid).values_list('id', flat=True)
            q_objects.add(Q(refid__in=list(dianpu_ids)), Q.AND)

        queryset = Discussdianpuxinxi.objects.filter(q_objects).all()
        count = Discussdianpuxinxi.objects.filter(q_objects).count()

        # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = None
        result = DiscussdianpuxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'refid__icontains': request.query_params.get('refid'),
            'userid__icontains': request.query_params.get('userid'),
            'nickname__icontains': request.query_params.get('nickname'),
            'content__icontains': request.query_params.get('content'),
            'reply__icontains': request.query_params.get('reply'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Discussdianpuxinxi.objects.filter(q_objects).all()
        count = Discussdianpuxinxi.objects.filter(q_objects).count()

                    # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = paginator.page(paginator.num_pages)
        result = DiscussdianpuxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

