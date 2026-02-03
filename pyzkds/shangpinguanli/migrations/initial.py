from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shangpinguanli',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'shangpinmingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品名称'),
                    
                 ),
                            (
                    'shangpintupian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品图片'),
                    
                 ),
                            (
                    'fenleimingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='分类名称'),
                    
                 ),
                            (
                    'jieshao',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='介绍'),
                    
                 ),
                            (
                    'xiangqing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='详情'),
                    
                 ),
                            (
                    'dianpumingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺名称'),
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
                            (
                    'price',
                    
                 ),
                            (
                    'onelimittimes',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='单限'),
                    
                 ),
                            (
                    'alllimittimes',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='库存'),
                    
                 ),
                            (
                    'sfsh',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='是否审核'),
                    
                 ),
                            (
                    'shhf',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='审核回复'),
                    
                 ),
                            (
                    'thumbsupnum',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='赞'),
                    
                 ),
                            (
                    'crazilynum',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='踩'),
                    
                 ),
            
            ],
            options={
                'db_table': 'shangpinguanli',
            },
        ),



    ]
