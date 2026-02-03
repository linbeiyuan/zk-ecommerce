

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
                  <span class="detail-attr-label">分类名称：</span>
                  <span class="detail-attr-value">{{detail.fenleimingcheng}}</span>
                </div>
                                        
                <div class="detail-attr-item">
                  <span class="detail-attr-label">介绍：</span>
                  <span class="detail-attr-value">{{detail.jieshao}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">店铺名称：</span>
                  <span class="detail-attr-value">{{detail.dianpumingcheng}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">价格：</span>
                  <span class="detail-attr-value">{{detail.price}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">库存：</span>
                  <span class="detail-attr-value">{{detail.alllimittimes}}</span>
                </div>
                                                                                                                                            </div>

          <!-- 操作按钮 -->
          <div class="detail-actions">

            
              <button v-if="!storeupFlag" @click="storeUp(1)" class="detail-btn detail-btn-small detail-btn-collect">
                <i class="fas fa-bookmark"></i>
                <span>收藏</span>
              </button>
              <button v-if="storeupFlag" @click="storeUp(1)" class="detail-btn detail-btn-small detail-btn-collected">
                <i class="fas fa-flag"></i>
                <span>已收藏</span>
              </button>
            
                                                                                                                                                                                                                                                                                                                                                                                                                                            
            
            



            
            
            




                        



                          <button
                      @click="onThumb('thumbsupnum')"
                      :disabled="thumbsUpLoading"
                      :class="{'opacity-50 cursor-not-allowed': thumbsUpLoading, 'thumb-animate': thumbsUpAnimate}"
                      class="flex items-center gap-2 rounded-lg bg-green-500 px-4 py-2 text-white hover:bg-green-600 transition-all duration-300 transform hover:scale-105 !rounded-button whitespace-nowrap">
                <i class="fas fa-thumbs-up" :class="{'animate-bounce': thumbsUpAnimate}"></i>
                <span>赞 ({{ detail.thumbsupnum || 0 }})</span>
              </button>
              <button
                      @click="onThumb('crazilynum')"
                      :disabled="thumbsDownLoading"
                      :class="{'opacity-50 cursor-not-allowed': thumbsDownLoading, 'thumb-animate': thumbsDownAnimate}"
                      class="flex items-center gap-2 rounded-lg bg-gray-500 px-4 py-2 text-white hover:bg-gray-600 transition-all duration-300 transform hover:scale-105 !rounded-button whitespace-nowrap">
                <i class="fas fa-thumbs-down" :class="{'animate-bounce': thumbsDownAnimate}"></i>
                <span>踩 ({{ detail.crazilynum || 0 }})</span>
              </button>
            
                          

                <button @click="addCartTap()" class="detail-btn detail-btn-small detail-btn-cart">
                  <i class="fas fa-shopping-cart"></i>
                  <span>加入购物车</span>
                </button>


                            

            

          </div>
        </div>
      </div>

      <!-- 详情描述区 -->
      <div class="detail-description">
        <h2 class="detail-section-title">详情</h2>



                  
                  
                  
                  
                  
                  
                  
            <div class="detail-description-content" v-html="detail.xiangqing"></div>
          
                  
                  
                  
                  
                  
                  
                  
                  
                  
        
                                                                                                                                                                                                                                                                                                        

      </div>
              <!-- 评论区 -->
        <div class="detail-comments">
          <h2 class="detail-section-title">用户评论</h2>

          <!-- 评论输入框 -->
          <div class="comment-form">
            <div class="comment-avatar">
              <i class="fas fa-user"></i>
            </div>
            <div class="comment-input-box">
            <textarea
                    v-model="formData.content"
                    class="comment-textarea"
                    placeholder="写下你的评论..."
            ></textarea>
              <button @click="addpl()" class="comment-submit-btn">
                <i class="fas fa-paper-plane"></i>
                <span>发表评论</span>
              </button>
            </div>
          </div>

          <!-- 评论列表 -->
          <div class="comment-list">
            <div v-for="item in pinglunDate" :key="item.id" class="comment-item">
              <div class="comment-avatar">
                <i class="fas fa-user"></i>
              </div>
              <div class="comment-content">
                <div class="comment-header">
                  <span class="comment-author">{{ item.nickname }}</span>
                </div>
                <p class="comment-text">{{ item.content }}</p>
                <div v-if="item.reply" class="comment-reply">
                  <div class="reply-avatar">
                    <i class="fas fa-user"></i>
                  </div>
                  <div class="reply-content">
                    <span class="reply-author">管理员</span>
                    <p class="reply-text">{{ item.reply }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
    url: `shangpinguanli/info/${id}`,
    method: "get"
  }).then((data) => {
    if (data && data.code === 0) {
      state.detail=data.data;
              isStoreup(id);
            
        getpllist()

          } else {
      notify(data.msg,{type:'error'});
    }
  });

      const state=reactive({
        detail:{},
    user:{},
    pinglunDate:[],
              storeupFlag:0,
      storeupList:[],
              thumbsUpLoading: false,
      thumbsDownLoading: false,
      thumbsUpAnimate: false,
      thumbsDownAnimate: false,
        detailTable:'shangpinguanli',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false,
  })


  const {detail,user,pinglunDate,detailFlag,
              storeupFlag,
      storeupList,
                  thumbsUpLoading,
      thumbsDownLoading,
      thumbsUpAnimate,
      thumbsDownAnimate,
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
          isStoreup(id);
      }
  function info(id) {
    request({
      url: `shangpinguanli/info/${id}`,
      method: "get"
    }).then((data) => {
      if (data && data.code === 0) {
        state.detail=data.data;
      } else {
        notify(data.msg,{type:'error'});
      }
    });
  }



    

    
    function getpllist() {
      request({
        url: `discussshangpinguanli/list`,
        method: "get",
        params: {
          refid: state.detail.id,
        }
      }).then((data) => {
        if (data && data.code === 0) {
          state.pinglunDate=data.data.list;
        } else {
          notify(data.msg,{type:'error'});
        }
      });
    }





    function addpl(){
      state.formData.nickname=Session.get("adminName")
      state.formData.userid=state.user.id
      state.formData.refid=state.detail.id

      request({
        url: `discussshangpinguanli/save`,
        method: "post",
        data:state.formData
      }).then((data) => {
        if (data && data.code === 0) {
          notify("评论成功",{type:'success'});

          getpllist();
        } else {
          notify(data.msg,{type:'error'});
        }
      });
    }

    
    

    




    function addCartTap() {
      if (state.detail.alllimittimes==0)
      {

        notify('商品已售罄',{type:'error'});

        return
      }
      // 库存限制
      if (state.detail.alllimittimes && state.detail.alllimittimes > 0 && state.detail.alllimittimes < state.buynumber) {
        notify('商品已售罄',{type:'error'});
        return
      }
      // 查询是否已经添加到购物车

      request({
        url: `cart/list`,
        method: "get",
        params:{
          userid:state.user.id,
          tablename: `${state.detailTable}`,
          goodid: state.detail.id
        }
      }).then((data) => {
        if (data.data.list.length > 0) {
          notify('该商品已经添加到购物车',{type:'error'});
          return
        } else {



          request({
            url:"cart/save",
            method:"post",
            data:{
              tablename: `${state.detailTable}`,
              goodid: state.detail.id,
                                                                                                            goodname: state.detail.shangpinmingcheng,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              picture: state.detail.shangpintupian,
                                                                                                                                                                                                                                                                                                                                                                                                                    buynumber: 1,
              userid: state.user.id,
              price: state.detail.price,
              discountprice:0
            }
          }).then((data) => {
            if (data && data.code === 0) {

              notify("添加到购物车成功",{type:'success'});
            } else {
              notify(data.msg,{type:'error'});

            }
          });


        }
      });
    }


    
        function isStoreup(id){
      request({
        url:'storeup/list',
        method:'get',
        params:{
          page: 1,
          limit: 1,
          type: 1,
          refid: state.detail.id,
          tablename: state.detailTable,
          userid: state.user.id
        }
      }).then((data)=>{
        state.storeupList=data.data.list;
        if (data.data.list.length == 1) {
          state.storeupFlag=1;
        }else{
          state.storeupFlag=0;
        }


      })
    }


    function storeUp(type){
      request({
        url:'storeup/list',
        method:'get',
        params:{
          page: 1,
          limit: 1,
          type: 1,
          refid: state.detail.id,
          tablename: state.detailTable,
          userid: state.user.id
        }
      }).then((data)=>{
        state.storeupList=data.data.list;

        if (data.data.list.length == 1) {

          request({
            url:'storeup/delete',
            method:'post',
            data:[data.data.list[0].id]

          }).then((data)=>{
            notify("取消成功",{type:'warning'});

            state.storeupFlag=0;

          })
        }else{
          request({
            url:'storeup/save',
            method:'post',
            data:{
              refid: state.detail.id,
              tablename: state.detailTable,
                                                                                                            name: state.detail.shangpinmingcheng,
                                                                                                                                                                                                                                                                                                                                                                                                                                                  userid:state.user.id,
                                                                                                                                          picture: state.detail.shangpintupian,
                                                                                                                                                                                                                                                                                                                                                                                                                  }

          }).then((data)=>{
            notify("收藏成功",{type:'warning'});

            state.storeupFlag=1;

          })
        }
      })
    }

    


    
    
        // 点赞和踩的处理函数
    const onThumb = (type) => {
      // 防止重复点击
      if (type === 'thumbsupnum' && state.thumbsUpLoading) return;
      if (type === 'crazilynum' && state.thumbsDownLoading) return;

      // 设置加载状态
      if (type === 'thumbsupnum') {
        state.thumbsUpLoading = true;
        state.thumbsUpAnimate = true;
      } else {
        state.thumbsDownLoading = true;
        state.thumbsDownAnimate = true;
      }

      // 增加计数
      state.detail[type] = (state.detail[type] || 0) + 1;

      // 发送请求
      request({
        url: `shangpinguanli/update`,
        method: 'post',
        data: state.detail
      }).then((res) => {
        if (res && res.code === 0) {
          notify('操作成功', { type: 'success' });
          // 重新获取数据以确保准确性
          info(id);
        } else {
          // 失败时回滚计数
          state.detail[type] = (state.detail[type] || 1) - 1;
          notify(res.msg || '操作失败', { type: 'error' });
        }
      }).catch((error) => {
        // 错误时回滚计数
        state.detail[type] = (state.detail[type] || 1) - 1;
        notify('网络错误，请稍后重试', { type: 'error' });
      }).finally(() => {
        // 清除加载状态
        if (type === 'thumbsupnum') {
          state.thumbsUpLoading = false;
          // 300ms后清除动画
          setTimeout(() => {
            state.thumbsUpAnimate = false;
          }, 300);
        } else {
          state.thumbsDownLoading = false;
          // 300ms后清除动画
          setTimeout(() => {
            state.thumbsDownAnimate = false;
          }, 300);
        }
      });
    };
    

</script>