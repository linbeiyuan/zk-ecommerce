
<script setup>

    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify} from '@/utils/element';
    import { isAuth } from '@/utils/utils'
    import { ElLoading } from 'element-plus'
    const state=reactive({
        ruleForm: {},
        open:false,
        title:'',
        type:'',
        rules: {
            name: [
                { required: true, message: '请输入收件人名称', trigger: 'blur' },
            ],
            phone: [
                { required: true, message: '请输入手机号', trigger: 'blur' }
            ],
            address: [
                { required: true, message: '请输入地址', trigger: 'change' }
            ]

        }
    })
    const emit = defineEmits(['refresh']);
    const {ruleForm,open,type,rules} = {...toRefs(state)};

    const formRef=ref();
    function submitForm() {

        formRef.value?.validate((valid) => {
            if (valid) {

                this.ruleForm.isdefault='否'
                if(this.type=='add'){
                    request({
                        url:'address/add',
                        method:'post',
                        data:state.ruleForm
                    }).then((data) => {
                        if (data && data.code === 0) {
                        notify("新增成功",{type:'success'});
                        state.open=false;
                        emit("refresh");

                    } else {

                        notify(data.msg,{type:'error'});
                    }
                });
                }else{
                    request({
                        url:'address/update',
                        method:'post',
                        data:state.ruleForm
                    }).then((data) => {
                        if (data && data.code === 0) {


                        notify("新增成功",{type:'success'});
                        state.open=false;
                        emit("refresh");

                    } else {
                        notify(data.msg,{type:'error'});
                    }
                });
                }



            } else {
                console.log('error submit!!');
        return false;
    }
    });







    }

    function openaddOrupdate(title,item,type){
        state.open=true;
        state.type=type;
        state.title=title;
        state.ruleForm=item;
    }


    defineExpose({
        openaddOrupdate
    })


</script>

<template>
       <el-dialog :title="title" v-model="open" append-to-body :close-on-click-modal="false" :close-on-press-escape="false">
<el-form :model="ruleForm"  :rules="rules" Lrequired="true" ref="formRef" label-width="100px" class="demo-ruleForm">
  <el-form-item label="收件人" prop="name">
    <el-input v-model="ruleForm.name"></el-input>
  </el-form-item>
  <el-form-item label="收件人电话" prop="phone">
    <el-input v-model="ruleForm.phone"></el-input>
  </el-form-item>
  <el-form-item label="地址" prop="address">
    <el-input type="textarea" v-model="ruleForm.address"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm()">立即创建</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
</el-dialog>
</template>

