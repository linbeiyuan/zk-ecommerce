<script setup lang='ts'>
  import { defineAsyncComponent,reactive,ref,toRefs,defineProps } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify} from '@/utils/element';
  import { isAuth } from '@/utils/utils';
  import { ElLoading } from 'element-plus';

  import { useSocketStore } from '../../stores/socketStore';

  const state=reactive({
    ruleForm: {
      ask:''
    },
    dataList: [],
    showFlag:true,
    open:false,
    userInfo: undefined,
    im_users: [],
    targetUserId: undefined,
    targetUserNicheng: '',
  })

  const ragRef=ref();
  const ragRefInstance=ref();
  const {id,ruleForm,dataList,userInfo,inter,open, im_users, targetUserId, targetUserNicheng} = {...toRefs(state)};
  const selectedIndex = ref(null);
  const scrollableDiv = ref(null);

  // 父组件传值给子组件
  // const props = defineProps({
  //   userId: String, // 指定 detail 的类型为 String
  //   biaoti: String, // 指定 biaoti 的类型为 String
  // });
  // state.targetUserId = props.userId
  // state.targetUserNicheng = props.biaoti

  let socketStore = useSocketStore();
  state.userInfo = JSON.parse(localStorage.getItem('user'));

  if (socketStore.socket === undefined || socketStore.socket == null || socketStore.socket.readyState === WebSocket.CLOSE) {
    socketStore.initializeSocket(state.userInfo.id, state.userInfo.nicheng, state.userInfo.role)
  }
  let socket = socketStore.socket;

  function openaddOrupdate(detail) {
    state.dataList = []
    state.im_users = []
    state.targetUserId = detail.userid
    state.targetUserNicheng = detail.biaoti
    getHistoryMsg();
    state.open = true;
  }

  function getCurrentDateTime() {
    const now = new Date();
    // 获取年份，并填充为四位数
    const year = now.getFullYear();
    // 获取月份，并填充为两位数
    const month = String(now.getMonth() + 1).padStart(2, '0'); // 月份从0开始，需要加1
    // 获取日期，并填充为两位数
    const day = String(now.getDate()).padStart(2, '0');
    // 获取小时，并填充为两位数
    const hours = String(now.getHours()).padStart(2, '0');
    // 获取分钟，并填充为两位数
    const minutes = String(now.getMinutes()).padStart(2, '0');
    // 获取秒，并填充为两位数
    const seconds = String(now.getSeconds()).padStart(2, '0');
    // 拼接成目标格式
    const formattedDateTime = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    return formattedDateTime;
  }

  function onSubmit(){
    if (state.ruleForm.ask != undefined && state.ruleForm.ask != '') {
      state.dataList.push({'ask': state.ruleForm.ask, 'nickname': state.userInfo.nicheng, 'sendTime': getCurrentDateTime()});

      socket.send(JSON.stringify({
        type: 'MESSAGE',
        srcUserId: state.userInfo.id,
        srcUserNicheng: state.userInfo.nicheng,
        targetUserId: state.targetUserId,  //给谁发消息
        msg: state.ruleForm.ask
      }));
      state.ruleForm.ask = '';
      scrollToBottom();
    }
  }

  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === 'MESSAGE') {
      console.log('收到消息', data)
      // console.log(state.dataList)
      state.dataList.push({'reply': data['msg'], 'nickname': data['srcUserNichengStr'], 'sendTime': data['sendTime']});
      scrollToBottom();
    }
    if (data.type === 'JOIN') {
    }
  };

  socket.onclose = () => {
    socketStore.initializeSocket(state.userInfo.id, state.userInfo.nicheng, state.userInfo.role)
    socket = socketStore.socket;
    console.log('WebSocket连接已关闭');
  };

  //查询历史消息
  function getHistoryMsg() {
    request({
      url:`consultation/querySomeBodyMsg`,
      method:'get',
      params: {sender: state.targetUserId}
    }).then(resp => {
      let data = resp.data;

      for (let i = 0; i < data.length; i++) {
        if(data[i]['sender'] != state.userInfo.id) {
          state.dataList.push({'reply': data[i]['msg'], 'nickname': data[i]['senderName'], 'sendTime': data[i]['sendTime']});
        } else {
          state.dataList.push({'ask': data[i]['msg'], 'nickname': data[i]['senderName'], 'sendTime': data[i]['sendTime']});
        }
      }
    })
  }

  // 更新消息状态
  function updateMsgStatus() {
    request({
      url:`consultation/update`,
      method:'POST',
      data: {sender: this.targetUserId}
    }).then(resp => {

    })
  }

  function initUser() {
    let im_user = {}
    im_user['nicheng'] = this.targetUserNicheng
    im_user['userId'] = this.targetUserId
    im_user['unread_msg_count'] = ''
    state.im_users.push(im_user)
  }

  function handleClose() {
    state.open = false;
  }

  const scrollToBottom = () => {
    if (scrollableDiv.value) {
      scrollableDiv.value.scrollTop = scrollableDiv.value.scrollHeight;
    }
  };


  // updateMsgStatus();

  defineExpose({
    openaddOrupdate,
    updateMsgStatus
  })
</script>

<template>
  <el-dialog :before-close="handleClose" :title="title" v-model="open" append-to-body :close-on-click-modal="false" :close-on-press-escape="false">
    <el-form @submit.prevent="onSubmit" style="height: 500px; border: 1px solid silver; background-color: #C8C8A9;" class="detail-form-content chat-form" v-model="ruleForm" label-width="0">
      <div style="width: 100%; height: 100%; display: flex; justify-content: center;">

        <div style="width: 200px; height: 100%; border: 1px; background-color: white;">
          <div class="selectable-div" >
            <div style="width: 150px; display: flex; justify-content: center; align-items: center;">
              <img src="../../assets/avatar2.jpg" style="width: 30px; height:30px; border-radius: 20px;"/>
              <!--              <el-badge :value="user.unread_msg_count" class="item">-->
              <div style="min-width: 50px; width: auto;">{{targetUserNicheng}}</div>
              <!--              </el-badge>-->
            </div>
          </div>
        </div>

        <div style="background-color: lightblue; height:100%; display: flex; flex-direction: column; justify-content: center; width: 100%;">
          <div class="chat-content" ref="scrollableDiv">
            <div style="width: 100%;" v-for="item in dataList">
              <div v-if="item.ask" class="left-content" >
                <div style="font-size: 12px; font-family: '微软雅黑 Light'; font-weight: bold; margin-bottom: 5px; text-align: left;">{{item.nickname}} {{item.sendTime}}</div>
                <el-alert class="text-content" :title="item.ask" :closable="false" style="color: black; font-size: 16px;" ></el-alert>
              </div>
              <div v-else class="right-content" >
                <div style="font-size: 12px; font-family: '微软雅黑 Light'; font-weight: bold; margin-bottom: 5px; text-align: right;">{{item.nickname}} {{item.sendTime}}</div>
                <el-alert class="text-content" :title="item.reply" :closable="false" style="color: black; font-size: 16px;" ></el-alert>
              </div>
            </div>
          </div>

          <div class="btn-input" style="height:60px;">
            <el-input style="flex: 1;margin-right: 10px;" v-model="ruleForm.ask" placeholder="请输入沟通内容" clearable @keydown.enter.native="onSubmit" autofocus></el-input>
            <el-button type="primary" @click="onSubmit">发送</el-button>
          </div>
        </div>
      </div>
    </el-form>
  </el-dialog>
</template>

