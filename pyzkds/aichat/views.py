from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatHistory
import requests
import json
from utils.myjwt import myjwt

# 通义千问API配置
QWEN_API_KEY = "sk-227e1489de0f4bb6b2c69d3e0937a819"  # 通义千问API密钥
QWEN_API_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

# Create your views here.


@api_view(['POST'])
def chat_with_ai(request):
    """与AI对话"""
    try:
        # 获取用户信息
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)
        userid = user_info['data'].get('userid') if 'data' in user_info else user_info.get('id')

        # 获取用户问题
        question = request.data.get('question', '').strip()
        if not question:
            return Response({'code': 1, 'msg': '问题不能为空'})

        # 调用通义千问API
        answer = call_qwen_api(question)

        if answer:
            # 保存聊天记录
            ChatHistory.objects.create(
                userid=userid,
                question=question,
                answer=answer
            )

            return Response({
                'code': 0,
                'msg': '成功',
                'data': {
                    'question': question,
                    'answer': answer
                }
            })
        else:
            return Response({'code': 1, 'msg': 'AI服务暂时不可用，请稍后重试'})

    except Exception as e:
        return Response({'code': 500, 'msg': f'对话失败: {str(e)}'})


def call_qwen_api(question):
    """调用通义千问API"""
    try:
        headers = {
            'Authorization': f'Bearer {QWEN_API_KEY}',
            'Content-Type': 'application/json; charset=utf-8'
        }

        data = {
            "model": "qwen-turbo",
            "input": {
                "messages": [
                    {
                        "role": "system",
                        "content": "你是一个友好的购物助手，帮助用户解答关于购物、商品、订单等问题。请用简洁明了的语言回答，避免使用过多的表情符号。"
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            },
            "parameters": {
                "result_format": "message"
            }
        }

        response = requests.post(QWEN_API_URL, headers=headers, json=data, timeout=30)

        if response.status_code == 200:
            result = response.json()
            if result.get('output') and result['output'].get('choices'):
                answer = result['output']['choices'][0]['message']['content']
                # 确保返回的内容是有效的UTF-8字符串
                return answer.encode('utf-8', errors='ignore').decode('utf-8')

        return None

    except Exception as e:
        print(f"调用通义千问API失败: {str(e)}")
        return None


@api_view(['GET'])
def get_chat_history(request):
    """获取聊天历史"""
    try:
        # 获取用户信息
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        user_info = myjwt.jwt_decode(token)
        userid = user_info['data'].get('userid') if 'data' in user_info else user_info.get('id')

        # 获取分页参数
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 20))

        # 查询聊天历史
        history = ChatHistory.objects.filter(userid=userid)
        total = history.count()

        # 分页
        start = (page - 1) * limit
        end = start + limit
        history_list = history[start:end]

        # 构建返回数据
        data = []
        for item in history_list:
            data.append({
                'id': item.id,
                'question': item.question,
                'answer': item.answer,
                'addtime': item.addtime.strftime('%Y-%m-%d %H:%M:%S')
            })

        return Response({
            'code': 0,
            'msg': '成功',
            'data': {
                'list': data,
                'total': total
            }
        })

    except Exception as e:
        return Response({'code': 500, 'msg': f'获取历史失败: {str(e)}'})
