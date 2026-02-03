<script setup lang="ts" name="LayoutLogo">
   import {useLayoutConfigStore} from '@/stores/layoutConfig'
   import { storeToRefs } from 'pinia';
   const layoutConfig=useLayoutConfigStore();
   const {isCollapse,globalTitle}=storeToRefs(layoutConfig)
</script>

<template>
   <div class="layout-logo">
     <img class="layout-logo-img" src="@/assets/logo.png" alt="">
     <span v-if="!isCollapse">{{globalTitle}}</span>
   </div>
</template>

<style scoped>

</style>