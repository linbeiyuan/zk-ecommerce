<script setup lang='ts'>
  import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify} from '@/utils/element';
  import { isAuth } from '@/utils/utils'
  import { ElLoading } from 'element-plus'
  const AddEdit=defineAsyncComponent(()=>import('@/views/dianpuxinxi/add-edit.vue'));
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


                                                    if (state.searchForm.dianpumingcheng != '' && state.searchForm.dianpumingcheng != undefined) {
            params['dianpumingcheng'] = '%' + state.searchForm.dianpumingcheng + '%'
          }
                                              if (state.searchForm.nicheng != '' && state.searchForm.nicheng != undefined) {
            params['nicheng'] = '%' + state.searchForm.nicheng + '%'
          }
                                                                                                                                            

      request({
        url:'dianpuxinxi/list',
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
      url:`dianpuxinxi/delete`,
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
      <h2 class="list-page-title">店铺信息</h2>

      <!-- 搜索栏 -->
      <div class="list-search">

        <div class="list-search-input">
          <i class="fas fa-search"></i>
          <input type="text" placeholder="店铺名称" v-model="searchForm.dianpumingcheng">
        </div>
        <div class="list-search-input">
          <i class="fas fa-search"></i>
          <input type="text" placeholder="昵称" v-model="searchForm.nicheng">
        </div>

        <button class="list-search-btn" @click="handleQuery()">搜索</button>
      </div>

      <!-- 列表内容 -->
      <div class="list-grid">
        <router-link
          v-for="(item, index) in dataList"
          :key="index"
          :to="`/dianpuxinxidetail/${item.id}`"
          class="list-card"
        >
          <div class="list-card-img">
            <img :src="item.tupian" :alt="item.tupian">
          </div>
          <div class="list-card-info">
            <h3 class="list-card-title">{{ item.dianpumingcheng }}</h3>
          </div>
          <div class="list-card-info">
            <h3 class="list-card-title">{{ item.nicheng }}</h3>
          </div>
        </router-link>
      </div>

      <!-- 分页 -->
      <div class="list-pagination">
        <m-page :page="page" @pageChange="getDataList"/>
      </div>
    </div>
  </div>
</template>
