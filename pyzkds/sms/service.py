"""
短信服务模块
使用容联云发送短信验证码
"""
import random
import time
import redis
from ronglian_sms_sdk import SmsSDK
from django.conf import settings
import os

# 容联云配置
ACCOUNT_SID = '2c94811c9035ff9f0191dc01fcf0587f'
AUTH_TOKEN = 'c68cc0510bff41f0b45e1a8e93ad39e5'
APP_ID = '2c94811c9035ff9f0191dc01fe8e5886'
TEMPLATE_ID = '1'  # 短信模板ID，需要在容联云后台创建

# Redis 连接
redis_host = os.environ.get('REDIS_HOST', '127.0.0.1')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)


def generate_code():
    """生成4位随机验证码（容联云模板要求1-4位）"""
    return str(random.randint(1000, 9999))


def send_sms_code(phone):
    """
    发送短信验证码

    Args:
        phone: 手机号

    Returns:
        dict: {
            'success': True/False,
            'message': '提示信息',
            'code': '验证码'（仅开发环境返回）
        }
    """
    # 检查1分钟内是否已发送
    time_key = f'sms_time:{phone}'
    if redis_client.exists(time_key):
        remaining = redis_client.ttl(time_key)
        return {
            'success': False,
            'message': f'请{remaining}秒后再试'
        }

    # 生成验证码
    code = generate_code()

    # 检查是否启用真实短信发送（通过环境变量控制）
    enable_real_sms = os.environ.get('ENABLE_REAL_SMS', 'false').lower() == 'true'
    print(f"[SMS DEBUG] ENABLE_REAL_SMS环境变量: {os.environ.get('ENABLE_REAL_SMS', 'not set')}")
    print(f"[SMS DEBUG] enable_real_sms: {enable_real_sms}")
    print(f"[SMS DEBUG] 手机号: {phone}, 验证码: {code}")

    # 如果未启用真实短信，则模拟发送
    if not enable_real_sms:
        print(f"[SMS DEBUG] 模拟发送模式")
        # 存储验证码到 Redis（5分钟过期）
        code_key = f'sms:{phone}'
        redis_client.setex(code_key, 300, code)

        # 设置1分钟发送限制
        redis_client.setex(time_key, 60, int(time.time()))

        return {
            'success': True,
            'message': '验证码发送成功（开发环境）',
            'code': code  # 开发环境返回验证码方便测试
        }

    # 启用真实短信：发送真实短信
    print(f"[SMS DEBUG] 真实发送模式 - 开始调用容联云API")
    try:
        sdk = SmsSDK(ACCOUNT_SID, AUTH_TOKEN, APP_ID)
        print(f"[SMS DEBUG] SDK初始化成功")
        # 发送短信，参数：模板ID, 手机号, [验证码, 有效期（分钟）]
        result = sdk.sendMessage(TEMPLATE_ID, phone, [code, '5'])
        print(f"[SMS DEBUG] 容联云返回结果类型: {type(result)}")
        print(f"[SMS DEBUG] 容联云返回结果: {result}")

        # 处理返回结果（可能是字典或字符串）
        if isinstance(result, str):
            # 如果返回的是字符串，尝试解析为JSON
            import json
            try:
                result = json.loads(result)
            except:
                return {
                    'success': False,
                    'message': f'发送失败：{result}'
                }

        if result.get('statusCode') == '000000':
            print(f"[SMS DEBUG] 短信发送成功")
            # 存储验证码到 Redis（5分钟过期）
            code_key = f'sms:{phone}'
            redis_client.setex(code_key, 300, code)

            # 设置1分钟发送限制
            redis_client.setex(time_key, 60, int(time.time()))

            return {
                'success': True,
                'message': '验证码发送成功'
            }
        else:
            return {
                'success': False,
                'message': f'发送失败：{result.get("statusMsg", "未知错误")}'
            }
    except Exception as e:
        return {
            'success': False,
            'message': f'发送失败：{str(e)}'
        }


def verify_sms_code(phone, code):
    """
    验证短信验证码

    Args:
        phone: 手机号
        code: 用户输入的验证码

    Returns:
        dict: {
            'success': True/False,
            'message': '提示信息'
        }
    """
    code_key = f'sms:{phone}'
    stored_code = redis_client.get(code_key)

    if not stored_code:
        return {
            'success': False,
            'message': '验证码已过期或不存在'
        }

    if stored_code == code:
        # 验证成功，删除验证码（防止重复使用）
        redis_client.delete(code_key)
        return {
            'success': True,
            'message': '验证成功'
        }
    else:
        return {
            'success': False,
            'message': '验证码错误'
        }


def get_sms_history(phone):
    """
    获取某手机号的验证码历史（用于管理）

    Args:
        phone: 手机号

    Returns:
        list: 验证码历史记录
    """
    code_key = f'sms:{phone}'
    code = redis_client.get(code_key)
    ttl = redis_client.ttl(code_key)

    if code:
        return [{
            'phone': phone,
            'code': code,
            'remaining_seconds': ttl
        }]
    else:
        return []
