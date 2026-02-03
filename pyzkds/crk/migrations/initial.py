from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crk',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'refid',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='关联表id'),
                    
                 ),
                            (
                    'name',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='出入库物品名称'),
                    
                 ),
                            (
                    'sl',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='出入库数量'),
                    
                 ),
                            (
                    'crkzt',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='出入库状态'),
                    
                 ),
            
            ],
            options={
                'db_table': 'crk',
            },
        ),



    ]
