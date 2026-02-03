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
class CrkSave(APIView):
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
        try:
            name=data['name']
            if name == '':
                name = None
        except KeyError:
            name = None
        except ValueError:
            name = None
        try:
            sl=data['sl']
            if sl == '':
                sl = None
        except KeyError:
            sl = None
        except ValueError:
            sl = None
        try:
            crkzt=data['crkzt']
            if crkzt == '':
                crkzt = None
        except KeyError:
            crkzt = None
        except ValueError:
            crkzt = None
        Crk.objects.create(
            refid=refid,
            name=name,
            sl=sl,
            crkzt=crkzt,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class CrkUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        refid=data['refid']
        name=data['name']
        sl=data['sl']
        crkzt=data['crkzt']
        id = data['id']
        Crk.objects.filter(id=id).update(
        id=id,
        refid=refid,
        name=name,
        sl=sl,
        crkzt=crkzt,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class CrkDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Crk.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class CrkInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Crk.objects.filter(id=int(id)).all()
        entityser = CrkSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class CrkList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return CrkListNotPage(request)
        else:
            return CrkListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return CrkListNotPage(request)
        else:
            return CrkListPage(request)

def CrkListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'refid__icontains': request.query_params.get('refid'),
                                'name__icontains': request.query_params.get('name'),
                                'sl__icontains': request.query_params.get('sl'),
                                'crkzt__icontains': request.query_params.get('crkzt'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Crk.objects.filter(q_objects).all()
    count = Crk.objects.filter(q_objects).count()

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
    result = CrkSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def CrkListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'refid__icontains': request.query_params.get('refid'),
                                'name__icontains': request.query_params.get('name'),
                                'sl__icontains': request.query_params.get('sl'),
                                'crkzt__icontains': request.query_params.get('crkzt'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Crk.objects.filter(q_objects).all()
    count = Crk.objects.filter(q_objects).count()
    result = CrkSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class CrkPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序
        shangjia_userid = request.query_params.get('shangjia_userid')

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'refid__icontains': request.query_params.get('refid'),
            'name__icontains': request.query_params.get('name'),
            'sl__icontains': request.query_params.get('sl'),
            'crkzt__icontains': request.query_params.get('crkzt'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        # 如果传入商家ID，只查询该商家商品的出入库记录
        if shangjia_userid is not None:
            shangpin_ids = Shangpinguanli.objects.filter(userid=shangjia_userid).values_list('id', flat=True)
            q_objects.add(Q(refid__in=list(shangpin_ids)), Q.AND)

        queryset = Crk.objects.filter(q_objects).all()
        count = Crk.objects.filter(q_objects).count()

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
        result = CrkSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序
        shangjia_userid = request.query_params.get('shangjia_userid')

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'refid__icontains': request.query_params.get('refid'),
            'name__icontains': request.query_params.get('name'),
            'sl__icontains': request.query_params.get('sl'),
            'crkzt__icontains': request.query_params.get('crkzt'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        # 如果传入商家ID，只查询该商家商品的出入库记录
        if shangjia_userid is not None:
            shangpin_ids = Shangpinguanli.objects.filter(userid=shangjia_userid).values_list('id', flat=True)
            q_objects.add(Q(refid__in=list(shangpin_ids)), Q.AND)

        queryset = Crk.objects.filter(q_objects).all()
        count = Crk.objects.filter(q_objects).count()

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
        result = CrkSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

