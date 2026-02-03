from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dianpuxinxi',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'dianpumingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺名称'),
                    
                 ),
                            (
                    'tupian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='图片'),
                    
                 ),
                            (
                    'nicheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='昵称'),
                    
                 ),
                            (
                    'shangjiadianhua',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商家电话'),
                    
                 ),
                            (
                    'dianpujianjie',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺简介'),
                    
                 ),
                            (
                    'dianpudizhi',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺地址'),
                    
                 ),
                            (
                    'userid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='用户id'),
                    
                 ),
                            (
                    'lat',
                    
                 ),
                            (
                    'lnt',
                    
                 ),
                            (
                    'conent',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='标记'),
                    
                 ),
                            (
                    'sfsh',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='是否审核'),
                    
                 ),
                            (
                    'shhf',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='审核回复'),
                    
                 ),
            
            ],
            options={
                'db_table': 'dianpuxinxi',
            },
        ),



    ]
