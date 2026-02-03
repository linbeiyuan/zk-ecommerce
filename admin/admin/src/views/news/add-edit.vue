<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import base from "@/utils/base";
    import { uploadImg } from '@/api/common/media';
    import request from "@/utils/request";
    import {notify} from '@/utils/element'
    const Editor=defineAsyncComponent(()=>import('@/components/editor/index.vue'));
    const formRef=ref();
    const state=reactive({
        loadding:false,//加载框
        visible:false,//隐藏显示
        formData:{} as any,
        title:'新增',
        type:'add'
    })
    const initData={

    }
    const {
        loadding,
        visible,
        formData,
        title,
        type
    } = {...toRefs(state)};


    function open(title:string,type:string,formData?:any){

        state.title=title;
        state.type=type;
        state.formData={...formData,...initData};
        state.visible=true;
    }


    const emit = defineEmits(['refresh']);

    const close=()=>{
        state.visible=false;
    }

    function submitForm(){
        formRef.value?.validate((valid:boolean)=>{

            if(!valid) return;
            state.loadding=true;
            request({
                url:`news/${!state.formData.id ? "save" : "update"}`,
                method:'post',
                data:state.formData
            }).then(({data})=>{
                notify("操作成功",{type:'success'});
            state.loadding=false;
            close();
            emit("refresh");
        })



        })

    }

    defineExpose({
        open
    })














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
            formData.value.picture = name+'upload/'+ data.file;
        } catch(e) {

        } finally {
            loadding.value = false;
        }
    }










</script>

<template>
    <el-dialog :title="`${title}`" v-model="visible"
               center draggable :before-close="close" width="1000px"
               :close-on-click-modal="false" destroy-on-close>
        <div v-loading="loadding">
            <el-form ref="formRef" :model="formData"
                     label-width="85px" label-right="right"
                     label-suffix=":" status-icon
            >

                <el-form-item label="标题" prop="title" :rules="{required: true, message: '标题为必填项！', trigger: 'blur'}">
                    <el-input v-model="formData.title" maxlength="30" clearable show-word-limit placeholder="请输入标题" />
                </el-form-item>


                <el-form-item label="介绍" prop="introduction">
                    <el-input v-model="formData.introduction" maxlength="100" clearable show-word-limit type="textarea" />
                </el-form-item>


                <el-form-item label="图片" prop="picture" :rules="{required: true, message: '为必填项', trigger: 'blur'}">

                    <el-upload
                            class="avatar-uploader"
                            accept="image/png,image/jpg,image/jpeg"
                            action="#"
                            :show-file-list="false"
                            :http-request="handleUploadImg"
                    >
                        <img style="width: 100px;height: 100px;" v-if="formData.picture" :src="formData.picture" class="avatar" />
                        <el-icon v-else class="avatar-uploader-icon"><ele-Plus /></el-icon>

                    </el-upload>
                </el-form-item>


                <el-form-item label="内容" prop="content">

                    <Editor v-model="formData.content"/>

                </el-form-item>




            </el-form>
            <el-row justify="center" class="mt10">
                <el-button @click="close">取 消</el-button>
                <el-button @click="submitForm" type="primary">保 存</el-button>
            </el-row>
        </div>
    </el-dialog>
</template>

<style lang="scss" scoped>
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