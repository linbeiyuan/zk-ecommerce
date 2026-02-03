<template>
  <div class="add-edit-container">
    <el-form :model="form" label-width="120px">
      <el-form-item label="标题">
        <el-input v-model="form.title" placeholder="请输入标题" />
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="form.username" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item label="开始日期">
        <el-date-picker v-model="form.funddate" type="date" placeholder="选择日期" />
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker v-model="form.enddate" type="date" placeholder="选择日期" />
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';

const form = reactive({
  title: '',
  username: '',
  funddate: '',
  enddate: ''
});
</script>

<style scoped>
.add-edit-container {
  padding: 20px;
}
</style>
