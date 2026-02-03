from django.db import models

# Create your models here.

# 实体表
class Shangjia(models.Model):
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    yonghuming = models.CharField(max_length=100, null=True, verbose_name='用户名')
    mima = models.CharField(max_length=100, null=True, verbose_name='密码')
    shoujihao = models.CharField(max_length=100, null=True, verbose_name='手机号')
    shangjiamingcheng = models.CharField(max_length=100, null=True, verbose_name='商家名称')
    money = models.FloatField(null=True, verbose_name='余额')
    jf = models.FloatField(null=True, verbose_name='积分')

    class Meta:
        db_table = 'shangjia'

    def shangjia_to_dict(instance):
        return {
            'id': instance.id,
            'addtime': instance.addtime,
            'yonghuming': instance.yonghuming,
            'mima': instance.mima,
            'shoujihao': instance.shoujihao,
            'shangjiamingcheng': instance.shangjiamingcheng,
            'money': instance.money,
            'jf': instance.jf,
        }