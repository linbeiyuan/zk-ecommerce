<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify,confirm} from '@/utils/element';
    import { isAuth } from '@/utils/utils';
    import {exportExcel} from '@/utils/exportExcel';
    import printJS from 'print-js'
    import { layer } from '@layui/layui-vue';
    import { uploadImg } from '@/api/common/media';
    import base from "@/utils/base";
    const AddEdit=defineAsyncComponent(()=>import('@/views/lease/add-edit.vue'));
    const state=reactive({
        query:{

        },
        page:{
            current:1,
            size:10,
            total:0
        },
        tableList:[],
        ids:[],
        isdel:true,
        dialogFormVisible:false,
        detail:{},
        ruleForm:{
            reply:'',
            rpicture:''
        },
        loadding:false

    })
    const { query,tableList,page,isdel,ids,dialogFormVisible,loadding,detail,ruleForm
    } = {...toRefs(state)};

    //进入执行
    getDateList();
    //获取列表
    function getDateList(){
        const params={
            page: state.page.current,
            limit: state.page.size,
        }


        if (state.query.username != '' && state.query.username != undefined) {
            params['username'] = '%' + state.query.username + '%'
        }


        request({
            url:'messagess/page',
            method:'post',
            params
        }).then(({data})=>{

            state.page.total=data.total;
        state.tableList=data.list;
    })
    }
    //查询
    function handleQuery(){
        getDateList();
    }

    //删除

    function handleDelete(row:any){

        layer.confirm("是否要删除",
                {
                    btn: [
                        {text:'确认', callback: (id) => {
                            request({
                                        url:`messagess/delete`,
                        method:'post',
                data:[row.id]
    }).then(({data})=>{
            layer.msg("删除成功", { time: 1000, icon: 1 })
        layer.close(id);
        getDateList();

    })
    }
    },
        {text:'取消', callback: (id) => {

            layer.close(id); }
        }
    ]
    }
    );




    }

    const multipleSelection = ref<[]>([]);

    function handleSelectionChange(val:any){
        multipleSelection.value=val;
        const list=toRaw(multipleSelection.value)
        list.forEach((item)=>{
            state.ids.push(item.id);
    })

        if(list.length==0){
            state.ids=[];
            state.isdel=true
        }else{
            state.isdel=false
        }

    }


    function listdel(){

        if(state.ids.length==0){
            layer.msg("多选删除项不能为空", { icon : 2, time: 1000})
            return;
        }else{
            request({
                url:`messagess/delete`,
                method:'post',
                data:state.ids
            }).then(({data})=>{
                notify("删除成功",{type:'success'});
            getDateList();

        })
        }



    }


    const users=Session.get(Key.userInfoKey);

    const editRef=ref();

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
            detail.value.rpicture = name+'upload/'+ data.file;
        } catch(e) {

        } finally {
            loadding.value = false;
        }
    }


    function messagesbyid(row){
        state.detail=row;
        state.dialogFormVisible=true;
    }


    function onSubmit(){
        request({
            url:'messagess/update',
            method: "post",
            data:state.detail
        }).then((
                data
        ) => {
            if (data && data.code === 0) {
            notify("回复成功",{type:'success'});
            state.ruleForm={};
            state.dialogFormVisible=false;
            getDateList();
        } else {
            notify(data.msg,{type:'error'});


        }
    });
    }


    const columns = ref([

        { title:"选项", width: "55px", type: "checkbox", fixed: "left" },
        { title:"留言人",key:"username"},
        { title:"图片",key:"cpicture", customSlot: "cpicture"},
        { title:"回复图片",key:"rpicture", customSlot: "rpicture"},
        { title:"操作", width: "150px", customSlot:"operator", key:"operator", fixed: "right", ignoreExport: true }]);





</script>

<template>
    <el-card shadow="never" class="index">
        <template #header>
            <div class="card_header">

                <b>列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">


                <el-form-item label="留言人"  prop="username">
                    <el-input v-model="query.username" maxlength="100" placeholder="留言人" clearable style="width: 200px;"/>
                </el-form-item>

                <el-form-item>
                    <lay-button type="primary" @click="handleQuery()">查询</lay-button>
                    <lay-button v-if="isAuth('qichexinxi','删除')" type="danger" @click="listdel()">多选删除</lay-button>
                </el-form-item>
            </el-form>






            <div style="height: 400px;">
                <lay-table :height="'100%'"
                           :columns="columns"
                           :data-source="tableList"
                           v-model:selected-keys="ids">


                    <template #cpicture="{ row }">
                        <img v-if="row.cpicture" :src="row.cpicture" width="100" height="100">
                        <div v-else>无图片</div>

                    </template>
                    <template #rpicture="{ row }">
                        <img v-if="row.rpicture" :src="row.rpicture" width="100" height="100">
                        <div v-else>无图片</div>

                    </template>

                    <template v-slot:operator="{ row }">
                        <lay-button size="xs" type="primary" @click="messagesbyid(row)" >回复</lay-button>
                        <lay-button size="xs" type="danger" @click="handleDelete(row)" >删除</lay-button>
                    </template>

                </lay-table>
            </div>



            <!-- 分页 -->
            <m-page :page="page" @pageChange="getDateList"/>

            <AddEdit ref="editRef" @refresh="getDateList"/>
        </div>
    </el-card>
    <el-dialog v-model="dialogFormVisible" title="回复留言" width="500">
        <el-card style="width: 100%;margin: auto;">
            <el-form
                    ref="formRef" :model="ruleForm"
                    label-width="85px" label-right="right"
                    label-suffix=":" status-icon
            >
                <el-row>
                    <el-col :span="24">
                        <el-form-item label="留言内容">
                            <el-input disabled v-model="detail.content" type="textarea" />
                        </el-form-item>
                    </el-col>


                    <el-col :span="24">
                        <el-form-item label="图片" prop="rpicture" :rules="{required: true, message: '为必填项', trigger: 'blur'}">

                            <el-upload
                                    class="avatar-uploader"
                                    accept="image/png,image/jpg,image/jpeg"
                                    action="#"
                                    :show-file-list="false"
                                    :http-request="handleUploadImg"
                            >
                                <img style="width: 100px;height: 100px;" v-if="detail.rpicture" :src="detail.rpicture" class="avatar" />
                                <el-icon v-else class="avatar-uploader-icon"><ele-Plus /></el-icon>

                            </el-upload>
                        </el-form-item>
                    </el-col>


                    <el-col :span="24">
                        <el-form-item label="回复内容">
                            <el-input v-model="detail.reply" type="textarea" />
                        </el-form-item>
                    </el-col>



                </el-row>
                <el-form-item>
                    <el-button type="primary" @click="onSubmit">提交</el-button>
                </el-form-item>
            </el-form>

        </el-card>

    </el-dialog>

</template>

<style scoped>
    .avatar-uploader{
        border:1px solid #e4e6e9
    }

    .avatar-uploader .el-upload {
        border: 1px dashed var(--el-border-color);
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: var(--el-transition-duration-fast);
    }

    .avatar-uploader .el-upload:hover {
        border-color: var(--el-color-primary);
    }

    .el-icon.avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        text-align: center;
    }

</style>
