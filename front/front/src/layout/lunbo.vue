<script setup lang="ts">
import request from "@/utils/request";
import {ref,onMounted,reactive,toRefs,nextTick} from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Pagination, Autoplay } from 'swiper/modules';
const swiperModules = [Pagination, Autoplay];
const state=reactive({
  page:{
    current:1,//当前页码
    size:20,//每页显示多少条
    total:0,//总条数
  },
  tableList:[],
  loadding:false,
  query:{name:'',type:1}
});
const {page,tableList,loadding,query} = {...toRefs(state)};
onMounted(()=>{
  getpagelist();
})
async function getpagelist(){
  try {
    state.loadding=true;
    request({
      url:'config/list',
      method:'get'
    }).then((data)=>{
      state.tableList.length=0;
      // 修复图片URL中的端口号
      state.tableList=data.data.list.map((item:any)=>({
        ...item,
        value: item.value?.replace(':8080', ':8000') || item.value
      }));
    })
    nextTick(()=>{})
  } catch (error) {

  }finally{
    state.loadding=false;
  }
}

</script>

<template>

  <div class="relative h-[600px] mt-16">
    <swiper
        :modules="swiperModules"
        :slides-per-view="1"
        :loop="true"
        :autoplay="{
  delay: 5000,
  disableOnInteraction: false
  }"
        :pagination="{ clickable: true }"
        class="h-full"
    >
      <swiper-slide v-for="(slide, index) in tableList" :key="index">
        <div class="relative h-full">
          <img :src="slide.value" :alt="slide.name" class="w-full h-full object-cover object-top">
        </div>
      </swiper-slide>
    </swiper>
  </div>


</template>

