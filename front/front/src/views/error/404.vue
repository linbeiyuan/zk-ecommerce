<script setup lang="ts" name="NotFound">
import { useRouter } from 'vue-router';
const router = useRouter();

</script>

<template>
    <div class="error-container layout-padding" >
        <img class="error-img" src="@/assets/404.svg"/>
        <div  class="error-wrap">
            <div class="error-title">您所访问的页面不存在！</div>
            <div class="error-msg">请检查您输入的网址是否正确，或点击下面的按钮返回首页。</div>
            <el-button @click="router.push('/')" round type="primary">返回首页</el-button>
        </div>
    </div>
</template>

