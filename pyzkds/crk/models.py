from django.db import models

# Create your models here.

# 实体表
class Crk(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    refid = models.IntegerField(null=True, verbose_name='关联表id')
    name = models.CharField(max_length=100, null=True, verbose_name='出入库物品名称')
    sl = models.IntegerField(null=True, verbose_name='出入库数量')
    crkzt = models.CharField(max_length=100, null=True, verbose_name='出入库状态')

    class Meta:
        db_table = 'crk'

    def crk_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'refid': instance.refid,
            'name': instance.name,
            'sl': instance.sl,
            'crkzt': instance.crkzt,
        }