from django.db import models

# Create your models here.

# 实体表
class Shangpinfenlei(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    fenleimingcheng = models.CharField(max_length=100, null=True, verbose_name='分类名称')
    fenleitupian = models.CharField(max_length=100, null=True, verbose_name='分类图片')

    class Meta:
        db_table = 'shangpinfenlei'

    def shangpinfenlei_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'fenleimingcheng': instance.fenleimingcheng,
            'fenleitupian': instance.fenleitupian,
        }