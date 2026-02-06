from django.db import models

# 优惠券模板表
class Coupon(models.Model):
    """优惠券模板"""
    name = models.CharField(max_length=100, verbose_name='优惠券名称')
    type = models.IntegerField(verbose_name='类型', default=1)  # 1:满减券

    # 满减券字段
    condition_amount = models.FloatField(null=True, blank=True, verbose_name='满足金额')
    discount_amount = models.FloatField(null=True, blank=True, verbose_name='减免金额')

    # 发放设置
    total_count = models.IntegerField(verbose_name='发行总量')
    receive_limit = models.IntegerField(default=1, verbose_name='每人限领')

    # 有效期
    valid_days = models.IntegerField(verbose_name='有效天数')
    start_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')

    status = models.IntegerField(default=1, verbose_name='状态')  # 1:进行中 2:已结束
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'coupon'


# 用户优惠券表
class UserCoupon(models.Model):
    """用户领取的优惠券"""
    userid = models.BigIntegerField(verbose_name='用户ID')
    coupon_id = models.IntegerField(verbose_name='优惠券模板ID')

    # 优惠券信息
    name = models.CharField(max_length=100, verbose_name='优惠券名称')
    type = models.IntegerField(verbose_name='类型')
    condition_amount = models.FloatField(null=True, blank=True, verbose_name='满足金额')
    discount_amount = models.FloatField(null=True, blank=True, verbose_name='减免金额')

    # 使用状态
    status = models.IntegerField(default=1, verbose_name='状态')  # 1:未使用 2:已使用 3:已过期
    orderid = models.CharField(max_length=100, null=True, blank=True, verbose_name='订单号')

    # 时间
    receive_time = models.DateTimeField(auto_now_add=True, verbose_name='领取时间')
    use_time = models.DateTimeField(null=True, blank=True, verbose_name='使用时间')
    expire_time = models.DateTimeField(verbose_name='过期时间')

    class Meta:
        db_table = 'user_coupon'
