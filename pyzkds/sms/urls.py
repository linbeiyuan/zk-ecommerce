"""
短信验证码 URL 路由
"""
from django.urls import path
from sms.views import SendSmsCodeView, VerifySmsCodeView, SmsHistoryView

urlpatterns = [
    # 发送验证码
    path('send', SendSmsCodeView.as_view(), name='send_sms_code'),

    # 验证验证码（测试用）
    path('verify', VerifySmsCodeView.as_view(), name='verify_sms_code'),

    # 查询验证码历史
    path('history/<str:phone>', SmsHistoryView.as_view(), name='sms_history'),
]
