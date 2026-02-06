"""springboot4oKm0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pyzkds/address/', include('address.urls')),
    path('pyzkds/orders/', include('orders.urls')),
    path('pyzkds/cart/', include('cart.urls')),
    path('pyzkds/news/', include('news.urls')),
    path('pyzkds/messagess/', include('messagess.urls')),
    path('pyzkds/crk/', include('crk.urls')),
    path('pyzkds/shangpinguanli/', include('shangpinguanli.urls')),
    path('pyzkds/discussshangpinguanli/', include('discussshangpinguanli.urls')),
    path('pyzkds/shangpinfenlei/', include('shangpinfenlei.urls')),
    path('pyzkds/dianpuxinxi/', include('dianpuxinxi.urls')),
    path('pyzkds/discussdianpuxinxi/', include('discussdianpuxinxi.urls')),
    path('pyzkds/jifenshangdian/', include('jifenshangdian.urls')),
    path('pyzkds/yonghu/', include('yonghu.urls')),
    path('pyzkds/shangjia/', include('shangjia.urls')),

    path('pyzkds/users/', include('users.urls')),
    path('pyzkds/forum/', include('forum.urls')),
    path('pyzkds/storeup/', include('storeup.urls')),
    path('pyzkds/config/', include('config.urls')),
    path('pyzkds/file/', include('file.urls')),
    path('pyzkds/', include('common.urls')),
    path('pyzkds/consultation/', include('consultation.urls')),
    path('pyzkds/letter/', include('letter.urls')),
    path('pyzkds/coupon/', include('coupon.urls')),
    path('pyzkds/aichat/', include('aichat.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)