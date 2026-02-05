<template>
  <div class="letter-container">
    <div class="letter-card">
      <div class="card-header">
        <span class="title">我的消息</span>
        <button @click="refreshData" class="refresh-btn" :disabled="loading">
          <i class="fas fa-sync-alt" :class="{ 'fa-spin': loading }"></i>
          刷新
        </button>
      </div>

      <div class="letter-content">
        <!-- 左侧商家列表 -->
        <div class="shop-list">
          <div
            v-for="shop in shopList"
            :key="shop.shopId"
            :class="['shop-item', { active: selectedShopId === shop.shopId }]"
            @click="selectShop(shop.shopId, shop.shopName)"
          >
            <div class="shop-avatar">
              <i class="fas fa-store"></i>
            </div>
            <div class="shop-info">
              <div class="shop-name">{{ shop.shopName }}</div>
              <div class="last-message">{{ shop.lastMessage }}</div>
            </div>
            <span v-if="shop.unreadCount > 0" class="unread-badge">{{ shop.unreadCount }}</span>
          </div>
          <div v-if="shopList.length === 0" class="empty-list">
            <p>暂无消息</p>
          </div>
        </div>

        <!-- 右侧消息区域 -->
        <div class="message-area">
          <div v-if="!selectedShopId" class="no-selection">
            <p>请选择一个商家查看消息</p>
          </div>
          <div v-else class="message-content">
            <!-- 消息列表 -->
            <div class="message-list" ref="messageListRef">
              <div
                v-for="msg in messageList"
                :key="msg.id"
                :class="['message-item', msg.isSelf ? 'self' : 'other']"
              >
                <div class="message-bubble">
                  <div class="message-text">{{ msg.msg }}</div>
                  <div class="message-time">{{ formatTime(msg.sendTime) }}</div>
                </div>
              </div>
            </div>

            <!-- 发送消息区域 -->
            <div class="send-area">
              <textarea
                v-model="replyMessage"
                placeholder="输入消息内容..."
                rows="3"
                @keydown.ctrl.enter="sendReply"
              ></textarea>
              <button @click="sendReply" :disabled="sending" class="send-btn">
                {{ sending ? '发送中...' : '发送 (Ctrl+Enter)' }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import request from '@/utils/request';
import { notify } from '@/utils/element';

const loading = ref(false);
const sending = ref(false);
const shopList = ref([]);
const messageList = ref([]);
const selectedShopId = ref(null);
const selectedShopName = ref('');
const replyMessage = ref('');
const messageListRef = ref(null);
const currentUserId = ref(null);

onMounted(() => {
  getCurrentUser();
  loadShopList();
});

// 获取当前登录用户信息
function getCurrentUser() {
  const user = JSON.parse(localStorage.getItem('user') || '{}');
  currentUserId.value = user.id;
}

// 加载商家列表
async function loadShopList() {
  loading.value = true;
  try {
    const res = await request({
      url: 'letter/queryMsg',
      method: 'get'
    });

    if (res.code === 0) {
      // 按商家分组消息
      const shopMap = new Map();
      res.data.forEach(msg => {
        const shopId = msg.sender === currentUserId.value ? msg.receiver : msg.sender;
        const shopName = msg.sender === currentUserId.value ? msg.receiverName : msg.senderName;

        if (!shopMap.has(shopId)) {
          shopMap.set(shopId, {
            shopId,
            shopName,
            lastMessage: msg.msg,
            unreadCount: 0,
            lastTime: msg.sendTime
          });
        }

        // 统计未读消息
        if (msg.sender !== currentUserId.value && msg.readStatus === 0) {
          shopMap.get(shopId).unreadCount++;
        }
      });

      shopList.value = Array.from(shopMap.values()).sort((a, b) =>
        new Date(b.lastTime) - new Date(a.lastTime)
      );
    }
  } catch (error) {
    console.error('加载商家列表失败:', error);
    notify('加载商家列表失败', { type: 'error' });
  } finally {
    loading.value = false;
  }
}

// 选择商家
async function selectShop(shopId, shopName) {
  selectedShopId.value = shopId;
  selectedShopName.value = shopName;
  await loadMessages(shopId);
  markAsRead(shopId);
}

// 加载消息列表
async function loadMessages(shopId) {
  try {
    const res = await request({
      url: 'letter/querySomeBodyMsg',
      method: 'get',
      params: { sender: shopId }
    });

    if (res.code === 0) {
      messageList.value = res.data.map(msg => ({
        ...msg,
        isSelf: msg.sender === currentUserId.value
      }));
      await nextTick();
      scrollToBottom();
    }
  } catch (error) {
    console.error('加载消息失败:', error);
    notify('加载消息失败', { type: 'error' });
  }
}

// 发送回复
async function sendReply() {
  if (!replyMessage.value.trim()) {
    notify('请输入消息内容', { type: 'warning' });
    return;
  }

  sending.value = true;
  try {
    const res = await request({
      url: 'letter/send',
      method: 'post',
      data: {
        receiver: selectedShopId.value,
        receiverName: selectedShopName.value,
        msg: replyMessage.value
      }
    });

    if (res.code === 0) {
      notify('发送成功', { type: 'success' });
      replyMessage.value = '';
      await loadMessages(selectedShopId.value);
    } else {
      notify(res.msg || '发送失败', { type: 'error' });
    }
  } catch (error) {
    console.error('发送失败:', error);
    notify('发送失败', { type: 'error' });
  } finally {
    sending.value = false;
  }
}

// 标记为已读
async function markAsRead(shopId) {
  try {
    await request({
      url: 'letter/update',
      method: 'post',
      data: { sender: shopId }
    });
    // 更新商家列表中的未读数
    const shop = shopList.value.find(s => s.shopId === shopId);
    if (shop) {
      shop.unreadCount = 0;
    }
  } catch (error) {
    console.error('标记已读失败:', error);
  }
}

// 刷新数据
function refreshData() {
  loadShopList();
  if (selectedShopId.value) {
    loadMessages(selectedShopId.value);
  }
}

// 滚动到底部
function scrollToBottom() {
  if (messageListRef.value) {
    messageListRef.value.scrollTop = messageListRef.value.scrollHeight;
  }
}

// 格式化时间
function formatTime(time) {
  if (!time) return '';
  const date = new Date(time);
  return `${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${String(date.getMinutes()).padStart(2, '0')}`;
}
</script>

<style scoped>
.letter-container {
  padding: 20px;
  background-color: #f5f7fa;
  min-height: 100vh;
}

.letter-card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid #e4e7ed;
}

.title {
  font-size: 20px;
  font-weight: bold;
  color: #303133;
}

.refresh-btn {
  padding: 8px 16px;
  background-color: #409eff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: background-color 0.3s;
}

.refresh-btn:hover:not(:disabled) {
  background-color: #66b1ff;
}

.refresh-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.fa-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.letter-content {
  display: flex;
  height: 650px;
}

.shop-list {
  width: 280px;
  border-right: 1px solid #e4e7ed;
  overflow-y: auto;
}

.shop-item {
  display: flex;
  align-items: center;
  padding: 15px;
  cursor: pointer;
  border-bottom: 1px solid #f0f0f0;
  position: relative;
  transition: background-color 0.3s;
}

.shop-item:hover {
  background-color: #f5f7fa;
}

.shop-item.active {
  background-color: #ecf5ff;
}

.shop-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: #67c23a;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 20px;
  margin-right: 12px;
}

.shop-info {
  flex: 1;
  overflow: hidden;
}

.shop-name {
  font-size: 14px;
  font-weight: 500;
  color: #303133;
  margin-bottom: 4px;
}

.last-message {
  font-size: 12px;
  color: #909399;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.unread-badge {
  position: absolute;
  right: 15px;
  top: 15px;
  background-color: #f56c6c;
  color: white;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 12px;
}

.empty-list {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #909399;
}

.message-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.no-selection {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #909399;
  font-size: 16px;
}

.message-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background-color: #f5f7fa;
}

.message-item {
  margin-bottom: 20px;
  display: flex;
}

.message-item.self {
  justify-content: flex-end;
}

.message-item.self .message-bubble {
  background-color: #409eff;
  color: white;
}

.message-item.other {
  justify-content: flex-start;
}

.message-item.other .message-bubble {
  background-color: white;
  color: #303133;
}

.message-bubble {
  max-width: 60%;
  padding: 10px 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-text {
  word-break: break-word;
  line-height: 1.5;
}

.message-time {
  font-size: 12px;
  margin-top: 5px;
  opacity: 0.7;
}

.send-area {
  padding: 15px;
  border-top: 1px solid #e4e7ed;
  background-color: white;
}

.send-area textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  resize: none;
  font-size: 14px;
  font-family: inherit;
}

.send-area textarea:focus {
  outline: none;
  border-color: #409eff;
}

.send-btn {
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  background-color: #409eff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.send-btn:hover:not(:disabled) {
  background-color: #66b1ff;
}

.send-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>




