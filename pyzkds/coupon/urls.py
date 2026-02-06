from django.urls import path
from .views import *

urlpatterns = [
    path('list', CouponList.as_view()),  # 获取可领取的优惠券列表
    path('receive', receive_coupon),  # 领取优惠券
    path('my', UserCouponList.as_view()),  # 我的优惠券
    path('available', get_available_coupons),  # 获取可用优惠券
    path('create', create_coupon),  # 创建优惠券
    path('delete', delete_coupon),  # 删除优惠券
    path('use', use_coupon),  # 使用优惠券
]
