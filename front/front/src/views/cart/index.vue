<script setup lang='ts'>
  import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify} from '@/utils/element';
  import { isAuth } from '@/utils/utils'
  import { ElLoading } from 'element-plus'
  const AddEdit=defineAsyncComponent(()=>import('@/views/cart/add-edit.vue'));
  const state=reactive({

    dataList: [],
    searchForm:{
      biaoti:'',

    },
        page:{
      current:1,
      size:10,
      total:0
    },
    showFlag:true,
  })

  const ragRef=ref();
  const ragRefInstance=ref();
  const {dataList,searchForm,page,showFlag
      } = {...toRefs(state)};

  getDataList()

    
    
  function download(file) {
    window.open(`${file}`)
  }
    
    function getDataList(){

      ragRefInstance.value = ElLoading.service({
        target: ragRef.value,
        body: true,
        text: 'Loading...',
      })
      const params={
        page: state.page.current,
        limit: state.page.size,
      }


                                                                                                                                                  

      request({
        url:'cart/list',
        method:'get',
        params
      }).then((data)=>{
        ragRefInstance.value.close()
        state.page.total=data.data.total;
        state.dataList=data.data.list;

      })
    }
      function handleQuery(){
    getDataList()
  }

  const editRef=ref();

  function add(){
    editRef.value.open('新增','add');
  }
  function handleEdit(row:any){
    editRef.value.open('修改','up',row);
  }
  function handleDelete(row:any){

    request({
      url:`cart/delete`,
      method:'post',
      data:[row.id]
    }).then(({data})=>{
      notify("删除成功",{type:'success'});
      getDataList();

    })
  }

</script>

<template>
  <div class="list-page">
    <div class="list-container">
      <!-- 页面标题 -->
      <h2 class="list-page-title">购物车</h2>

      <!-- 搜索栏 -->
      <div class="list-search">


        <button class="list-search-btn" @click="handleQuery()">搜索</button>
      </div>

      <!-- 列表内容 -->
      <div class="list-grid">
        <router-link
          v-for="(item, index) in dataList"
          :key="index"
          :to="`/cartdetail/${item.id}`"
          class="list-card"
        >
        </router-link>
      </div>

      <!-- 分页 -->
      <div class="list-pagination">
        <m-page :page="page" @pageChange="getDataList"/>
      </div>
    </div>
  </div>
</template>
