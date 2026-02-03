

<template>
  <div class="detail-page">
    <div class="detail-container">
      <!-- 产品信息区 -->
      <div class="detail-content">
        <!-- 左侧图片 -->
                                                                                    <div class="detail-image-box">
              <img :src="detail.shangpintupian" :alt="detail.shangpintupian" class="detail-image" @click="handleImagePreview">
            </div>
                                                                        
        <!-- 右侧信息 -->
        <div class="detail-info-box">
                                                                  
              <h1 class="detail-title">{{ detail.shangpinmingcheng }}</h1>
                                                                                                                        <!-- 产品属性 -->
          <div class="detail-attrs">
                                                                              
                <div class="detail-attr-item">
                  <span class="detail-attr-label">商品名称：</span>
                  <span class="detail-attr-value">{{detail.shangpinmingcheng}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">商品简介：</span>
                  <span class="detail-attr-value">{{detail.shangpinjianjie}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">积分：</span>
                  <span class="detail-attr-value">{{detail.jifen}}</span>
                </div>
                                    </div>

          <!-- 操作按钮 -->
          <div class="detail-actions">

            
                                                                                                                                                                                                  
            
            



            
            
            




                        



            
                                        
                <button @click="addIntegralTap()" class="detail-btn detail-btn-small detail-btn-cart">
                  <i class="fas fa-shopping-cart"></i>
                  <span>兑换</span>
                </button>
              

            

          </div>
        </div>
      </div>

      <!-- 详情描述区 -->
      <div class="detail-description">
        <h2 class="detail-section-title">详情</h2>



                  
                  
                  
                  
                  
                  
            <div class="detail-description-content" v-html="detail.shangpinxiangqing"></div>
          
                  
        
                                                                                                                                      

      </div>
          </div>
    <!-- 图片预览弹窗 -->
    <div v-if="showPreview" class="detail-preview" @click="closePreview">
      <img :src="detail.tupian" :alt="detail.chanpinmingcheng" class="detail-preview-img">
    </div>
  </div>






  <el-dialog title="收货地址" v-model="dialogFormVisible">
    <el-form :model="form">
      <el-form-item label="收货地址" :label-width="formLabelWidth">
        <el-select v-model="form.address" clearable placeholder="请选择" style="width: 600px;">
          <el-option
                  v-for="item in addressList"
                  :key="item.id"
                  :label="(item.address+','+item.name+','+item.phone)"
                  :value="(item.address+','+item.name+','+item.phone)">
          </el-option>
        </el-select>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="dialogFormVisible = false">取 消</el-button>
      <el-button type="primary" @click="jforders()" :loading="loading" :class="{disabled: loading}">确 定</el-button>
    </div>
  </el-dialog>




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
    url: `jifenshangdian/info/${id}`,
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
          dialogFormVisible:false,
      addressList:[],
      form:{
        address:''
      },
                detailTable:'jifenshangdian',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false,
  })


  const {detail,user,pinglunDate,detailFlag,
          dialogFormVisible,
      addressList,
      form,
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
      url: `jifenshangdian/info/${id}`,
      method: "get"
    }).then((data) => {
      if (data && data.code === 0) {
        state.detail=data.data;
      } else {
        notify(data.msg,{type:'error'});
      }
    });
  }



    

    
        function addIntegralTap() {
      if(state.user.jf<state.detail.jifen){
        notify('积分不足',{type:'error'});
        return
      }

      getaddress();
      state.dialogFormVisible=true;

    }


    function getaddress(){
      request({
        url:"address/list",
        method:'get',
        data:{
          userid:state.user.id
        }
      }).then((
              data
      ) => {
        if (data && data.code === 0) {
          state.addressList = data.data.list;


        } else {
          notify(data.msg,{type:'error'});
        }
      })
    }

    function jforders(){





      if(state.form.address==''){
        notify('请选择地址',{type:'error'});
        return
      }
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

      if(state.user.jf<state.detail.jifen){
        notify('积分不足',{type:'error'});
        return
      }

      state.user.jf=state.user.jf-state.detail.jifen;
      request({
        url:`${sessionTable}/update`,
        method:'post',
        data: state.user
      }).then((data)=>{

        let order = {
          orderid: genTradeNo(),
          tablename: state.detailTable,
          userid: state.user.id,
          goodid: state.detail.id,

                                                                                goodname: state.detail.shangpinmingcheng,
                                                                                                                                                                                                                    picture: state.detail.shangpintupian,
                                                                                                  buynumber: 1,
          discountprice: 0,
          price: state.detail.jifen,
          total: state.detail.jifen,
          discounttotal: state.detail.jifen,
          type: 2,
          address: state.form.address,
          status: '已支付'
        }


        request({
          url:`orders/add`,
          method:'post',
          data:order
        }).then(({data})=>{
          notify('兑换成功',{type:'success'});
        })



      })

      state.dialogFormVisible=false;

    }


    function  genTradeNo() {
      var date = new Date();
      var tradeNo = date.getFullYear().toString() + (date.getMonth() + 1).toString() +
              date.getDate().toString() + date.getHours().toString() + date.getMinutes().toString() +
              date.getSeconds().toString() + date.getMilliseconds().toString();
      for (var i = 0; i < 5; i++) //5位随机数，用以加在时间戳后面。
      {
        tradeNo += Math.floor(Math.random() * 10);
      }
      return tradeNo;
    }


    

    
    


    
    
    

</script>