<!-- 代码已包含 CSS：使用 TailwindCSS , 安装 TailwindCSS 后方可看到布局样式效果 -->
<template>
  <div class="min-h-screen bg-gray-100 flex justify-center items-start py-8">
    <div class="w-[1000px] bg-white rounded-xl shadow-lg flex flex-col h-[800px]">
      <!-- 头部区域 -->
      <div class="p-4 border-b border-gray-100">
        <h2 class="text-xl font-semibold text-gray-800">AI 智能助手</h2>
        <p class="text-sm text-gray-500 mt-1">24/7 为您提供智能对话服务</p>
      </div>
      <!-- 对话内容区域 -->
      <div ref="chatContainer" class="flex-1 overflow-y-auto p-6 space-y-6">
        <div v-for="(message, index) in messages" :key="index" class="flex" :class="message.isUser ? 'justify-end' : 'justify-start'">
          <div class="max-w-[70%] break-words p-4 rounded-lg shadow-sm"
               :class="message.isUser ? 'bg-blue-500 text-white' : 'bg-gray-50 text-gray-800'">
            <p class="text-sm leading-relaxed">{{ message.content }}</p>
            <div class="text-xs mt-1 opacity-70 text-right">{{ message.time }}</div>
          </div>
        </div>
        <div v-if="isLoading" class="flex items-center space-x-2">
          <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
      <!-- 输入区域 -->
      <div class="border-t border-gray-100 p-6 bg-white rounded-b-xl">
        <div class="relative flex items-end max-w-4xl mx-auto">
  <textarea
      ref="inputRef"
      v-model="userInput"
      rows="1"
      class="w-full resize-none rounded-lg border border-gray-200 bg-gray-50 p-4 pr-12 text-sm focus:border-blue-500 focus:ring-1 focus:ring-blue-500 shadow-sm"
      placeholder="请输入您的问题..."
      @input="autoResize"
      @keydown.enter.prevent="handleSend"
  ></textarea>
          <button
              class="!rounded-button absolute bottom-2 right-2 px-4 py-2 bg-blue-500 text-white hover:bg-blue-600 whitespace-nowrap transition-colors duration-200"
              @click="handleSend"
              :disabled="isLoading || !userInput.trim()"
          >
            发送
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { ref, onMounted, nextTick } from 'vue';
import request from "@/utils/request";
interface Message {
  content: string;
  isUser: boolean;
  time: string;
}
const chatContainer = ref<HTMLElement | null>(null);
const inputRef = ref<HTMLTextAreaElement | null>(null);
const userInput = ref('');
const isLoading = ref(false);
const messages = ref<Message[]>([
  {
    content: '你好！我是AI助手，很高兴为您服务。请问有什么我可以帮助您的吗？',
    isUser: false,
    time: '14:00'
  }
]);
const getCurrentTime = () => {
  const now = new Date();
  return `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
};
const autoResize = () => {
  if (inputRef.value) {
    inputRef.value.style.height = 'auto';
    inputRef.value.style.height = `${inputRef.value.scrollHeight}px`;
  }
};
const scrollToBottom = async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};
const simulateAIResponse = async (trimmedInput) => {
  isLoading.value = true;
  // await new Promise(resolve => setTimeout(resolve, 1500));
  const aiResponses = [];
  // const randomResponse = aiResponses[Math.floor(Math.random() * aiResponses.length)];
  request({
    url:`openai/openAi/${trimmedInput}`,
    method:'post',
  }).then((data)=>{
    messages.value.push({
      content: data.msg,
      isUser: false,
      time: getCurrentTime()
    });
    isLoading.value = false;
    scrollToBottom();
    // console.log(data.msg)
  })

};
const handleSend = async () => {
  const trimmedInput = userInput.value.trim();
  if (!trimmedInput || isLoading.value) return;

  messages.value.push({
    content: trimmedInput,
    isUser: true,
    time: getCurrentTime()
  });
  userInput.value = '';
  await scrollToBottom();
  await simulateAIResponse(trimmedInput);
  if (inputRef.value) {
    inputRef.value.style.height = 'auto';
  }
};
onMounted(() => {
  scrollToBottom();
});
</script>


