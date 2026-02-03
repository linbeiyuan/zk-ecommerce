<script setup lang="ts" name="LayoutAside">
   import {defineAsyncComponent} from 'vue';
   import {useLayoutConfigStore} from '@/stores/layoutConfig'
   import { storeToRefs } from 'pinia';
   const layoutConfig=useLayoutConfigStore();
   const {isCollapse}=storeToRefs(layoutConfig)
   const Logo=defineAsyncComponent(()=>import('@/layout/layoutAside/logo.vue'));
   const VerticalMenu=defineAsyncComponent(()=>import('@/layout/layoutAside/verticalMenu.vue'));

  const props= defineProps<{
       type:number
   }>();


</script>

<template>

  
 <div class="h100">
      <!--左侧菜单栏-->
            <el-aside 
            
            class="layout-aside"
            :class="isCollapse ? 'layout-aside-menu-60' :'layout-aside-menu-200'"
            >
                <Logo></Logo>
                <VerticalMenu :type="props.type"></VerticalMenu>
            </el-aside>
        </div>
</template>

<style scoped>

</style>