<template>
  <div class="ai-chat-container">
    <div class="chat-header">
      <h2>AI购物助手</h2>
      <p class="subtitle">有任何购物问题都可以问我哦~</p>
    </div>

    <div class="chat-messages" ref="messagesContainer">
      <div v-if="messages.length === 0" class="welcome-message">
    
        <h3>你好！我是AI购物助手</h3>
        <p>我可以帮你解答关于商品、订单、优惠券等问题</p>
        <div class="quick-questions">
          <div class="quick-question" @click="askQuestion('如何使用优惠券？')">
            如何使用优惠券？
          </div>
          <div class="quick-question" @click="askQuestion('怎么查看我的订单？')">
            怎么查看我的订单？
          </div>
          <div class="quick-question" @click="askQuestion('如何联系商家？')">
            如何联系商家？
          </div>
        </div>
      </div>

      <div v-for="(msg, index) in messages" :key="index" class="message-wrapper">
        <div :class="['message', msg.type]">
          <div class="message-avatar">
            <span v-if="msg.type === 'user'">用户</span>
            <span v-else>千问</span>
          </div>
          <div class="message-content">
            <div class="message-text">{{ msg.content }}</div>
            <div class="message-time">{{ msg.time }}</div>
          </div>
        </div>
      </div>

      <div v-if="loading" class="message-wrapper">
        <div class="message ai">
          <div class="message-avatar"></div>
          <div class="message-content">
            <div class="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="chat-input-area">
      <el-input
        v-model="inputMessage"
        placeholder="输入你的问题..."
        @keyup.enter="sendMessage"
        :disabled="loading"
        class="chat-input"
      >
        <template #append>
          <el-button
            type="primary"
            @click="sendMessage"
            :loading="loading"
            :disabled="!inputMessage.trim()"
          >
            发送
          </el-button>
        </template>
      </el-input>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import request from '@/utils/request'
import { ElMessage } from 'element-plus'

const messages = ref([])
const inputMessage = ref('')
const loading = ref(false)
const messagesContainer = ref(null)

// 发送消息
const sendMessage = async () => {
  if (!inputMessage.value.trim() || loading.value) return

  const question = inputMessage.value.trim()
  inputMessage.value = ''

  // 添加用户消息
  messages.value.push({
    type: 'user',
    content: question,
    time: getCurrentTime()
  })

  scrollToBottom()
  loading.value = true

  try {
    const res = await request({
      url: 'aichat/chat',
      method: 'post',
      data: { question }
    })

    if (res.code === 0) {
      // 添加AI回复
      messages.value.push({
        type: 'ai',
        content: res.data.answer,
        time: getCurrentTime()
      })
    } else {
      ElMessage.error(res.msg || 'AI回复失败')
    }
  } catch (error) {
    ElMessage.error('发送失败，请稍后重试')
  } finally {
    loading.value = false
    scrollToBottom()
  }
}

// 快速提问
const askQuestion = (question) => {
  inputMessage.value = question
  sendMessage()
}

// 获取当前时间
const getCurrentTime = () => {
  const now = new Date()
  return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`
}

// 滚动到底部
const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}
</script>

<style scoped>
.ai-chat-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 120px);
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
  background: #f5f7fa;
}

.chat-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  color: white;
  margin-bottom: 20px;
}

.chat-header h2 {
  margin: 0 0 8px 0;
  font-size: 28px;
}

.subtitle {
  margin: 0;
  opacity: 0.9;
  font-size: 14px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background: white;
  border-radius: 12px;
  margin-bottom: 20px;
}

.welcome-message {
  text-align: center;
  padding: 40px 20px;
}

.welcome-icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.welcome-message h3 {
  color: #333;
  margin-bottom: 10px;
}

.welcome-message p {
  color: #666;
  margin-bottom: 30px;
}

.quick-questions {
  display: flex;
  gap: 10px;
  justify-content: center;
  flex-wrap: wrap;
}

.quick-question {
  padding: 10px 20px;
  background: #f0f2f5;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
  color: #666;
}

.quick-question:hover {
  background: #667eea;
  color: white;
  transform: translateY(-2px);
}

.message-wrapper {
  margin-bottom: 20px;
}

.message {
  display: flex;
  gap: 12px;
  max-width: 80%;
}

.message.user {
  margin-left: auto;
  flex-direction: row-reverse;
}

.message-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  flex-shrink: 0;
}

.message.user .message-avatar {
  background: #667eea;
}

.message.ai .message-avatar {
  background: #f0f2f5;
}

.message-content {
  flex: 1;
}

.message-text {
  padding: 12px 16px;
  border-radius: 12px;
  line-height: 1.6;
  word-wrap: break-word;
}

.message.user .message-text {
  background: #667eea;
  color: white;
}

.message.ai .message-text {
  background: #f0f2f5;
  color: #333;
}

.message-time {
  font-size: 12px;
  color: #999;
  margin-top: 4px;
}

.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 12px 16px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background: #999;
  border-radius: 50%;
  animation: typing 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    transform: translateY(0);
  }
  30% {
    transform: translateY(-10px);
  }
}

.chat-input-area {
  background: white;
  padding: 20px;
  border-radius: 12px;
}

.chat-input {
  width: 100%;
}
</style>

