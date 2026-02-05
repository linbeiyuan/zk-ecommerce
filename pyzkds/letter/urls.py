from django.urls import path
from . import views

urlpatterns = [
    path('queryMsg', views.query_msg, name='query_msg'),
    path('querySomeBodyMsg', views.query_somebody_msg, name='query_somebody_msg'),
    path('send', views.send_message, name='send_message'),
    path('update', views.update_read_status, name='update_read_status'),
    path('queryLetterList', views.query_letter_list, name='query_letter_list'),
]