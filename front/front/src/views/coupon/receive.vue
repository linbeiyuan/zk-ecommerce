<template>
  <div class="coupon-receive-center">
    <div class="page-header">
      <h2>优惠券领取中心</h2>
      <p class="subtitle">领取优惠券，享受更多优惠</p>
    </div>

    <div class="coupon-list" v-loading="loading">
      <div v-if="couponList.length === 0" class="empty-state">
        <el-empty description="暂无可领取的优惠券" />
      </div>

      <div v-else class="coupon-grid">
        <div
          v-for="coupon in couponList"
          :key="coupon.id"
          class="coupon-card"
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
            <div class="coupon-info">
              <div class="info-item">
                <span class="label">有效期：</span>
                <span class="value">{{ coupon.valid_days }}天</span>
              </div>
              <div class="info-item">
                <span class="label">剩余：</span>
                <span class="value">{{ coupon.remaining_count }}张</span>
              </div>
              <div class="info-item">
                <span class="label">限领：</span>
                <span class="value">{{ coupon.receive_limit }}张/人</span>
              </div>
            </div>
            <el-button
              type="primary"
              size="small"
              @click="handleReceive(coupon)"
              class="receive-btn"
            >
              立即领取
            </el-button>
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
import { useRouter } from 'vue-router'

const router = useRouter()
const loading = ref(false)
const couponList = ref([])

// 获取可领取的优惠券列表
const getCouponList = async () => {
  loading.value = true
  try {
    const res = await request({
      url: 'coupon/list',
      method: 'get'
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

// 领取优惠券
const handleReceive = async (coupon) => {
  try {
    const res = await request({
      url: 'coupon/receive',
      method: 'post',
      data: {
        coupon_id: coupon.id
      }
    })
    if (res.code === 0) {
      ElMessage.success('领取成功！')
      // 刷新列表
      getCouponList()
    } else {
      ElMessage.warning(res.msg || '领取失败')
    }
  } catch (error) {
    ElMessage.error('领取失败，请稍后重试')
  }
}

onMounted(() => {
  getCouponList()
})
</script>

<style scoped>
.coupon-receive-center {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
}

.page-header h2 {
  font-size: 32px;
  color: #333;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 16px;
  color: #666;
}

.coupon-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(450px, 1fr));
  gap: 20px;
}

.coupon-card {
  display: flex;
  border: 2px solid #ff6b6b;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8787 100%);
  transition: all 0.3s;
  box-shadow: 0 2px 8px rgba(255, 107, 107, 0.2);
}

.coupon-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(255, 107, 107, 0.4);
}

.coupon-left {
  width: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  padding: 20px;
  position: relative;
}

.coupon-left::after {
  content: '';
  position: absolute;
  right: -1px;
  top: 50%;
  transform: translateY(-50%);
  width: 2px;
  height: 80%;
  background: white;
  opacity: 0.3;
}

.coupon-amount {
  font-size: 42px;
  font-weight: bold;
  line-height: 1;
}

.coupon-amount .symbol {
  font-size: 24px;
  vertical-align: top;
}

.coupon-condition {
  font-size: 13px;
  margin-top: 8px;
  opacity: 0.9;
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
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 12px;
}

.coupon-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}

.info-item {
  font-size: 14px;
  color: #666;
}

.info-item .label {
  color: #999;
}

.info-item .value {
  color: #333;
  font-weight: 500;
}

.receive-btn {
  align-self: flex-end;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8787 100%);
  border: none;
  padding: 8px 24px;
  font-size: 14px;
}

.receive-btn:hover {
  background: linear-gradient(135deg, #ff5252 0%, #ff6b6b 100%);
}

.empty-state {
  padding: 60px 0;
}
</style>
