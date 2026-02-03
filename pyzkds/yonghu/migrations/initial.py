from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yonghu',
            fields=[
                            (
                    'id',
                                        models.BigAutoField(blank=True, max_length=100, null=True, verbose_name='主键'),
                    
                 ),
                            (
                    'addtime',
                    
                 ),
                            (
                    'yonghuming',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名'),
                    
                 ),
                            (
                    'mima',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='密码'),
                    
                 ),
                            (
                    'shoujihao',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='手机号'),
                    
                 ),
                            (
                    'dizhi',
                                        models.CharField(blank=True, max_length=100, null=True, verbose_name='地址'),
                    
                 ),
                            (
                    'money',
                    
                 ),
                            (
                    'jf',
                    
                 ),
            
            ],
            options={
                'db_table': 'yonghu',
            },
        ),



    ]
