<template>
  <div class="min-h-screen bg-gray-50">
    <div class="max-w-6xl mx-auto px-4 py-8">
      <!-- 文章头部 -->
      <div class="mb-8">
        <h1 class="text-3xl font-bold mb-4">{{detail.title}}</h1>
        <div class="flex items-center text-gray-600 text-sm space-x-4">
          <span>发布时间：{{detail.addtime}}</span>
          <span>•</span>
          <span>发布人：admin</span>
        </div>
      </div>

      <!-- 主图 -->
      <div class="relative mb-8 group">
        <img
            :src="detail.picture"
            class="w-full h-[500px] object-cover object-top cursor-pointer"
            @click="showImagePreview = true"
        />
      </div>

      <!-- 文章简介 -->
      <div class="bg-gray-100 border-l-4 border-blue-500 p-6 mb-8">
        <p class="text-lg leading-relaxed">
          {{ detail.introduction }}
        </p>
      </div>

      <!-- 文章正文 -->
      <div class="prose max-w-none">

        <p class="mb-6" v-html="detail.content">
        </p>






      </div>

    </div>

    <!-- 返回顶部按钮 -->
    <button
        v-show="showBackToTop"
        @click="scrollToTop"
        class="fixed right-8 bottom-8 bg-blue-500 text-white p-3 rounded-full shadow-lg hover:bg-blue-600 transition-colors !rounded-button"
    >
      <i class="fas fa-arrow-up"></i>
    </button>

    <!-- 图片预览 -->
    <div v-if="showImagePreview" class="fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center" @click="showImagePreview = false">
      <img :src="detail.picture" class="max-w-[90%] max-h-[90vh] object-contain" />
    </div>
  </div>
</template>

<script lang="ts" setup>
  import { ref, onMounted, onUnmounted,reactive,toRefs } from 'vue';

  const showBackToTop = ref(false);
  const showImagePreview = ref(false);
  const currentPreviewImage = ref('');
  import request from "@/utils/request";
  import {notify,confirm} from '@/utils/element';
  import { useRoute } from 'vue-router'

  const route = useRoute()

  // 打印
  const id=route.params.id

  const state=reactive({
    detail:{},
    user:{},
    pinglunDate:[],
    detailTable:'news',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false
  })

  const {detail} = {...toRefs(state)};



  request({
    url: `news/info/${id}`,
    method: "get"
  }).then((data) => {
    if (data && data.code === 0) {
      state.detail=data.data;
    } else {
      notify(data.msg,{type:'error'});
    }
  });







  const handleScroll = () => {
    showBackToTop.value = window.scrollY > 300;
  };

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  onMounted(() => {
    window.addEventListener('scroll', handleScroll);
  });

  onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll);
  });
</script>





