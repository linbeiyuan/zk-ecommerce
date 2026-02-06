from rest_framework import serializers
from .models import Coupon, UserCoupon


class CouponSerializer(serializers.ModelSerializer):
    """优惠券模板序列化器"""
    remaining_count = serializers.SerializerMethodField()

    class Meta:
        model = Coupon
        fields = '__all__'

    def get_remaining_count(self, obj):
        """计算剩余数量"""
        issued_count = UserCoupon.objects.filter(coupon_id=obj.id).count()
        return obj.total_count - issued_count


class UserCouponSerializer(serializers.ModelSerializer):
    """用户优惠券序列化器"""
    class Meta:
        model = UserCoupon
        fields = '__all__'
