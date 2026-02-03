from django.db import models

# Create your models here.

# 实体表
class Dianpuxinxi(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    dianpumingcheng = models.CharField(max_length=100, null=True, verbose_name='店铺名称')
    tupian = models.CharField(max_length=100, null=True, verbose_name='图片')
    nicheng = models.CharField(max_length=100, null=True, verbose_name='昵称')
    shangjiadianhua = models.CharField(max_length=100, null=True, verbose_name='商家电话')
    dianpujianjie = models.CharField(max_length=100, null=True, verbose_name='店铺简介')
    dianpudizhi = models.CharField(max_length=100, null=True, verbose_name='店铺地址')
    userid = models.IntegerField(null=True, verbose_name='用户id')
    lat = models.FloatField(null=True, verbose_name='lat')
    lnt = models.FloatField(null=True, verbose_name='lnt')
    conent = models.CharField(max_length=100, null=True, verbose_name='标记')
    sfsh = models.CharField(max_length=100, null=True, verbose_name='是否审核')
    shhf = models.CharField(max_length=100, null=True, verbose_name='审核回复')

    class Meta:
        db_table = 'dianpuxinxi'

    def dianpuxinxi_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'dianpumingcheng': instance.dianpumingcheng,
            'tupian': instance.tupian,
            'nicheng': instance.nicheng,
            'shangjiadianhua': instance.shangjiadianhua,
            'dianpujianjie': instance.dianpujianjie,
            'dianpudizhi': instance.dianpudizhi,
            'userid': instance.userid,
            'lat': instance.lat,
            'lnt': instance.lnt,
            'conent': instance.conent,
            'sfsh': instance.sfsh,
            'shhf': instance.shhf,
        }