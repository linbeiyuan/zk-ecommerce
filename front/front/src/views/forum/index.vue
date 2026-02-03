<script setup lang="ts">
  import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify,confirm} from '@/utils/element';
  import { isAuth } from '@/utils/utils';
  import * as XLSX from "xlsx";

  const state=reactive({
    query:{
      title:'',

    },
    page:{
      current:1,
      size:10,
      total:0
    },
    tableList:[],
    ids:[],
    isdel:true,
    showFlag:true

  })
  const { query,tableList,page,isdel,showFlag} = {...toRefs(state)};

  //进入执行
  getDateList();
  //获取列表
  function getDateList(){
    const params={
      page: state.page.current,
      limit: state.page.size,
    }


    if (state.query.title != '' && state.query.title != undefined) {
      params['title'] = '%' + state.query.title + '%'
    }
    request({
      url:'forum/flist?isdone=开放&sort=addtime&order=desc',
      method:'get',
      params
    }).then(({data})=>{

      state.page.total=data.total;
      state.tableList=data.list;
    })
  }










</script>

<template>



  <!-- 主要内容区 -->
  <main class="max-w-7xl mx-auto px-4 pt-24 pb-16">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-lg font-semibold">最新帖子</h2>
    </div>

    <!-- 帖子列表 -->
    <div class="bg-white rounded-xl shadow-sm">
      <div v-for="(post, index) in tableList" :key="post.id"
           class="p-4 cursor-pointer hover:bg-gray-50 transition-colors"
           :class="{'border-b border-gray-100': index !== post.length - 1}"
      >
        <router-link :to="`/forumdetail/`+post.id" class="shadow">
          <div class="flex justify-between items-start">
            <h3 class="text-lg font-medium text-gray-900 hover:text-blue-600">{{ post.title }}</h3>
            <span class="text-sm text-gray-500 whitespace-nowrap ml-4">{{ post.addtime }}</span>
          </div>
        </router-link>
      </div>
    </div>
    <m-page :page="page" style="text-align: center;" @pageChange="getDateList"/>
  </main>



</template>


