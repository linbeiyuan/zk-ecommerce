# asgi.py

import os
import django

# 必须先设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

# 初始化Django
django.setup()

# 然后才能导入Django相关模块
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from . import routing  # 导入路由配置

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP 请求
    "websocket": URLRouter(
        routing.websocket_urlpatterns  # WebSocket 路由
    ),
})