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
from storeup.models import Storeup


# 保存
class DianpuxinxiSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            dianpumingcheng=data['dianpumingcheng']
            if dianpumingcheng == '':
                dianpumingcheng = None
        except KeyError:
            dianpumingcheng = None
        except ValueError:
            dianpumingcheng = None
        try:
            tupian=data['tupian']
            if tupian == '':
                tupian = None
        except KeyError:
            tupian = None
        except ValueError:
            tupian = None
        try:
            nicheng=data['nicheng']
            if nicheng == '':
                nicheng = None
        except KeyError:
            nicheng = None
        except ValueError:
            nicheng = None
        try:
            shangjiadianhua=data['shangjiadianhua']
            if shangjiadianhua == '':
                shangjiadianhua = None
        except KeyError:
            shangjiadianhua = None
        except ValueError:
            shangjiadianhua = None
        try:
            dianpujianjie=data['dianpujianjie']
            if dianpujianjie == '':
                dianpujianjie = None
        except KeyError:
            dianpujianjie = None
        except ValueError:
            dianpujianjie = None
        try:
            dianpudizhi=data['dianpudizhi']
            if dianpudizhi == '':
                dianpudizhi = None
        except KeyError:
            dianpudizhi = None
        except ValueError:
            dianpudizhi = None
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        try:
            lat=data['lat']
            if lat == '':
                lat = None
        except KeyError:
            lat = None
        except ValueError:
            lat = None
        try:
            lnt=data['lnt']
            if lnt == '':
                lnt = None
        except KeyError:
            lnt = None
        except ValueError:
            lnt = None
        try:
            conent=data['conent']
            if conent == '':
                conent = None
        except KeyError:
            conent = None
        except ValueError:
            conent = None
        try:
            sfsh=data['sfsh']
            if sfsh == '':
                sfsh = None
        except KeyError:
            sfsh = None
        except ValueError:
            sfsh = None
        try:
            shhf=data['shhf']
            if shhf == '':
                shhf = None
        except KeyError:
            shhf = None
        except ValueError:
            shhf = None
        Dianpuxinxi.objects.create(
            dianpumingcheng=dianpumingcheng,
            tupian=tupian,
            nicheng=nicheng,
            shangjiadianhua=shangjiadianhua,
            dianpujianjie=dianpujianjie,
            dianpudizhi=dianpudizhi,
            userid=userid,
            lat=lat,
            lnt=lnt,
            conent=conent,
            sfsh=sfsh,
            shhf=shhf,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class DianpuxinxiUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        dianpumingcheng=data['dianpumingcheng']
        tupian=data['tupian']
        nicheng=data['nicheng']
        shangjiadianhua=data['shangjiadianhua']
        dianpujianjie=data['dianpujianjie']
        dianpudizhi=data['dianpudizhi']
        userid=data['userid']
        lat=data['lat']
        lnt=data['lnt']
        conent=data['conent']
        sfsh=data['sfsh']
        shhf=data['shhf']
        id = data['id']
        Dianpuxinxi.objects.filter(id=id).update(
        id=id,
        dianpumingcheng=dianpumingcheng,
        tupian=tupian,
        nicheng=nicheng,
        shangjiadianhua=shangjiadianhua,
        dianpujianjie=dianpujianjie,
        dianpudizhi=dianpudizhi,
        userid=userid,
        lat=lat,
        lnt=lnt,
        conent=conent,
        sfsh=sfsh,
        shhf=shhf,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class DianpuxinxiDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Dianpuxinxi.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class DianpuxinxiInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Dianpuxinxi.objects.filter(id=int(id)).all()
        entityser = DianpuxinxiSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class DianpuxinxiList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return DianpuxinxiListNotPage(request)
        else:
            return DianpuxinxiListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return DianpuxinxiListNotPage(request)
        else:
            return DianpuxinxiListPage(request)

def DianpuxinxiListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
                                'tupian__icontains': request.query_params.get('tupian'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'shangjiadianhua__icontains': request.query_params.get('shangjiadianhua'),
                                'dianpujianjie__icontains': request.query_params.get('dianpujianjie'),
                                'dianpudizhi__icontains': request.query_params.get('dianpudizhi'),
                                                'lat__icontains': request.query_params.get('lat'),
                                'lnt__icontains': request.query_params.get('lnt'),
                                'conent__icontains': request.query_params.get('conent'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Dianpuxinxi.objects.filter(q_objects).all()
    count = Dianpuxinxi.objects.filter(q_objects).count()

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
    result = DianpuxinxiSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def DianpuxinxiListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
                                'tupian__icontains': request.query_params.get('tupian'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'shangjiadianhua__icontains': request.query_params.get('shangjiadianhua'),
                                'dianpujianjie__icontains': request.query_params.get('dianpujianjie'),
                                'dianpudizhi__icontains': request.query_params.get('dianpudizhi'),
                                                'lat__icontains': request.query_params.get('lat'),
                                'lnt__icontains': request.query_params.get('lnt'),
                                'conent__icontains': request.query_params.get('conent'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Dianpuxinxi.objects.filter(q_objects).all()
    count = Dianpuxinxi.objects.filter(q_objects).count()
    result = DianpuxinxiSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class DianpuxinxiPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
            'tupian__icontains': request.query_params.get('tupian'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'shangjiadianhua__icontains': request.query_params.get('shangjiadianhua'),
            'dianpujianjie__icontains': request.query_params.get('dianpujianjie'),
            'dianpudizhi__icontains': request.query_params.get('dianpudizhi'),
            'userid__icontains': request.query_params.get('userid'),
            'lat__icontains': request.query_params.get('lat'),
            'lnt__icontains': request.query_params.get('lnt'),
            'conent__icontains': request.query_params.get('conent'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Dianpuxinxi.objects.filter(q_objects).all()
        count = Dianpuxinxi.objects.filter(q_objects).count()

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
        result = DianpuxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
            'tupian__icontains': request.query_params.get('tupian'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'shangjiadianhua__icontains': request.query_params.get('shangjiadianhua'),
            'dianpujianjie__icontains': request.query_params.get('dianpujianjie'),
            'dianpudizhi__icontains': request.query_params.get('dianpudizhi'),
            'userid__icontains': request.query_params.get('userid'),
            'lat__icontains': request.query_params.get('lat'),
            'lnt__icontains': request.query_params.get('lnt'),
            'conent__icontains': request.query_params.get('conent'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Dianpuxinxi.objects.filter(q_objects).all()
        count = Dianpuxinxi.objects.filter(q_objects).count()

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
        result = DianpuxinxiSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})


# 推荐
class Recommend(APIView):
    def post(self, request):
        user_id = request.query_params.get('userId')
        num = request.query_params.get('num')

        # 使用 values_list 获取每个用户及其对应的收藏id
        queryset = Storeup.objects.values_list('userid', 'refid')
        
        # 使用 defaultdict 来方便地构建 Dict[userid, Set[refid]] 结构
        collections = defaultdict(set)
        
        for userid, refid in queryset:
            collections[str(userid)].add(refid)
        
        # 将 defaultdict 转换为普通的 dict
        user_item_collections = dict(collections)
        # 查询数据库，将Dict传入UserBasedCollaborativeFiltering
        userBasedCF = UserBasedCollaborativeFiltering(user_item_collections)
        recommendations = userBasedCF.recommend_items(user_id, num)
        keys = recommendations.keys()
        # 使用 Django ORM
        recommended_items = Dianpuxinxi.objects.filter(id__in=keys)
        result = [Dianpuxinxi.dianpuxinxi_to_dict(item) for item in recommended_items]
        return Response({'code': 0, 'data': result})






def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

