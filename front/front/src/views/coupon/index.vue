<template>
  <div class="coupon-center">
    <div class="page-header">
      <h2>我的优惠券</h2>
    </div>

    <el-tabs v-model="activeTab" @tab-change="handleTabChange">
      <el-tab-pane label="未使用" name="1"></el-tab-pane>
      <el-tab-pane label="已使用" name="2"></el-tab-pane>
      <el-tab-pane label="已过期" name="3"></el-tab-pane>
    </el-tabs>

    <div class="coupon-list" v-loading="loading">
      <div v-if="couponList.length === 0" class="empty-state">
        <el-empty description="暂无优惠券" />
      </div>

      <div v-else class="coupon-grid">
        <div
          v-for="coupon in couponList"
          :key="coupon.id"
          class="coupon-card"
          :class="{ 'used': coupon.status === 2, 'expired': coupon.status === 3 }"
        >
          <div class="coupon-left">
            <div class="coupon-amount">
              <span class="symbol">¥</span>
              <span class="value">{{ coupon.discount_amount }}</span>
            </div>
            <div class="coupon-condition">
              满{{ coupon.condition_amount }}元可用
            </div>
          </div>

          <div class="coupon-right">
            <div class="coupon-name">{{ coupon.name }}</div>
            <div class="coupon-time">
              有效期至：{{ formatDate(coupon.expire_time) }}
            </div>
            <div class="coupon-status">
              <el-tag v-if="coupon.status === 1" type="success">未使用</el-tag>
              <el-tag v-else-if="coupon.status === 2" type="info">已使用</el-tag>
              <el-tag v-else type="danger">已过期</el-tag>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import request from '@/utils/request'
import { ElMessage } from 'element-plus'

const activeTab = ref('1')
const loading = ref(false)
const couponList = ref([])

// 获取优惠券列表
const getCouponList = async () => {
  loading.value = true
  try {
    const res = await request({
      url: 'coupon/my',
      method: 'get',
      params: {
        status: activeTab.value
      }
    })
    if (res.code === 0) {
      couponList.value = res.data
    }
  } catch (error) {
    ElMessage.error('获取优惠券列表失败')
  } finally {
    loading.value = false
  }
}

// 切换标签
const handleTabChange = () => {
  getCouponList()
}

// 格式化日期
const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN')
}

onMounted(() => {
  getCouponList()
})
</script>

<style scoped>
.coupon-center {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  margin-bottom: 20px;
}

.page-header h2 {
  font-size: 24px;
  color: #333;
}

.coupon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.coupon-card {
  display: flex;
  border: 2px solid #ff6b6b;
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8787 100%);
  transition: transform 0.3s;
}

.coupon-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
}

.coupon-card.used,
.coupon-card.expired {
  background: #e0e0e0;
  border-color: #999;
  opacity: 0.7;
}

.coupon-left {
  width: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  padding: 20px;
}

.coupon-amount {
  font-size: 36px;
  font-weight: bold;
}

.coupon-amount .symbol {
  font-size: 20px;
}

.coupon-condition {
  font-size: 12px;
  margin-top: 5px;
}

.coupon-right {
  flex: 1;
  padding: 20px;
  background: white;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.coupon-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.coupon-time {
  font-size: 14px;
  color: #666;
  margin-top: 10px;
}
</style>
