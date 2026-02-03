<template>

    <el-dialog :title="title" v-model="open" append-to-body :close-on-click-modal="false" :close-on-press-escape="false">

        <el-scrollbar style="height: 700px;">
            <el-form :model="ruleForm"  :rules="rules" Lrequired="true" ref="forumRef" label-width="100px" class="demo-ruleForm">

                <el-form-item label="标题" prop="title">
                    <el-input v-model="ruleForm.title"></el-input>
                </el-form-item>
                <el-form-item label="类型" prop="isdone">
                    <el-radio  v-model="ruleForm.isdone" label="开放">开放</el-radio>
                    <el-radio  v-model="ruleForm.isdone" label="关闭">关闭</el-radio>
                </el-form-item>

                <el-form-item label="内容" prop="content">
                    <Editor v-model="ruleForm.content"/>
                </el-form-item>

                <el-form-item style="line-height: 10%;">
                    <el-button type="primary" @click="submitForm()">立即创建</el-button>
                    <el-button @click="resetForm('ruleForm')">重置</el-button>
                </el-form-item>
            </el-form>
        </el-scrollbar>
    </el-dialog>

</template>

<script setup>
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import { defineAsyncComponent,reactive,ref,toRefs,nextTick } from 'vue';
    import {notify,confirm} from '@/utils/element';
    const Editor=defineAsyncComponent(()=>import('@/components/editor/index.vue'));
       const state=reactive({
           ruleForm: {},
           open:false,
           title:'',
           type:'',
           rules: {
               title: [
                   { required: true, message: '请输入名称', trigger: 'blur' },
               ],
               isdone: [
                   { required: true, message: '请选择类型', trigger: 'blur' }
               ],
               content: [
                   { required: true, message: '请输入内容', trigger: 'change' }
               ]

           }
       })

    const {ruleForm,open,type,rules,tltle} = {...toRefs(state)};
    const emit = defineEmits(['refresh']);
            const forumRef=ref();
           function submitForm() {

               forumRef.value.validate((valid) => {
                if (valid) {
                    state.ruleForm.username=Session.get("adminName");
                    state.ruleForm.parentid=0;
                if(state.type=='add'){
                        request({
                url:'forum/add',
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
                url:'forum/update',
                method:'post',
                data:state.ruleForm
                }).then((data) => {
                if (data && data.code === 0) {
                        notify("修改成功",{type:'success'});
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

