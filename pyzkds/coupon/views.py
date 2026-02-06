from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from utils.myjwt import myjwt
from .models import Coupon, UserCoupon
from .serializers import CouponSerializer, UserCouponSerializer


# 获取可领取的优惠券列表
class CouponList(APIView):
    def get(self, request):
        """获取所有可领取的优惠券"""
        try:
            now = timezone.now()
            coupons = Coupon.objects.filter(
                status=1,
                start_time__lte=now,
                end_time__gte=now
            ).all()
            serializer = CouponSerializer(coupons, many=True)
            return Response({'code': 0, 'data': serializer.data})
        except Exception as e:
            return Response({'code': 500, 'msg': str(e)})


# 领取优惠券
@api_view(['POST'])
def receive_coupon(request):
    """用户领取优惠券"""
    try:
        # 获取用户ID
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)
        if 'data' in user_info:
            userid = user_info['data'].get('userid')
        else:
            userid = user_info.get('id')

        coupon_id = request.data.get('coupon_id')

        # 检查优惠券是否存在
        coupon = Coupon.objects.filter(id=coupon_id, status=1).first()
        if not coupon:
            return Response({'code': 1, 'msg': '优惠券不存在或已下架'})

        # 检查是否在有效期内
        now = timezone.now()
        if now < coupon.start_time or now > coupon.end_time:
            return Response({'code': 1, 'msg': '优惠券不在有效期内'})

        # 检查是否已达到领取上限
        received_count = UserCoupon.objects.filter(
            userid=userid,
            coupon_id=coupon_id
        ).count()
        if received_count >= coupon.receive_limit:
            return Response({'code': 1, 'msg': f'每人限领{coupon.receive_limit}张'})

        # 检查库存
        issued_count = UserCoupon.objects.filter(coupon_id=coupon_id).count()
        if issued_count >= coupon.total_count:
            return Response({'code': 1, 'msg': '优惠券已被抢光'})

        # 发放优惠券
        expire_time = now + timedelta(days=coupon.valid_days)
        UserCoupon.objects.create(
            userid=userid,
            coupon_id=coupon.id,
            name=coupon.name,
            type=coupon.type,
            condition_amount=coupon.condition_amount,
            discount_amount=coupon.discount_amount,
            expire_time=expire_time
        )

        return Response({'code': 0, 'msg': '领取成功'})
    except Exception as e:
        return Response({'code': 500, 'msg': f'领取失败: {str(e)}'})


# 查询用户的优惠券列表
class UserCouponList(APIView):
    def get(self, request):
        """获取用户的优惠券列表"""
        try:
            # 获取用户ID
            token = request.META.get('HTTP_TOKEN', 'No token provided')
            user_info = myjwt.jwt_decode(token)
            if 'data' in user_info:
                userid = user_info['data'].get('userid')
            else:
                userid = user_info.get('id')

            # 获取状态参数（1:未使用 2:已使用 3:已过期）
            status = request.query_params.get('status')

            # 查询用户优惠券
            query = UserCoupon.objects.filter(userid=userid)
            if status:
                query = query.filter(status=status)

            coupons = query.order_by('-receive_time').all()
            serializer = UserCouponSerializer(coupons, many=True)

            return Response({'code': 0, 'data': serializer.data})
        except Exception as e:
            return Response({'code': 500, 'msg': str(e)})


# 获取可用优惠券（购物车结算时使用）
@api_view(['GET'])
def get_available_coupons(request):
    """获取当前订单可用的优惠券"""
    try:
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)
        if 'data' in user_info:
            userid = user_info['data'].get('userid')
        else:
            userid = user_info.get('id')

        total_amount = float(request.query_params.get('total_amount', 0))
        now = timezone.now()
        coupons = UserCoupon.objects.filter(
            userid=userid,
            status=1,
            expire_time__gt=now
        ).all()

        available = []
        unavailable = []

        for coupon in coupons:
            coupon_data = UserCouponSerializer(coupon).data
            if coupon.condition_amount and total_amount >= coupon.condition_amount:
                coupon_data['can_use'] = True
                available.append(coupon_data)
            else:
                coupon_data['can_use'] = False
                coupon_data['reason'] = f'需满{coupon.condition_amount}元'
                unavailable.append(coupon_data)

        return Response({'code': 0, 'data': {'available': available, 'unavailable': unavailable}})
    except Exception as e:
        return Response({'code': 500, 'msg': str(e)})


# 创建优惠券（管理员）
@api_view(['POST'])
def create_coupon(request):
    """管理员创建优惠券"""
    try:
        data = request.data
        Coupon.objects.create(
            name=data['name'],
            type=1,
            condition_amount=data['condition_amount'],
            discount_amount=data['discount_amount'],
            total_count=data['total_count'],
            receive_limit=data.get('receive_limit', 1),
            valid_days=data['valid_days'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            status=1
        )
        return Response({'code': 0, 'msg': '创建成功'})
    except Exception as e:
        return Response({'code': 500, 'msg': f'创建失败: {str(e)}'})


# 删除优惠券（管理员）
@api_view(['POST'])
def delete_coupon(request):
    """管理员删除优惠券"""
    try:
        coupon_id = request.data.get('id')
        if not coupon_id:
            return Response({'code': 1, 'msg': '优惠券ID不能为空'})

        coupon = Coupon.objects.filter(id=coupon_id).first()
        if not coupon:
            return Response({'code': 1, 'msg': '优惠券不存在'})

        coupon.delete()
        return Response({'code': 0, 'msg': '删除成功'})
    except Exception as e:
        return Response({'code': 500, 'msg': f'删除失败: {str(e)}'})


# 使用优惠券（订单提交时调用）
@api_view(['POST'])
def use_coupon(request):
    """使用优惠券"""
    try:
        user_coupon_id = request.data.get('user_coupon_id')
        orderid = request.data.get('orderid')

        if not user_coupon_id or not orderid:
            return Response({'code': 1, 'msg': '参数不完整'})

        # 查找用户优惠券
        user_coupon = UserCoupon.objects.filter(id=user_coupon_id).first()
        if not user_coupon:
            return Response({'code': 1, 'msg': '优惠券不存在'})

        # 更新优惠券状态
        from django.utils import timezone
        user_coupon.status = 2  # 已使用
        user_coupon.orderid = orderid
        user_coupon.use_time = timezone.now()
        user_coupon.save()

        return Response({'code': 0, 'msg': '优惠券使用成功'})
    except Exception as e:
        return Response({'code': 500, 'msg': f'使用失败: {str(e)}'})
