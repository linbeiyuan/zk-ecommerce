from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat_with_ai),  # AI对话
    path('history', views.get_chat_history),  # 获取聊天历史
]
