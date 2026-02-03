from django.db import models

# Create your models here.

# 实体表
class Jifenshangdian(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    shangpinmingcheng = models.CharField(max_length=100, null=True, verbose_name='商品名称')
    shangpintupian = models.CharField(max_length=100, null=True, verbose_name='商品图片')
    shangpinjianjie = models.CharField(max_length=100, null=True, verbose_name='商品简介')
    shangpinxiangqing = models.CharField(max_length=100, null=True, verbose_name='商品详情')
    jifen = models.IntegerField(null=True, verbose_name='积分')

    class Meta:
        db_table = 'jifenshangdian'

    def jifenshangdian_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'shangpinmingcheng': instance.shangpinmingcheng,
            'shangpintupian': instance.shangpintupian,
            'shangpinjianjie': instance.shangpinjianjie,
            'shangpinxiangqing': instance.shangpinxiangqing,
            'jifen': instance.jifen,
        }