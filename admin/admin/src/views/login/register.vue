<script setup lang="ts">
import { defineAsyncComponent, reactive, ref, toRefs } from 'vue';
import base from "@/utils/base";
import { uploadImg } from '@/api/common/media';
import request from "@/utils/request";
import { notify } from '@/utils/element'
import { Session } from '@/utils/storage';
const Editor = defineAsyncComponent(() => import('@/components/editor/index.vue'));
const formRef = ref();
const state = reactive({
    loadding: false,//加载框
    visible: false,//隐藏显示
    formData: {} as any,
                                                                                                                                                                                                                                                                                                                                                title: '注册',
    tableName: ''
})
const initData = {

}
const {
    loadding,
    visible,
    formData,
    title,
    tableName,
                                                                                                                                                                                                                                                                                                                                            
} = { ...toRefs(state) };


function open(tableName: string,title:string) {

    state.tableName = tableName;
    state.visible = true;
    state.title = title
}


const emit = defineEmits(['refresh']);

const close = () => {
    state.visible = false;
}

function submitForm() {
    formRef.value?.validate((valid: boolean) => {

        if (!valid) return;
        state.loadding = true;
        request({
            url: `${state.tableName}/register`,
            method: 'post',
            data: state.formData
        }).then(({ data }) => {
            notify("注册成功", { type: 'success' });
            state.loadding = false;
            close();

        })



    })

}

defineExpose({
    open
})

                
               
               
               
               
               
               
               
   
                        
               
               
               
               
               
               
               
   
        

</script>

<template>
    <el-dialog :title="title" v-model="visible" center draggable :before-close="close" width="400px"
        :close-on-click-modal="false" destroy-on-close>
        <div v-loading="loadding">
            <el-form ref="formRef" :model="formData" label-width="100px" label-right="right" label-suffix=":"
                status-icon style="width: 300px; margin: 0 auto;">

                                                                                                                                
                        <el-form-item  v-if="tableName=='yonghu'" label="用户名" prop="yonghuming" :rules="{required: true, message: '用户名为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.yonghuming" maxlength="30" clearable show-word-limit placeholder="请输入用户名" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='yonghu'" label="密码" prop="mima" :rules="{required: true, message: '密码为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.mima" maxlength="30" clearable show-word-limit placeholder="请输入密码" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='yonghu'" label="手机号" prop="shoujihao" :rules="{required: true, message: '手机号为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.shoujihao" maxlength="30" clearable show-word-limit placeholder="请输入手机号" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='yonghu'" label="地址" prop="dizhi" :rules="{required: true, message: '地址为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.dizhi" maxlength="30" clearable show-word-limit placeholder="请输入地址" />
                        </el-form-item>
                                                                                                                                                                                                                                 
                        <el-form-item  v-if="tableName=='shangjia'" label="用户名" prop="yonghuming" :rules="{required: true, message: '用户名为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.yonghuming" maxlength="30" clearable show-word-limit placeholder="请输入用户名" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='shangjia'" label="密码" prop="mima" :rules="{required: true, message: '密码为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.mima" maxlength="30" clearable show-word-limit placeholder="请输入密码" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='shangjia'" label="手机号" prop="shoujihao" :rules="{required: true, message: '手机号为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.shoujihao" maxlength="30" clearable show-word-limit placeholder="请输入手机号" />
                        </el-form-item>
                                                        
                        <el-form-item  v-if="tableName=='shangjia'" label="商家名称" prop="shangjiamingcheng" :rules="{required: true, message: '商家名称为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.shangjiamingcheng" maxlength="30" clearable show-word-limit placeholder="请输入商家名称" />
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
.avatar-uploader {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 1px dashed var(--el-border-color);
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader:hover {
    border-color: var(--el-color-primary);
}

.avatar {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 100px;
    height: 100px;
}
</style>