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
class ShangpinguanliSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            shangpinmingcheng=data['shangpinmingcheng']
            if shangpinmingcheng == '':
                shangpinmingcheng = None
        except KeyError:
            shangpinmingcheng = None
        except ValueError:
            shangpinmingcheng = None
        try:
            shangpintupian=data['shangpintupian']
            if shangpintupian == '':
                shangpintupian = None
        except KeyError:
            shangpintupian = None
        except ValueError:
            shangpintupian = None
        try:
            fenleimingcheng=data['fenleimingcheng']
            if fenleimingcheng == '':
                fenleimingcheng = None
        except KeyError:
            fenleimingcheng = None
        except ValueError:
            fenleimingcheng = None
        try:
            jieshao=data['jieshao']
            if jieshao == '':
                jieshao = None
        except KeyError:
            jieshao = None
        except ValueError:
            jieshao = None
        try:
            xiangqing=data['xiangqing']
            if xiangqing == '':
                xiangqing = None
        except KeyError:
            xiangqing = None
        except ValueError:
            xiangqing = None
        try:
            dianpumingcheng=data['dianpumingcheng']
            if dianpumingcheng == '':
                dianpumingcheng = None
        except KeyError:
            dianpumingcheng = None
        except ValueError:
            dianpumingcheng = None
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        userid = myjwt.jwt_decode(token)['data']['userid']
        try:
            price=data['price']
            if price == '':
                price = None
        except KeyError:
            price = None
        except ValueError:
            price = None
        try:
            onelimittimes=data['onelimittimes']
            if onelimittimes == '':
                onelimittimes = None
        except KeyError:
            onelimittimes = None
        except ValueError:
            onelimittimes = None
        try:
            alllimittimes=data['alllimittimes']
            if alllimittimes == '':
                alllimittimes = None
        except KeyError:
            alllimittimes = None
        except ValueError:
            alllimittimes = None
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
        try:
            thumbsupnum=data['thumbsupnum']
            if thumbsupnum == '':
                thumbsupnum = None
        except KeyError:
            thumbsupnum = None
        except ValueError:
            thumbsupnum = None
        try:
            crazilynum=data['crazilynum']
            if crazilynum == '':
                crazilynum = None
        except KeyError:
            crazilynum = None
        except ValueError:
            crazilynum = None
        Shangpinguanli.objects.create(
            shangpinmingcheng=shangpinmingcheng,
            shangpintupian=shangpintupian,
            fenleimingcheng=fenleimingcheng,
            jieshao=jieshao,
            xiangqing=xiangqing,
            dianpumingcheng=dianpumingcheng,
            userid=userid,
            price=price,
            onelimittimes=onelimittimes,
            alllimittimes=alllimittimes,
            sfsh=sfsh,
            shhf=shhf,
            thumbsupnum=thumbsupnum,
            crazilynum=crazilynum,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class ShangpinguanliUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        shangpinmingcheng=data['shangpinmingcheng']
        shangpintupian=data['shangpintupian']
        fenleimingcheng=data['fenleimingcheng']
        jieshao=data['jieshao']
        xiangqing=data['xiangqing']
        dianpumingcheng=data['dianpumingcheng']
        userid=data['userid']
        price=data['price']
        onelimittimes=data['onelimittimes']
        alllimittimes=data['alllimittimes']
        sfsh=data['sfsh']
        shhf=data['shhf']
        thumbsupnum=data['thumbsupnum']
        crazilynum=data['crazilynum']
        id = data['id']
        Shangpinguanli.objects.filter(id=id).update(
        id=id,
        shangpinmingcheng=shangpinmingcheng,
        shangpintupian=shangpintupian,
        fenleimingcheng=fenleimingcheng,
        jieshao=jieshao,
        xiangqing=xiangqing,
        dianpumingcheng=dianpumingcheng,
        userid=userid,
        price=price,
        onelimittimes=onelimittimes,
        alllimittimes=alllimittimes,
        sfsh=sfsh,
        shhf=shhf,
        thumbsupnum=thumbsupnum,
        crazilynum=crazilynum,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class ShangpinguanliDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Shangpinguanli.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class ShangpinguanliInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Shangpinguanli.objects.filter(id=int(id)).all()
        entityser = ShangpinguanliSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class ShangpinguanliList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return ShangpinguanliListNotPage(request)
        else:
            return ShangpinguanliListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return ShangpinguanliListNotPage(request)
        else:
            return ShangpinguanliListPage(request)

def ShangpinguanliListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'shangpinmingcheng__icontains': request.query_params.get('shangpinmingcheng'),
                                'shangpintupian__icontains': request.query_params.get('shangpintupian'),
                                'fenleimingcheng__icontains': request.query_params.get('fenleimingcheng'),
                                'jieshao__icontains': request.query_params.get('jieshao'),
                                'xiangqing__icontains': request.query_params.get('xiangqing'),
                                'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
                                                'price__icontains': request.query_params.get('price'),
                                'onelimittimes__icontains': request.query_params.get('onelimittimes'),
                                'alllimittimes__icontains': request.query_params.get('alllimittimes'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                                'thumbsupnum__icontains': request.query_params.get('thumbsupnum'),
                                'crazilynum__icontains': request.query_params.get('crazilynum'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Shangpinguanli.objects.filter(q_objects).all()
    count = Shangpinguanli.objects.filter(q_objects).count()

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
    result = ShangpinguanliSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def ShangpinguanliListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'shangpinmingcheng__icontains': request.query_params.get('shangpinmingcheng'),
                                'shangpintupian__icontains': request.query_params.get('shangpintupian'),
                                'fenleimingcheng__icontains': request.query_params.get('fenleimingcheng'),
                                'jieshao__icontains': request.query_params.get('jieshao'),
                                'xiangqing__icontains': request.query_params.get('xiangqing'),
                                'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
                                                'price__icontains': request.query_params.get('price'),
                                'onelimittimes__icontains': request.query_params.get('onelimittimes'),
                                'alllimittimes__icontains': request.query_params.get('alllimittimes'),
                                'sfsh__icontains': request.query_params.get('sfsh'),
                                'shhf__icontains': request.query_params.get('shhf'),
                                'thumbsupnum__icontains': request.query_params.get('thumbsupnum'),
                                'crazilynum__icontains': request.query_params.get('crazilynum'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)

    q_objects.add(Q(**{'sfsh': '是'}), Q.AND)

    queryset = Shangpinguanli.objects.filter(q_objects).all()
    count = Shangpinguanli.objects.filter(q_objects).count()
    result = ShangpinguanliSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class ShangpinguanliPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'shangpinmingcheng__icontains': request.query_params.get('shangpinmingcheng'),
            'shangpintupian__icontains': request.query_params.get('shangpintupian'),
            'fenleimingcheng__icontains': request.query_params.get('fenleimingcheng'),
            'jieshao__icontains': request.query_params.get('jieshao'),
            'xiangqing__icontains': request.query_params.get('xiangqing'),
            'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
            'userid__icontains': request.query_params.get('userid'),
            'price__icontains': request.query_params.get('price'),
            'onelimittimes__icontains': request.query_params.get('onelimittimes'),
            'alllimittimes__icontains': request.query_params.get('alllimittimes'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
            'thumbsupnum__icontains': request.query_params.get('thumbsupnum'),
            'crazilynum__icontains': request.query_params.get('crazilynum'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Shangpinguanli.objects.filter(q_objects).all()
        count = Shangpinguanli.objects.filter(q_objects).count()

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
        result = ShangpinguanliSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'shangpinmingcheng__icontains': request.query_params.get('shangpinmingcheng'),
            'shangpintupian__icontains': request.query_params.get('shangpintupian'),
            'fenleimingcheng__icontains': request.query_params.get('fenleimingcheng'),
            'jieshao__icontains': request.query_params.get('jieshao'),
            'xiangqing__icontains': request.query_params.get('xiangqing'),
            'dianpumingcheng__icontains': request.query_params.get('dianpumingcheng'),
            'userid__icontains': request.query_params.get('userid'),
            'price__icontains': request.query_params.get('price'),
            'onelimittimes__icontains': request.query_params.get('onelimittimes'),
            'alllimittimes__icontains': request.query_params.get('alllimittimes'),
            'sfsh__icontains': request.query_params.get('sfsh'),
            'shhf__icontains': request.query_params.get('shhf'),
            'thumbsupnum__icontains': request.query_params.get('thumbsupnum'),
            'crazilynum__icontains': request.query_params.get('crazilynum'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Shangpinguanli.objects.filter(q_objects).all()
        count = Shangpinguanli.objects.filter(q_objects).count()

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
        result = ShangpinguanliSer(items, many=True)
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
        recommended_items = Shangpinguanli.objects.filter(id__in=keys)
        result = [Shangpinguanli.shangpinguanli_to_dict(item) for item in recommended_items]
        return Response({'code': 0, 'data': result})






def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid


# 销量统计 TOP10
class SalesTop10(APIView):
    def get(self, request):
        try:
            # 获取当前登录商家的用户ID
            token = request.META.get('HTTP_TOKEN')
            if not token:
                return Response({'code': 401, 'msg': '未登录'})

            # 解析token获取商家信息
            payload = myjwt.jwt_decode(token)
            shangjia_userid = payload.get('id')

            # 查询该商家的所有商品
            products = Shangpinguanli.objects.filter(
                userid=shangjia_userid
            ).values('id', 'shangpinmingcheng')[:10]

            # 转换为列表（暂时返回模拟数据）
            result = []
            for product in products:
                result.append({
                    'id': product['id'],
                    'shangpinmingcheng': product['shangpinmingcheng'],
                    'sales': 0  # 暂时返回0，后续可以通过订单统计
                })

            return Response({'code': 0, 'data': result})
        except Exception as e:
            print(f"销量统计错误: {str(e)}")
            return Response({'code': 500, 'msg': f'获取销量统计失败: {str(e)}'})

