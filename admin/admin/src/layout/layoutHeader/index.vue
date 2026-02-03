<script setup lang="ts" name="LayoutHeader">
   import {defineAsyncComponent} from 'vue';
   const Breadcrumb=defineAsyncComponent(()=>import('@/layout/layoutHeader/breadcrumb.vue'))
   const UserDropdown=defineAsyncComponent(()=>import('@/layout/layoutHeader/userDropdown.vue'))

 const props= defineProps<{
    id:number,
    img:string,
    uname:string
  }>();


</script>

<template>
    
  <el-header class="layout-header">
    <!--右侧头部区域-->
      <div class="layout-header-index">
        <!--面包屑-->
     <Breadcrumb/>
     <!--右侧下拉菜单-->
     <UserDropdown :img="props.img" :uname="props.uname" :id="props.id"/>
    </div>
    </el-header>
</template>

<style scoped>

</style>