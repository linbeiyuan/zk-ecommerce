<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs,onMounted,computed,watch,nextTick } from 'vue';
    import { useRoute } from 'vue-router';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify,confirm} from '@/utils/element';
    import { isAuth } from '@/utils/utils';
    import {exportExcel} from '@/utils/exportExcel';
    import printJS from 'print-js'
    
    import { useSocketStore } from '../../stores/socketStore';
    
    const state = reactive({
        ruleForm: {
            ask:''
        },
        dataList: [],
        showFlag:true,
        open:false,
        userInfo: undefined,
        im_users: [],
        targetUserId: undefined
    })
    
    const ragRef=ref();
    const ragRefInstance=ref();
    const {id, ruleForm, dataList, userInfo, inter, open, im_users, targetUserId} = {...toRefs(state)};
    const selectedIndex = ref(null);
    const scrollableDiv = ref(null);
    const route = useRoute();
    
    let socketStore = useSocketStore();
    state.userInfo = JSON.parse(localStorage.getItem('user'));
    
    if (socketStore.socket === undefined || socketStore.socket == null || socketStore.socket.readyState === WebSocket.CLOSE) {
        socketStore.initializeSocket(state.userInfo.id, state.userInfo.nicheng, state.userInfo.role)
    }
    let socket = socketStore.socket;
    
    getHistoryMsg();
    
    function onSubmit() {
        if (state.targetUserId == undefined) {
            alert('先选择聊天用户')
            return;
        }
        if (state.ruleForm.ask != undefined && state.ruleForm.ask != '') {
            state.dataList.push({'userId': parseInt(state.targetUserId), 'nickname': state.userInfo.nicheng, 'ask': state.ruleForm.ask, 'sendTime': getCurrentDateTime()});
            
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
        console.log('收到消息', data)
        if (data.type === 'MESSAGE') {
            let existUser = false;
            for (let i = 0; i < state.im_users.length; i++) {
                if (state.im_users[i]['userId'] == data.srcUserIdStr) {
                    if (state.targetUserId != data.srcUserIdStr) {
                        if(state.im_users[i]['unread_msg_count'] == '') {
                            state.im_users[i]['unread_msg_count'] = 1
                        } else {
                            state.im_users[i]['unread_msg_count'] = parseInt(state.im_users[i]['unread_msg_count']) + 1
                        }
                    }
                    existUser = true;
                    break;
                }
            }
            if(!existUser) {
                let im_user = {}
                im_user['nicheng'] = data.srcUserNichengStr
                im_user['userId'] = parseInt(data.srcUserIdStr)
                if (state.targetUserId != data.srcUserIdStr) {
                    im_user['unread_msg_count'] = 1
                }
                state.im_users.push(im_user)
            }
            
            if (state.targetUserId == data.srcUserIdStr && route.path == '/wenzhen') {
                request({
                    url:`consultation/update`,
                    method:'POST',
                    data: {sender: data.srcUserIdStr}
                }).then(resp => {
                    state.dataList.push({'userId': parseInt(data.srcUserIdStr), 'nickname': data.srcUserNichengStr, 'reply': data.msg, 'sendTime': data.sendTime});
                    scrollToBottom();
                })
            } else {
                state.dataList.push({'userId': parseInt(data.srcUserIdStr), 'nickname': data.srcUserNichengStr, 'reply': data.msg, 'sendTime': data.sendTime});
            }
        }
    };
    
    socket.onclose = () => {
        console.log('WebSocket连接已关闭');
        socketStore.initializeSocket(state.userInfo.id, state.userInfo.nicheng, state.userInfo.role)
        socket = socketStore.socket;
    };
    
    // function getOnlineUsers() {
    //   request({
    //     url:`doctorUserChat/queryOnlineUser`,
    //     method:'get'
    //   }).then(resp => {
    //     for (let i = 0; i < resp.data.length; i++) {
    //       state.im_users.push({'nicheng': '某人'+i, 'userId': resp.data[i]})
    //     }
    //   })
    // }
    
    //查询历史消息
    function getHistoryMsg() {
        request({
            url:`consultation/queryMsg`,
            method:'get',
            params: {receiver: state.userInfo.id}
        }).then(resp => {
            let data = resp.data;
            console.log(data)
            const result = data.reduce((acc, message) => {
                const senderId = message.sender;
                if (senderId != state.userInfo.id && !acc[senderId]) {
                    acc[senderId] = {
                        userId: senderId,
                        nicheng: message.senderName,
                        unread_msg_count: 0
                    };
                }
                if (senderId != state.userInfo.id && message.readStatus === 0) {
                    acc[senderId].unread_msg_count++;
                    
                } else if (senderId != state.userInfo.id && message.readStatus === 1) {
                    acc[senderId] = {
                        userId: senderId,
                        nicheng: message.senderName,
                        unread_msg_count: ''
                    };
                }
                return acc;
            }, {});
            
            const finalResult = Object.values(result);
            // console.log(finalResult)
            state.im_users = finalResult;
            
            for (let i = 0; i < data.length; i++) {
                if(data[i]['sender'] != state.userInfo.id) {
                    state.dataList.push({'userId': parseInt(data[i]['sender']), 'nickname': data[i]['senderName'], 'reply': data[i]['msg'], 'sendTime': data[i]['sendTime']});
                } else {
                    state.dataList.push({'userId': parseInt(data[i]['receiver']), 'nickname': state.userInfo.nicheng, 'ask': data[i]['msg'], 'sendTime': data[i]['sendTime']});
                }
            }
        })
    }
    
    function setTargetUser(userId, index) {
        state.targetUserId = userId;
        selectedIndex.value = index;
        for (let i = 0; i < state.im_users.length; i++) {
            if (state.im_users[i]["userId"] == userId) {
                state.im_users[i]["unread_msg_count"] = '';
            }
        }
        
        nextTick(function () {
            scrollToBottom()
        })
        
        request({
            url:`consultation/update`,
            method:'POST',
            data: {sender: userId}
        }).then(resp => {
        
        })
    }
    
    const scrollToBottom = () => {
        if (scrollableDiv.value) {
            scrollableDiv.value.scrollTop = scrollableDiv.value.scrollHeight;
        }
    };
    
    
    const cleanupFunction = () => {
        // socket.close();
    };
    
    watch(route, (to, from) => {
        cleanupFunction(); // 在路由变化时执行清理工作
    });
    
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

</script>

<template>
    <el-form @submit.prevent="onSubmit" style="height: 800px; border: 1px solid silver; background-color: #C8C8A9;" class="detail-form-content chat-form" v-model="ruleForm" label-width="0">
        <div style="width: 100%; height: 100%; display: flex; justify-content: center;">
            
            <div style="width: 200px; height: 100%; border: 1px; background-color: white;">
                <div class="selectable-div" v-for="(user, index) in im_users" :key="index" :class="{ selected: selectedIndex === index }" @click="setTargetUser(user.userId, index)">
                    <div style="width: 150px; display: flex; justify-content: center; align-items: center;">
                        <img src="../../assets/avatar2.jpg" style="width: 30px; height:30px; border-radius: 20px;"/>
                        <el-badge :value="user.unread_msg_count" class="item">
                            <div style="min-width: 50px; width: auto;">{{user.nicheng}}</div>
                        </el-badge>
                    </div>
                </div>
            </div>
            
            <div style="background-color: lightblue; height:100%; display: flex; flex-direction: column; justify-content: center; width: 100%;">
                <div class="chat-content" ref="scrollableDiv">
                    <div style="width: 100%;" v-bind:key="item.id" v-for="item in dataList" v-show="item.userId == state.targetUserId">
                        <div v-if="item.ask" class="left-content" >
                            <div style="font-size: 12px; font-family: '微软雅黑 Light'; font-weight: bold; margin-bottom: 5px;text-align:left;">{{item.nickname}} {{item.sendTime}}</div>
                            <el-alert class="text-content" :title="item.ask" :closable="false" style="color: black; font-size: 16px;" ></el-alert>
                        </div>
                        <div v-else class="right-content" >
                            <div style="font-size: 12px; font-family: '微软雅黑 Light'; font-weight: bold; margin-bottom: 5px;text-align:right;">{{item.nickname}} {{item.sendTime}}</div>
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
</template>

<style scoped>
    .item {
        //margin-top: 10px;
        //margin-right: 30px;
    }
    
    .selectable-div {
        padding: 10px;
        margin: 5px;
        border: 1px solid #ccc;
        cursor: pointer;
        text-align: center;
        transition: background-color 0.3s;
    }
    
    .selectable-div:hover {
        background-color: #cccccc;
    }
    
    .selectable-div.selected {
        background-color: lightblue;
    }
    
    html,body,#app {
        height: 100%;
    }
    body {
        margin: 0;
    }
    .chat-form {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .chat-content {
        overflow-y: auto;
        border: 1px solid #eeeeee;
        margin: 0;
        padding: 10px 5px 100px 5px;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .left-content {
        float: left;
        padding: 10px;
    }
    .right-content {
        float: right;
        padding: 10px;
    }
    .clear-float {
        clear: both;
    }
    .btn-input {
        margin-left: 0px;
        display: flex;
        width: 100%;
        padding: 10px 12px;
        box-sizing: border-box;
    }
</style>
