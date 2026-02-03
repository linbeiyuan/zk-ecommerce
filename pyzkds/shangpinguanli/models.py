from django.db import models

# Create your models here.

# 实体表
class Shangpinguanli(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    shangpinmingcheng = models.CharField(max_length=100, null=True, verbose_name='商品名称')
    shangpintupian = models.CharField(max_length=100, null=True, verbose_name='商品图片')
    fenleimingcheng = models.CharField(max_length=100, null=True, verbose_name='分类名称')
    jieshao = models.CharField(max_length=100, null=True, verbose_name='介绍')
    xiangqing = models.CharField(max_length=100, null=True, verbose_name='详情')
    dianpumingcheng = models.CharField(max_length=100, null=True, verbose_name='店铺名称')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    price = models.FloatField(null=True, verbose_name='价格')
    onelimittimes = models.IntegerField(null=True, verbose_name='单限')
    alllimittimes = models.IntegerField(null=True, verbose_name='库存')
    sfsh = models.CharField(max_length=100, null=True, verbose_name='是否审核')
    shhf = models.CharField(max_length=100, null=True, verbose_name='审核回复')
    thumbsupnum = models.IntegerField(null=True, verbose_name='赞')
    crazilynum = models.IntegerField(null=True, verbose_name='踩')

    class Meta:
        db_table = 'shangpinguanli'

    def shangpinguanli_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'shangpinmingcheng': instance.shangpinmingcheng,
            'shangpintupian': instance.shangpintupian,
            'fenleimingcheng': instance.fenleimingcheng,
            'jieshao': instance.jieshao,
            'xiangqing': instance.xiangqing,
            'dianpumingcheng': instance.dianpumingcheng,
            'userid': instance.userid,
            'price': instance.price,
            'onelimittimes': instance.onelimittimes,
            'alllimittimes': instance.alllimittimes,
            'sfsh': instance.sfsh,
            'shhf': instance.shhf,
            'thumbsupnum': instance.thumbsupnum,
            'crazilynum': instance.crazilynum,
        }