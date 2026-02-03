<script setup lang="ts" name="Layout">
import { Key } from '@/stores/auth';
import { Session } from '@/utils/storage';
import request from "@/utils/request";
import {GetUsersToken} from '@/api/auth'
   import { defineAsyncComponent,provide,reactive, toRefs,onMounted ,nextTick } from 'vue';
   const LayoutAside=defineAsyncComponent(()=>import('./layoutAside/index.vue'));
   const LayoutHeader=defineAsyncComponent(()=>import('./layoutHeader/index.vue'));
   const LayoutMain=defineAsyncComponent(()=>import('./layoutMain/index.vue'));
import { useSocketStore } from '../stores/socketStore';
const socketStore = useSocketStore();
   const state=reactive({
      users:{
        type:0,
        img:'',
        uname:'',
        id:0
      }
   })

   const {users} ={...toRefs(state)};


   onMounted(()=>{
   })


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

</script>

<template>

      <el-container class="layout-container">

        <LayoutAside :type="users.type"></LayoutAside>


      <el-container direction="vertical">
          <LayoutHeader :id="users.id" :img="users.img" :uname="users.uname"></LayoutHeader>
          <LayoutMain></LayoutMain>
      </el-container>
    </el-container>

</template>

<style>

</style>
