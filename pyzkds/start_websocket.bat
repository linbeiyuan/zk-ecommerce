@echo off
echo 正在启动Django WebSocket服务器...
echo 使用Daphne ASGI服务器，支持WebSocket连接
echo 服务器地址: http://0.0.0.0:8000
echo.
daphne -b 0.0.0.0 -p 8000 configs.asgi:application
