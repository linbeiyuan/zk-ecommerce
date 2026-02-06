<template>
  <div class="coupon-manage">
    <el-card>
      <template #header>
        <div class="card-header">
          <span>优惠券管理</span>
          <el-button type="primary" @click="handleAdd">创建优惠券</el-button>
        </div>
      </template>

      <el-table :data="tableData" v-loading="loading">
        <el-table-column prop="name" label="优惠券名称" />
        <el-table-column prop="discount_amount" label="优惠金额" />
        <el-table-column prop="condition_amount" label="使用条件" />
        <el-table-column prop="total_count" label="发行总量" />
        <el-table-column prop="remaining_count" label="剩余数量" />
        <el-table-column label="操作" width="150">
          <template #default="{ row }">
            <el-button type="danger" size="small" @click="handleDelete(row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 创建优惠券对话框 -->
    <el-dialog v-model="dialogVisible" title="创建优惠券" width="600px">
      <el-form :model="form" label-width="120px">
        <el-form-item label="优惠券名称">
          <el-input v-model="form.name" placeholder="例如：新人专享券" />
        </el-form-item>
        <el-form-item label="满足金额">
          <el-input-number v-model="form.condition_amount" :min="0" />
        </el-form-item>
        <el-form-item label="优惠金额">
          <el-input-number v-model="form.discount_amount" :min="0" />
        </el-form-item>
        <el-form-item label="发行总量">
          <el-input-number v-model="form.total_count" :min="1" />
        </el-form-item>
        <el-form-item label="每人限领">
          <el-input-number v-model="form.receive_limit" :min="1" />
        </el-form-item>
        <el-form-item label="有效天数">
          <el-input-number v-model="form.valid_days" :min="1" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleSubmit">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import request from '@/utils/request'
import { ElMessage, ElMessageBox } from 'element-plus'

const loading = ref(false)
const tableData = ref([])
const dialogVisible = ref(false)
const form = ref({
  name: '',
  condition_amount: 100,
  discount_amount: 20,
  total_count: 100,
  receive_limit: 1,
  valid_days: 30
})

const getList = async () => {
  loading.value = true
  try {
    const res = await request.get('/coupon/list')
    if (res.code === 0) {
      tableData.value = res.data
    }
  } catch (error) {
    ElMessage.error('获取列表失败')
  } finally {
    loading.value = false
  }
}

const handleAdd = () => {
  dialogVisible.value = true
}

const handleSubmit = async () => {
  try {
    const now = new Date()
    const endDate = new Date(now.getTime() + form.value.valid_days * 24 * 60 * 60 * 1000)

    // 格式化为 MySQL 兼容的时间格式 YYYY-MM-DD HH:mm:ss
    const formatDateTime = (date: Date) => {
      const year = date.getFullYear()
      const month = String(date.getMonth() + 1).padStart(2, '0')
      const day = String(date.getDate()).padStart(2, '0')
      const hours = String(date.getHours()).padStart(2, '0')
      const minutes = String(date.getMinutes()).padStart(2, '0')
      const seconds = String(date.getSeconds()).padStart(2, '0')
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
    }

    const res = await request.post('/coupon/create', {
      ...form.value,
      start_time: formatDateTime(now),
      end_time: formatDateTime(endDate)
    })

    if (res.code === 0) {
      ElMessage.success('创建成功')
      dialogVisible.value = false
      getList()
    }
  } catch (error) {
    ElMessage.error('创建失败')
  }
}

const handleDelete = async (row: any) => {
  try {
    await ElMessageBox.confirm('确定要删除这个优惠券吗？', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })

    const res = await request.post('/coupon/delete', { id: row.id })
    if (res.code === 0) {
      ElMessage.success('删除成功')
      getList()
    } else {
      ElMessage.error(res.msg || '删除失败')
    }
  } catch (error) {
    if (error !== 'cancel') {
      ElMessage.error('删除失败')
    }
  }
}

onMounted(() => {
  getList()
})
</script>
