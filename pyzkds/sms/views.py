"""
短信验证码 API 视图
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sms.service import send_sms_code, verify_sms_code, get_sms_history
import re


class SendSmsCodeView(APIView):
    """发送短信验证码"""

    def post(self, request):
        phone = request.data.get('phone')

        # 验证手机号格式
        if not phone:
            return Response({
                'code': 401,
                'msg': '请输入手机号'
            })

        # 手机号格式验证
        if not re.match(r'^1[3-9]\d{9}$', phone):
            return Response({
                'code': 401,
                'msg': '手机号格式不正确'
            })

        # 发送验证码
        result = send_sms_code(phone)

        if result['success']:
            response_data = {
                'code': 0,
                'msg': result['message']
            }
            # 开发环境返回验证码
            if 'code' in result:
                response_data['data'] = {'code': result['code']}
            return Response(response_data)
        else:
            return Response({
                'code': 401,
                'msg': result['message']
            })


class VerifySmsCodeView(APIView):
    """验证短信验证码（测试用）"""

    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')

        if not phone or not code:
            return Response({
                'success': False,
                'message': '请输入手机号和验证码'
            }, status=status.HTTP_400_BAD_REQUEST)

        # 验证验证码
        result = verify_sms_code(phone, code)

        if result['success']:
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class SmsHistoryView(APIView):
    """查询验证码历史（管理用）"""

    def get(self, request, phone):
        history = get_sms_history(phone)
        return Response({
            'success': True,
            'data': history
        }, status=status.HTTP_200_OK)
