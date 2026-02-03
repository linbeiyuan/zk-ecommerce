<script setup lang='ts'>
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify} from '@/utils/element';
    import { isAuth } from '@/utils/utils'
    import { ElLoading } from 'element-plus'



    const state=reactive({

        dataList: [],
        searchForm:{
            title:'',

        },

        page:{
            current:1,
            size:10,
            total:0
        },
        showFlag:true
    })

    const ragRef=ref();
    const ragRefInstance=ref();
    const {dataList,searchForm,page,showFlag} = {...toRefs(state)};

    getDataList()







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



                if (state.searchForm.title != '' && state.searchForm.title != undefined) {
                    params['title'] = '%' + state.searchForm.title + '%'
                }



        request({
            url:'news/list',
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


</script>

<template ref="ragRefInstance">



  <div class="py-20 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4">
      <h2 class="text-3xl font-bold text-center mb-4">系统公告</h2>
      <p class="text-gray-600 text-center mb-12">了解最新的资讯和独家XXX</p>
      <div class="grid grid-cols-2 gap-8">



        <div class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300"  v-for="(item, index) in dataList" :key="index">
          <div class="flex">
            <div class="w-1/3">
              <img :src="item.picture" alt="" class="w-full h-full object-cover">
            </div>
            <div class="w-2/3 p-6">
              <div class="flex items-center mb-3">
                <span class="ml-3 text-gray-500 text-sm">{{item.addtime}}</span>
              </div>
              <h3 class="text-xl font-bold mb-3">{{item.title}}</h3>
              <p class="text-gray-600 line-clamp-2">{{item.introduction}}</p>
              <router-link :to="`/newsdetail/`+item.id">
                <button class="mt-4 text-blue-600 hover:text-blue-700 flex items-center text-sm">
                  阅读更多 <i class="fas fa-arrow-right ml-2"></i>
                </button>
              </router-link>
            </div>
          </div>
        </div>




      </div>
      <m-page :page="page" style="text-align: center;" @pageChange="getDataList"/>
    </div>
  </div>



</template>


