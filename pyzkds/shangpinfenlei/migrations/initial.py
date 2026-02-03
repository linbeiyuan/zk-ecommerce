from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shangpinfenlei',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'fenleimingcheng',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='分类名称'),
                    
                 ),
                            (
                    'fenleitupian',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='分类图片'),
                    
                 ),
            
            ],
            options={
                'db_table': 'shangpinfenlei',
            },
        ),



    ]
