from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jifenshangdian',
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
                    'shangpinjianjie',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品简介'),
                    
                 ),
                            (
                    'shangpinxiangqing',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='商品详情'),
                    
                 ),
                            (
                    'jifen',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='积分'),
                    
                 ),
            
            ],
            options={
                'db_table': 'jifenshangdian',
            },
        ),



    ]
