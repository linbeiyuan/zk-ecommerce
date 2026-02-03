

<template>
  <div class="detail-page">
    <div class="detail-container">
      <!-- 产品信息区 -->
      <div class="detail-content">
        <!-- 左侧图片 -->
                                                                                                                    
        <!-- 右侧信息 -->
        <div class="detail-info-box">
                                                                                                                                                        <!-- 产品属性 -->
          <div class="detail-attrs">
                                                                                                                                                                                  </div>

          <!-- 操作按钮 -->
          <div class="detail-actions">

            
                                                                                                                                                                        
            
            



            
            
            




                        



            
            

          </div>
        </div>
      </div>

      <!-- 详情描述区 -->
      <div class="detail-description">
        <h2 class="detail-section-title">详情</h2>



                  
                  
                  
                  
                  
                  
        
                                                                                                                    

      </div>
          </div>
    <!-- 图片预览弹窗 -->
    <div v-if="showPreview" class="detail-preview" @click="closePreview">
      <img :src="detail.tupian" :alt="detail.chanpinmingcheng" class="detail-preview-img">
    </div>
  </div>










</template>
<script setup>



  import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify,confirm} from '@/utils/element';
  import { isAuth } from '@/utils/utils'
  import { ElLoading } from 'element-plus'
      const showPreview = ref(false);
  const handleImagePreview = () => {
    showPreview.value = true;
  };
  const closePreview = () => {
    showPreview.value = false;
  };

  import { useRoute } from 'vue-router'

    


    
  const route = useRoute()

        
    
    
  // 打印
  const id=route.params.id
  request({
    url: `crk/info/${id}`,
    method: "get"
  }).then((data) => {
    if (data && data.code === 0) {
      state.detail=data.data;
                } else {
      notify(data.msg,{type:'error'});
    }
  });

      const state=reactive({
        detail:{},
    user:{},
    pinglunDate:[],
                detailTable:'crk',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false,
  })


  const {detail,user,pinglunDate,detailFlag,
                    detailTable,
    formData,
  } = {...toRefs(state)};

        

    






  let sessionTable = Session.get("tableName")
  request({
    url: sessionTable + '/session',
    method: "get"
  }).then((
          data
  ) => {
    if (data && data.code === 0) {
      state.user = data.data;
    } else {
      notify(data.msg,{type:'error'});


    }
  });




  function download(file) {
    window.open(`${file}`)
  }


  function init(id){
    state.detailFlag=true;
    info(id);
      }
  function info(id) {
    request({
      url: `crk/info/${id}`,
      method: "get"
    }).then((data) => {
      if (data && data.code === 0) {
        state.detail=data.data;
      } else {
        notify(data.msg,{type:'error'});
      }
    });
  }



    

    
    

    
    


    
    
    

</script>