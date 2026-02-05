<template>
  <div class="letter-container">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span class="title">用户联系消息</span>
          <el-button type="primary" @click="refreshData" :loading="loading">
            <el-icon><Refresh /></el-icon>
            刷新
          </el-button>
        </div>
      </template>

      <div class="letter-content">
        <!-- 左侧用户列表 -->
        <div class="user-list">
          <div
            v-for="user in userList"
            :key="user.userId"
            :class="['user-item', { active: selectedUserId === user.userId }]"
            @click="selectUser(user.userId, user.userName)"
          >
            <div class="user-avatar">
              <el-icon><User /></el-icon>
            </div>
            <div class="user-info">
              <div class="user-name">{{ user.userName }}</div>
              <div class="last-message">{{ user.lastMessage }}</div>
            </div>
            <el-badge v-if="user.unreadCount > 0" :value="user.unreadCount" class="unread-badge" />
          </div>
          <div v-if="userList.length === 0" class="empty-list">
            <el-empty description="暂无联系消息" />
          </div>
        </div>

        <!-- 右侧消息区域 -->
        <div class="message-area">
          <div v-if="!selectedUserId" class="no-selection">
            <el-empty description="请选择一个用户查看消息" />
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
              <el-input
                v-model="replyMessage"
                type="textarea"
                :rows="3"
                placeholder="输入回复消息..."
                @keydown.enter.ctrl="sendReply"
              ></el-input>
              <el-button type="primary" @click="sendReply" :loading="sending">
                发送 (Ctrl+Enter)
              </el-button>
            </div>
          </div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, nextTick } from 'vue';
import { Refresh, User } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';
import request from '@/utils/request';

const loading = ref(false);
const sending = ref(false);
const userList = ref([]);
const messageList = ref([]);
const selectedUserId = ref(null);
const selectedUserName = ref('');
const replyMessage = ref('');
const messageListRef = ref(null);
const currentUserId = ref(null);

onMounted(() => {
  getCurrentUser();
  loadUserList();
});

// 获取当前登录用户信息
function getCurrentUser() {
  const user = JSON.parse(localStorage.getItem('user') || '{}');
  currentUserId.value = user.id;
}

// 加载用户列表
async function loadUserList() {
  loading.value = true;
  try {
    const res = await request.get('/letter/queryMsg', {
      params: { receiver: currentUserId.value }
    });

    if (res.code === 0) {
      // 按发送者分组消息
      const userMap = new Map();
      res.data.forEach(msg => {
        const userId = msg.sender === currentUserId.value ? msg.receiver : msg.sender;
        const userName = msg.sender === currentUserId.value ? msg.receiverName : msg.senderName;

        if (!userMap.has(userId)) {
          userMap.set(userId, {
            userId,
            userName,
            lastMessage: msg.msg,
            unreadCount: 0,
            lastTime: msg.sendTime
          });
        }

        // 统计未读消息
        if (msg.sender !== currentUserId.value && msg.readStatus === 0) {
          userMap.get(userId).unreadCount++;
        }
      });

      userList.value = Array.from(userMap.values()).sort((a, b) =>
        new Date(b.lastTime) - new Date(a.lastTime)
      );
    }
  } catch (error) {
    console.error('加载用户列表失败:', error);
    ElMessage.error('加载用户列表失败');
  } finally {
    loading.value = false;
  }
}

// 选择用户
async function selectUser(userId, userName) {
  selectedUserId.value = userId;
  selectedUserName.value = userName;
  await loadMessages(userId);
  markAsRead(userId);
}

// 加载消息列表
async function loadMessages(userId) {
  try {
    const res = await request.get('/letter/querySomeBodyMsg', {
      params: { sender: userId }
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
    ElMessage.error('加载消息失败');
  }
}

// 发送回复
async function sendReply() {
  if (!replyMessage.value.trim()) {
    ElMessage.warning('请输入消息内容');
    return;
  }

  sending.value = true;
  try {
    const res = await request.post('/letter/send', {
      receiver: selectedUserId.value,
      receiverName: selectedUserName.value,
      msg: replyMessage.value
    });

    if (res.code === 0) {
      ElMessage.success('发送成功');
      replyMessage.value = '';
      await loadMessages(selectedUserId.value);
    } else {
      ElMessage.error(res.msg || '发送失败');
    }
  } catch (error) {
    console.error('发送失败:', error);
    ElMessage.error('发送失败');
  } finally {
    sending.value = false;
  }
}

// 标记为已读
async function markAsRead(userId) {
  try {
    await request.post('/letter/update', { sender: userId });
    // 更新用户列表中的未读数
    const user = userList.value.find(u => u.userId === userId);
    if (user) {
      user.unreadCount = 0;
    }
  } catch (error) {
    console.error('标记已读失败:', error);
  }
}

// 刷新数据
function refreshData() {
  loadUserList();
  if (selectedUserId.value) {
    loadMessages(selectedUserId.value);
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

<style scoped lang="scss">
.letter-container {
  padding: 20px;

  .box-card {
    min-height: 700px;

    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;

      .title {
        font-size: 18px;
        font-weight: bold;
        color: #303133;
      }
    }

    .letter-content {
      display: flex;
      height: 650px;
      border: 1px solid #e4e7ed;
      border-radius: 4px;

      .user-list {
        width: 280px;
        border-right: 1px solid #e4e7ed;
        overflow-y: auto;

        .user-item {
          display: flex;
          align-items: center;
          padding: 15px;
          cursor: pointer;
          border-bottom: 1px solid #f0f0f0;
          position: relative;
          transition: background-color 0.3s;

          &:hover {
            background-color: #f5f7fa;
          }

          &.active {
            background-color: #ecf5ff;
          }

          .user-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: #409eff;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 20px;
            margin-right: 12px;
          }

          .user-info {
            flex: 1;
            overflow: hidden;

            .user-name {
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
          }

          .unread-badge {
            position: absolute;
            right: 15px;
            top: 15px;
          }
        }

        .empty-list {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100%;
        }
      }

      .message-area {
        flex: 1;
        display: flex;
        flex-direction: column;

        .no-selection {
          display: flex;
          align-items: center;
          justify-content: center;
          height: 100%;
        }

        .message-content {
          display: flex;
          flex-direction: column;
          height: 100%;

          .message-list {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            background-color: #f5f7fa;

            .message-item {
              margin-bottom: 20px;
              display: flex;

              &.self {
                justify-content: flex-end;

                .message-bubble {
                  background-color: #409eff;
                  color: white;
                }
              }

              &.other {
                justify-content: flex-start;

                .message-bubble {
                  background-color: white;
                  color: #303133;
                }
              }

              .message-bubble {
                max-width: 60%;
                padding: 10px 15px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);

                .message-text {
                  word-break: break-word;
                  line-height: 1.5;
                }

                .message-time {
                  font-size: 12px;
                  margin-top: 5px;
                  opacity: 0.7;
                }
              }
            }
          }

          .send-area {
            padding: 15px;
            border-top: 1px solid #e4e7ed;
            background-color: white;

            .el-button {
              margin-top: 10px;
              width: 100%;
            }
          }
        }
      }
    }
  }
}
</style>

