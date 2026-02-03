<script setup lang="ts">
     import {ref,reactive,onMounted,defineAsyncComponent,toRefs,watch} from 'vue';
     import { useRoute } from 'vue-router';
     const Header=defineAsyncComponent(()=>import('@/layout/header.vue'));
     const LunBo=defineAsyncComponent(()=>import('@/layout/lunbo.vue'));
     const Footer=defineAsyncComponent(()=>import('@/layout/footer.vue'));
      import { useAuthStore,Key } from '@/stores/auth';
      import { Session, Local } from '@/utils/storage';
      import {GetUsersToken} from '@/api/auth'
     import request from "@/utils/request";
                  import { useSocketStore } from '../stores/socketStore';
         const socketStore = useSocketStore();
                    const authstore=useAuthStore();
  // console.log();


   const state=reactive({
      users:{
        type:0,
        img:'',
        uname:'',
        id:0
      }
   })

   const {users} ={...toRefs(state)};

     const route = useRoute();
     const lunboVisible = ref(true);

     const tableName = Session.get("tableName");
     const response = request({
       url: `${tableName}/session`,
       method: 'POST'
     }).then(resp => {
       localStorage.setItem('user', JSON.stringify(resp.data));
       state.users = resp.data;
                    if(socketStore.socket === undefined || socketStore.socket == null || socketStore.socket.readyState === WebSocket.CLOSE) {
             socketStore.initializeSocket(state.users.id, state.users.nicheng, state.users.role)
           }
                         Session.set(Key.userInfoKey, resp.data);
     })

     // 使用 watch 监听路由变化
     watch(
         () => route.path,
         (newPath) => {
           // 根据新路径设置 lunboVisible 的值
           if (newPath === '/sixin') {
             lunboVisible.value = false;
           } else {
             lunboVisible.value = true;
           }
         },
         { immediate: true } // ����ִ��һ�λص������ó�ʼֵ
     );

     onMounted(()=>{
     })



</script>

<template>

  <Header></Header>

  <LunBo v-if="lunboVisible"/>
  <router-view></router-view>

  <Footer></Footer>

    
</template>

