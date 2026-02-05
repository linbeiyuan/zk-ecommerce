

<template>
  <div class="detail-page">
    <div class="detail-container">
      <!-- 产品信息区 -->
      <div class="detail-content">
        <!-- 左侧图片 -->
                                                                                    <div class="detail-image-box">
              <img :src="detail.tupian" :alt="detail.tupian" class="detail-image" @click="handleImagePreview">
            </div>
                                                                                                                                                                                                      
        <!-- 右侧信息 -->
        <div class="detail-info-box">
                                                                  
              <h1 class="detail-title">{{ detail.dianpumingcheng }}</h1>
                                                        
              <h1 class="detail-title">{{ detail.nicheng }}</h1>
                                                                                                                                                                                                                                      <!-- 产品属性 -->
          <div class="detail-attrs">
                                                                              
                <div class="detail-attr-item">
                  <span class="detail-attr-label">店铺名称：</span>
                  <span class="detail-attr-value">{{detail.dianpumingcheng}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">昵称：</span>
                  <span class="detail-attr-value">{{detail.nicheng}}</span>
                </div>
                                        
                <div class="detail-attr-item">
                  <span class="detail-attr-label">商家电话：</span>
                  <span class="detail-attr-value">{{detail.shangjiadianhua}}</span>
                </div>
                                        
                <div class="detail-attr-item">
                  <span class="detail-attr-label">店铺简介：</span>
                  <span class="detail-attr-value">{{detail.dianpujianjie}}</span>
                </div>
                                        
                <div class="detail-attr-item">
                  <span class="detail-attr-label">店铺地址：</span>
                  <span class="detail-attr-value">{{detail.dianpudizhi}}</span>
                </div>
                                                                  
                <div class="detail-attr-item">
                  <span class="detail-attr-label">lat：</span>
                  <span class="detail-attr-value">{{detail.lat}}</span>
                </div>
                                        
                <div class="detail-attr-item">
                  <span class="detail-attr-label">lnt：</span>
                  <span class="detail-attr-value">{{detail.lnt}}</span>
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
            
                                                                                                                                                                                                                                                                                                                                                                                        
            
            




              <button @click="contactShop" class="detail-btn detail-btn-small detail-btn-collect">
                <i class="fas fa-comment"></i>
                <span>联系</span>
              </button>

            
            




            
              <button @click="dwxz()" class="detail-btn detail-btn-small detail-btn-collect">
                <i class="fas fa-bookmark"></i>
                <span>地图标记</span>
              </button>

                        



            
            

          </div>
        </div>
      </div>

      <!-- 详情描述区 -->
      <div class="detail-description">
        <h2 class="detail-section-title">详情</h2>



                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
        
                                                                                                                                                                                                                                                                    

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








  <el-dialog :title="`定位`" v-model="visibledw"
             center draggable :before-close="closes" width="1000px"
             :close-on-click-modal="false" destroy-on-close align-center>
    <div id="container" class="mapDisplay"></div>
  </el-dialog>

  <!-- 联系对话框 - 聊天窗口 -->
  <el-dialog
    :title="`与 ${detail.nicheng || detail.dianpumingcheng} 的对话`"
    v-model="contactDialogVisible"
    width="600px"
    :close-on-click-modal="false"
  >
    <!-- 消息列表 -->
    <div class="chat-messages" ref="chatMessagesRef">
      <div
        v-for="msg in chatMessages"
        :key="msg.id"
        :class="['chat-message', msg.isSelf ? 'self' : 'other']"
      >
        <div class="message-bubble">
          <div class="message-text">{{ msg.msg }}</div>
          <div class="message-time">{{ formatChatTime(msg.sendTime) }}</div>
        </div>
      </div>
      <div v-if="chatMessages.length === 0" class="empty-chat">
        <p>暂无消息，开始聊天吧~</p>
      </div>
    </div>

    <!-- 发送消息区域 -->
    <div class="chat-input-area">
      <el-input
        v-model="contactMessage"
        type="textarea"
        :rows="3"
        placeholder="输入消息内容... (Ctrl+Enter 发送)"
        @keydown.ctrl.enter="sendContactMessage"
      ></el-input>
      <div class="chat-actions">
        <el-button @click="refreshChatMessages" size="small">
          <i class="fas fa-sync-alt"></i> 刷新
        </el-button>
        <el-button type="primary" @click="sendContactMessage" :loading="sendingMessage">
          发送
        </el-button>
      </div>
    </div>
  </el-dialog>



<Wd ref="WdRef"></Wd>


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

        const Wd=defineAsyncComponent(()=>import('@/views/wd/index.vue'));
    const WdRef=ref();
    


    
  const route = useRoute()

        
    import iconTeam from '@/assets/1.png';
    import AMapLoader from '@amap/amap-jsapi-loader';


        function wd() {
      WdRef.value.openaddOrupdate(state.detail);
    }

    // 联系商家
    function contactShop() {
      state.contactDialogVisible = true;
      state.contactMessage = '';
      state.chatMessages = [];
      loadChatMessages();
    }

    // 加载聊天消息
    async function loadChatMessages() {
      if (!state.detail.userid) return;

      try {
        const res = await request({
          url: 'letter/querySomeBodyMsg',
          method: 'get',
          params: { sender: state.detail.userid }
        });

        if (res.code === 0) {
          const user = JSON.parse(localStorage.getItem('user') || '{}');
          state.chatMessages = res.data.map(msg => ({
            ...msg,
            isSelf: msg.sender === user.id
          }));
          scrollToBottom();
        }
      } catch (error) {
        console.error('加载消息失败:', error);
      }
    }

    // 发送联系消息
    async function sendContactMessage() {
      if (!state.contactMessage.trim()) {
        notify('请输入消息内容', {type: 'warning'});
        return;
      }

      state.sendingMessage = true;
      try {
        const res = await request({
          url: 'letter/send',
          method: 'post',
          data: {
            receiver: state.detail.userid,
            receiverName: state.detail.nicheng || state.detail.dianpumingcheng,
            msg: state.contactMessage
          }
        });

        if (res.code === 0) {
          notify('发送成功', {type: 'success'});
          state.contactMessage = '';
          // 重新加载消息列表
          await loadChatMessages();
        } else {
          notify(res.msg || '发送失败', {type: 'error'});
        }
      } catch (error) {
        console.error('发送失败:', error);
        notify('发送失败', {type: 'error'});
      } finally {
        state.sendingMessage = false;
      }
    }

    // 刷新聊天消息
    function refreshChatMessages() {
      loadChatMessages();
    }

    // 滚动到底部
    function scrollToBottom() {
      setTimeout(() => {
        const chatBox = document.querySelector('.chat-messages');
        if (chatBox) {
          chatBox.scrollTop = chatBox.scrollHeight;
        }
      }, 100);
    }

    // 格式化聊天时间
    function formatChatTime(time) {
      if (!time) return '';
      const date = new Date(time);
      return `${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${String(date.getMinutes()).padStart(2, '0')}`;
    }

    
  // 打印
  const id=route.params.id
  request({
    url: `dianpuxinxi/info/${id}`,
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
          list:[],
      visibledw:false,
        detail:{},
    user:{},
    pinglunDate:[],
              storeupFlag:0,
      storeupList:[],
            detailTable:'dianpuxinxi',
    formData:{
      userid:"",
      nickname:"",
      refid:"",
      content:""
    },
    detailFlag:false,
    // 联系对话框相关
    contactDialogVisible: false,
    contactMessage: '',
    chatMessages: [],
    sendingMessage: false,
  })


  const {detail,user,pinglunDate,detailFlag,
              storeupFlag,
      storeupList,
              list,
      visibledw,
            detailTable,
    formData,
    contactDialogVisible,
    contactMessage,
    chatMessages,
    sendingMessage,
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
      url: `dianpuxinxi/info/${id}`,
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
        url: `discussdianpuxinxi/list`,
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
        url: `discussdianpuxinxi/save`,
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
                                                                                                            name: state.detail.dianpumingcheng,
                                                                                              name: state.detail.nicheng,
                                                                                                                                                                                                                                                                                                                          userid:state.user.id,
                                                                                                                                          picture: state.detail.tupian,
                                                                                                                                                                                                                                                                                                                                                      }

          }).then((data)=>{
            notify("收藏成功",{type:'warning'});

            state.storeupFlag=1;

          })
        }
      })
    }

    


    
    function getxy(){

      const params={
        page: 1,
        limit:1000,
      }
      request({
        url:"dianpuxinxi/page",
        method:"get",
        params
      }).then(({data})=>{
        // console.log(data.data);
        state.list=data.list;
      })
    }

    let map;

    function initmap(){
      AMapLoader.load({
        key: "637042e311014714fd266be0fae5624a", // 申请好的Web端开发者Key，首次调用 load 时必填
        version: "1.4.15", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
        plugins: [          //需要使用的插件
          'AMap.ToolBar',
          'AMap.Scale',
          'AMap.Geolocation',
          'AMap.PlaceSearch',
          'AMap.AutoComplete',
          'AMap.Geocoder',
          'AMap.CitySearch',
          "AMap.Marker"
        ], //需要使用的的插件列表，如比例尺'AMap.Scale'，支持添加多个如：['...','...']
      })
              .then((AMap) => {
                map = new AMap.Map("container", {
                  // 设置地图容器id
                  viewMode: "3D", // 是否为3D地图模式
                  zoom: 18, // 初始化地图级别
                  center: [116.397428, 39.90923], // 初始化地图中心点位置
                });






                //添加定位功能
                AMap.plugin('AMap.Geolocation', () => {
                  const geolocation = new AMap.Geolocation({
                    enableHighAccuracy: true, // 是否使用高精度定位
                    timeout: 10000, // 定位超时时间
                    buttonPosition:'RB',    //定位按钮的停靠位置
                    buttonOffset: new AMap.Pixel(10, 20),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
                    zoomToAccuracy: true,   //定位成功后是否自动调整地图视野到定位点
                  });

                  // 获取当前定位
                  geolocation.getCurrentPosition((status, result) => {
                    if (status === 'complete') {
                      const { lng, lat } = result.position;
                      // this.currentLocation = `经度: ${lng}, 纬度: ${lat}`;
                      map.setCenter([lng, lat]); // 将地图中心点设置为当前位置

                      var markerPoint = new AMap.Marker({
                        position: [lng, lat], // 经纬度
                        offset: new AMap.Pixel(-12, -32), // 标记点偏移量
                        // icon: '//vdata.amap.com/icons/b18/1/2.png', // 添加 Icon 图标 URL（不加icon应该有默认标记）
                      })
                      map.add(markerPoint)

                    } else {
                      console.error('定位失败:', result.message);
                    }
                  });
                });


                //    console.log("坐标系",state.list);

                state.list.map((data) => {
                  console.log(data.lat,data.lnt,data.conent)
                  const marker = new AMap.Marker({
                    position: new AMap.LngLat(data.lnt,data.lat),
                    title: data.conent, // 鼠标滑过点标记时的文字提示
                    icon: iconTeam, // 引入上面的图片
                    // conent: markerconent.value, // 引入上面HTML要素字符串
                    offset: new AMap.Pixel(-15,-15)
                  })
                  // 窗口信息
                  const infoWindow = new AMap.InfoWindow({
                    isCustom: true, // 自定义窗口,窗口外框以及内容完全按照conent所设的值添加
                    closeWhenClickMap: true, // 是否在鼠标点击地图关闭窗口
                    content: `<div style="background-color:lch(8 12.53 21.29 / 0.2);;width: 80px;height: 80px;border-radius: 6px;line-height: 80px;text-align: center;font-size:12px;">${data.conent}</div>`,
                    offset: new AMap.Pixel(0,-15)
                  })
                  // 给marker添加click事件
                  marker.on("click",(e) => {
                    infoWindow.open(
                            map,
                            // 窗口信息的位置
                            marker.getPosition(data.lnt, data.lat)
                    );
                  })
                  // 给map添加zoomend事件,当缩放级别时触发
                  map.on("zoomend",(e) => {
                    // 关闭信息窗体
                    map.clearInfoWindow(infoWindow);
                  })
                  marker.setMap(map);
                })





              })
              .catch((e) => {
                console.log(e);
              });
    }

    function dwxz(){
      state.visibledw=true;
      getxy();
      initmap();

    }

    function closes(){
      state.visibledw=false;
    }





</script>

<style scoped>
/* 聊天窗口样式 */
.chat-messages {
  height: 400px;
  overflow-y: auto;
  padding: 15px;
  background-color: #f5f7fa;
  border-radius: 4px;
  margin-bottom: 15px;
}

.chat-message {
  margin-bottom: 15px;
  display: flex;
}

.chat-message.self {
  justify-content: flex-end;
}

.chat-message.self .message-bubble {
  background-color: #409eff;
  color: white;
}

.chat-message.other {
  justify-content: flex-start;
}

.chat-message.other .message-bubble {
  background-color: white;
  color: #303133;
}

.message-bubble {
  max-width: 70%;
  padding: 10px 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-text {
  word-break: break-word;
  line-height: 1.5;
  margin-bottom: 5px;
}

.message-time {
  font-size: 12px;
  opacity: 0.7;
}

.empty-chat {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #909399;
}

.chat-input-area {
  margin-top: 10px;
}

.chat-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 10px;
}
</style>