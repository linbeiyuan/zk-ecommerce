<script setup lang='ts'>
    import { defineAsyncComponent,reactive,ref,toRefs,nextTick } from 'vue';
    import {notify,confirm} from '@/utils/element';
    import { uploadImg } from '@/api/common/media';
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import base from "@/utils/base";
    const state=reactive({
        ruleForm:{
            username:'',
            userid:'',
            content:'',
            cpicture:''
        },
        loadding:false,
        user:{},
        allmessages:[],
        page:{
            current:1,
            size:10000,
            total:0
        },
        dialogFormVisible:false
    })

    const {ruleForm,loadding,allmessages,page,dialogFormVisible} = {...toRefs(state)};

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

    async function handleUploadImg(options: any){
        // console.log('handleUploadImg', options);
        try {
            loadding.value = true;
            const form = new FormData();
            form.append('file', options.file);
            form.append('data', JSON.stringify({sourceType: 'goods_img'}));
            // 开始上传
            const data = await uploadImg(form);

            // 上传成功 , 将上传成功的图片地址赋值回显出来
            const name=base.get().url;
            ruleForm.value.cpicture = name+'upload/'+ data.file;
        } catch(e) {

        } finally {
            loadding.value = false;
        }
    }

    function onSubmit(){
        ruleForm.value.userid=state.user.id;
        ruleForm.value.username=Session.get("adminName");
        request({
            url:'messagess/add',
            method: "post",
            data:state.ruleForm
        }).then((
                data
        ) => {
            if (data && data.code === 0) {
            notify("留言成功",{type:'success'});
            state.ruleForm={};
            state.dialogFormVisible=false;
            getmessages();
        } else {
            notify(data.msg,{type:'error'});


        }
    });
    }
    getmessages();

    function getmessages() {

        const params={
            page: state.page.current,
            limit: state.page.size,
            order:'desc',
            sort:'addtime'
        }

        request({
            url: `messagess/list`,
            method: "get",
            params
        }).then((data) => {
            if (data && data.code === 0) {

            state.allmessages=data.data.list;
        } else {
            notify(data.msg,{type:'error'});
        }
    });
    }


    function addly(){
        state.dialogFormVisible=true;
    }

</script>

<template>

    <el-divider>
        <el-text class="mx-1" size="default">在线留言</el-text>
    </el-divider>



    <el-card style="width: 50%;margin: auto;">
        <el-button type="primary" @click="addly">点我留言</el-button>
    </el-card>



    <el-dialog v-model="dialogFormVisible" title="留言" width="500">
        <el-card style="width: 100%;margin: auto;">
            <el-form
                    ref="formRef" :model="ruleForm"
                    label-width="85px" label-right="right"
                    label-suffix=":" status-icon
            >
                <el-row>



                    <el-col :span="24">
                        <el-form-item label="图片" prop="picture" :rules="{required: true, message: '为必填项', trigger: 'blur'}">

                            <el-upload
                                    class="avatar-uploader"
                                    accept="image/png,image/jpg,image/jpeg"
                                    action="#"
                                    :show-file-list="false"
                                    :http-request="handleUploadImg"
                            >
                                <img style="width: 100px;height: 100px;" v-if="ruleForm.cpicture" :src="ruleForm.cpicture" class="avatar" />
                                <el-icon v-else class="avatar-uploader-icon"><ele-Plus /></el-icon>

                            </el-upload>
                        </el-form-item>
                    </el-col>


                    <el-col :span="24">
                        <el-form-item label="反馈内容">
                            <el-input v-model="ruleForm.content" type="textarea" />
                        </el-form-item>
                    </el-col>



                </el-row>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                </el-form-item>
            </el-form>

        </el-card>

    </el-dialog>

    <el-card class="el-card-d" shadow="always">
        <div class="infinite-list-wrapper" style="overflow:auto;">
            <el-timeline
                    infinite-scroll-disabled="disabled">
                <div v-if="allmessages.length>0">
                    <el-timeline-item v-for="(item,index) in allmessages"  :key="index" :timestamp='item.addtime' placement="top">
                        <el-card class="el-card-m">
                            <h4>{{item.username}}：</h4>
                            <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{item.content}}</p>
                            <el-image :zoom-rate="1.2"
                                      :max-scale="7"
                                      :min-scale="0.2"
                                      :preview-src-list="[item.cpicture]" v-if="item.cpicture" :src="item.cpicture" style="width: 100px;height: 100px;"/>

                            <el-card v-if="item.reply">
                                <h5>管理员回复：{{item.reply}}</h5>

                                <el-image :zoom-rate="1.2"
                                          :max-scale="7"
                                          :min-scale="0.2"
                                          :preview-src-list="[item.rpicture]" v-if="item.rpicture" :src="item.rpicture" style="width: 100px;height: 100px;"/>
                            </el-card>
                        </el-card>
                    </el-timeline-item>
                </div>
                <div v-else>
                    <el-timeline-item placement="top">
                        <el-card class="el-card-m" style="height:120px">
                            <h4>大黄子：</h4>
                            <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 说点什么吧😁</p>
                        </el-card>
                    </el-timeline-item>
                </div>
            </el-timeline>
        </div>

    </el-card>


</template>

