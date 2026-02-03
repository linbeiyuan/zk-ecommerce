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
class ShangjiaSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            yonghuming=data['yonghuming']
            if yonghuming == '':
                yonghuming = None
        except KeyError:
            yonghuming = None
        except ValueError:
            yonghuming = None
        try:
            mima=data['mima']
            if mima == '':
                mima = None
        except KeyError:
            mima = None
        except ValueError:
            mima = None
        try:
            shoujihao=data['shoujihao']
            if shoujihao == '':
                shoujihao = None
        except KeyError:
            shoujihao = None
        except ValueError:
            shoujihao = None
        try:
            shangjiamingcheng=data['shangjiamingcheng']
            if shangjiamingcheng == '':
                shangjiamingcheng = None
        except KeyError:
            shangjiamingcheng = None
        except ValueError:
            shangjiamingcheng = None
        try:
            money=data['money']
            if money == '':
                money = None
        except KeyError:
            money = None
        except ValueError:
            money = None
        try:
            jf=data['jf']
            if jf == '':
                jf = None
        except KeyError:
            jf = None
        except ValueError:
            jf = None
        Shangjia.objects.create(
            yonghuming=yonghuming,
            mima=mima,
            shoujihao=shoujihao,
            shangjiamingcheng=shangjiamingcheng,
            money=money,
            jf=jf,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class ShangjiaUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        yonghuming=data['yonghuming']
        mima=data['mima']
        shoujihao=data['shoujihao']
        shangjiamingcheng=data['shangjiamingcheng']
        money=data['money']
        jf=data['jf']
        id = data['id']
        Shangjia.objects.filter(id=id).update(
        id=id,
        yonghuming=yonghuming,
        mima=mima,
        shoujihao=shoujihao,
        shangjiamingcheng=shangjiamingcheng,
        money=money,
        jf=jf,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class ShangjiaDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Shangjia.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class ShangjiaInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Shangjia.objects.filter(id=int(id)).all()
        entityser = ShangjiaSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class ShangjiaList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return ShangjiaListNotPage(request)
        else:
            return ShangjiaListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return ShangjiaListNotPage(request)
        else:
            return ShangjiaListPage(request)

def ShangjiaListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'mima__icontains': request.query_params.get('mima'),
                                'shoujihao__icontains': request.query_params.get('shoujihao'),
                                'shangjiamingcheng__icontains': request.query_params.get('shangjiamingcheng'),
                                'money__icontains': request.query_params.get('money'),
                                'jf__icontains': request.query_params.get('jf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Shangjia.objects.filter(q_objects).all()
    count = Shangjia.objects.filter(q_objects).count()

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
    result = ShangjiaSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def ShangjiaListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'mima__icontains': request.query_params.get('mima'),
                                'shoujihao__icontains': request.query_params.get('shoujihao'),
                                'shangjiamingcheng__icontains': request.query_params.get('shangjiamingcheng'),
                                'money__icontains': request.query_params.get('money'),
                                'jf__icontains': request.query_params.get('jf'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Shangjia.objects.filter(q_objects).all()
    count = Shangjia.objects.filter(q_objects).count()
    result = ShangjiaSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class ShangjiaPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'mima__icontains': request.query_params.get('mima'),
            'shoujihao__icontains': request.query_params.get('shoujihao'),
            'shangjiamingcheng__icontains': request.query_params.get('shangjiamingcheng'),
            'money__icontains': request.query_params.get('money'),
            'jf__icontains': request.query_params.get('jf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Shangjia.objects.filter(q_objects).all()
        count = Shangjia.objects.filter(q_objects).count()

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
        result = ShangjiaSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'mima__icontains': request.query_params.get('mima'),
            'shoujihao__icontains': request.query_params.get('shoujihao'),
            'shangjiamingcheng__icontains': request.query_params.get('shangjiamingcheng'),
            'money__icontains': request.query_params.get('money'),
            'jf__icontains': request.query_params.get('jf'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Shangjia.objects.filter(q_objects).all()
        count = Shangjia.objects.filter(q_objects).count()

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
        result = ShangjiaSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})







# 用户登录
class LoginShangjia(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Shangjia.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='shangjia',
                role='商家',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Shangjia.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='shangjia',
                role='商家',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

# 用户获取session
class ShangjiaSession(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Shangjia.objects.filter(id=session).all()
        user_ser = ShangjiaSer(users, many=True)
        user_ser.data[0]['role'] = 'shangjia'
        return Response({'code': 0, 'data': user_ser.data[0]})

    def post(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Shangjia.objects.filter(id=session).all()
        user_ser = ShangjiaSer(users, many=True)
        user_ser.data[0]['role'] = 'shangjia'
        return Response({'code': 0, 'data': user_ser.data[0]})

# 用户注册
class Register(APIView):
    def post(self, request):
        data = request.data
        yonghuming=data.get('yonghuming')
        mima=data.get('mima')
        shoujihao=data.get('shoujihao')
        shangjiamingcheng=data.get('shangjiamingcheng')
        jf=data.get('jf', 0)  # 默认积分为0
        if not all([
            yonghuming,
            mima,
            shoujihao,
            shangjiamingcheng,
        ]):
            return Response({"code": 401, 'msg': '参数不全'})


        Shangjia.objects.create(
            id=generate_unique_userid(),
            yonghuming=yonghuming,
            mima=mima,
            shoujihao=shoujihao,
            shangjiamingcheng=shangjiamingcheng,
            jf=jf,
        )
        return Response({'code': 0, 'msg': '注册成功'})
   



def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

