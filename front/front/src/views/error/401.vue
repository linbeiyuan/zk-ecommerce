<script setup lang="ts" name="NoPermission">
import { useRouter } from 'vue-router';
const router = useRouter();

</script>

<template>
    <div class="error-container layout-padding flex-center">
        <img class="error-img" src="@/assets/401.svg"/>
        <div  class="error-wrap">
            <div  class="error-title">您没有操作权限，请联系管理员！</div>
            <div  class="error-msg">联系方式：https://www.mengxuegu.com</div>
            <el-button @click="router.push('/login')" type="primary" round>重新登录</el-button>
        </div>
    </div>
</template>

