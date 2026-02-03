
<!-- 代码已包含 CSS：使用 TailwindCSS , 安装 TailwindCSS 后方可看到布局样式效果 -->
<template>
  <div class="min-h-screen bg-gray-50">
    <div class="max-w-[1200px] mx-auto px-4 py-8">
      <!-- 文章主体 -->
      <div class="bg-white rounded-lg shadow-sm p-8">
        <!-- 标题区域 -->
        <h1 class="text-2xl font-bold text-gray-900">{{ detail.title }}</h1>
        <!-- 文章元信息 -->
        <div class="flex items-center mt-4 text-gray-600 text-sm space-x-6">
          <div class="flex items-center">
            <span>{{ detail.username }}</span>
          </div>
          <div class="flex items-center">
            <i class="fas fa-clock mr-1"></i>
            <span>{{ detail.addtime }}</span>
          </div>
        </div>
        <!-- 文章内容 -->
        <div class="mt-8 text-gray-800 leading-relaxed">
          <div v-html="detail.content"></div>
          <!-- <img :src="article.contentImage" class="w-full rounded-lg my-6 object-cover" /> -->
        </div>
      </div>
      <!-- 评论区 -->
      <div class="mt-8">
        <h2 class="text-xl font-bold text-gray-900 mb-4">评论</h2>
        <!-- 评论输入框 -->
        <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
    <textarea
        placeholder="写下你的评论..."  v-model="formData.content"
        class="w-full p-4 border border-gray-200 rounded-lg focus:outline-none focus:border-blue-500 min-h-[100px] text-gray-700"
    ></textarea>
          <div class="flex justify-end mt-4">
            <button @click="addpl()" class="px-6 py-2 bg-blue-500 text-white !rounded-button whitespace-nowrap hover:bg-blue-600">
              发表评论
            </button>
          </div>
        </div>
        <!-- 评论列表 -->
        <div class="space-y-6">
          <div v-for="item in pinglunDate " :key="item" class="bg-white rounded-lg shadow-sm p-6">
            <div class="flex items-center mb-4">
              <div class="flex flex-col">
                <div class="font-medium text-gray-900">{{ item.username }}</div>
                <div class="text-sm text-gray-500">{{ item.addtime }}</div>
              </div>
            </div>
            <p class="text-gray-700">{{ item.content }}</p>
            <!-- 回复功能 -->
            <!-- 回复列表 -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>

  import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify,confirm} from '@/utils/element';
  import { isAuth } from '@/utils/utils'
  import { ElLoading } from 'element-plus'
  import { useRoute } from 'vue-router'

  const route = useRoute()

  // 打印
  const id=route.params.id

  const state=reactive({
    detail:{},
    user:{},
    pinglunDate:[],
    detailTable:'${tableName}',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false
  })

  const {detail,user,pinglunDate,detailTable,formData,detailFlag} = {...toRefs(state)};


  const emit = defineEmits(['refresh']);





  let sessionTable = Session.get("tableName")
  request({
    url: sessionTable + '/session',
    method: "get"
  }).then((data) => {
    if (data && data.code === 0) {
      state.user = data.data;
    } else {
      notify(data.msg,{type:'error'});
    }
  });




  init();



  function init(){


    request({
      url: `forum/list/${id}`,
      method: "get"
    }).then((data) => {
      if (data && data.code === 0) {
        state.detail=data.data;
        state.pinglunDate=data.data.childs;
      } else {
        notify(data.msg,{type:'error'});
      }
    });
  }
  function addpl(){

    request({
      url:'forum/add',
      method:'post',
      data:{
        username: Session.get("adminName"),
        userid:state.user.id,
        parentid:state.detail.id,
        content:state.formData.content
      }
    }).then((data)=>{
      if (data && data.code === 0) {
        notify("评论成功",{type:"success"})

        init();
      } else {

      }
    })

  }






</script>
<style scoped>

</style>


