<script setup lang="ts" name="LayoutMain">

</script>

<template>
  
  <el-main class="layout-main">
      <!--主区域-->
    <el-scrollbar>
      <div class="layout-main-warp">
    <router-view>
      
    </router-view>
  </div>
  </el-scrollbar>

  </el-main>
</template>

<style scoped>
:deep(.el-scrollbar__view) {
    /*铺满高度*/ 
     height:100%
   }
</style>