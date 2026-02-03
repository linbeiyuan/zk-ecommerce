<script setup lang='ts'>
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import base from "@/utils/base";
    import { uploadImg } from '@/api/common/media';
    import request from "@/utils/request";
    import {notify} from '@/utils/element'
    import { Session } from '@/utils/storage';


    const formRef=ref();
    const state=reactive({
        loadding:false,//加载框
        visible:false,//隐藏显示
        formData:{} as any,
        user:{}
    })
    const initData={

    }
    const {
        loadding,
        visible,
        formData,
        user
    } = {...toRefs(state)};


    function open(tablename:string,title:string,tableid:any,price:any){
                init();

             
        state.formData.title=title;
        state.formData.tablename=tablename;
        state.formData.tableid=tableid;
        state.formData.username=Session.get("adminName");
        state.formData.price=price;
        state.visible=true;
        
        console.log(state.user.id);
    }


    function close(){
        state.visible=false;
    }
    function init(){
        let sessionTable = Session.get("tableName")
        request({
            url: sessionTable + '/session',
            method: "get"
        }).then((
                data
        ) => {
            console.log(user);
            if (data && data.code === 0) {
            state.user = data.data;

        } else {
  
        }
    });
    }



    function submitForm(){
        formRef.value?.validate((valid:boolean)=>{

                if(!valid) return;
                const params={
                    type:'未支付',
                    userid:state.user.id,
                    tableid:state.formData.tableid
                }
                request({
                url:`lease/list`,
                method:'post',
                params
                }).then((data)=>{
                   if(data.data.list.length==0){
                    state.loadding=true;
                state.formData.userid=state.user.id;
                state.formData.type="未支付";
                request({
                url:`lease/add`,
                method:'post',
                data:state.formData
                }).then(({data})=>{
                notify("订单生成，请前往个人中心支付",{type:'success'});
                    state.loadding=false;
                close();

                })
                   }else{
                    notify("您已有未支付操作，请支付之后在操作",{type:'error'});
                   }
                })

                
                
                 

                



                })
    }

    defineExpose({
        open
    })
</script>

<template>
  <el-dialog title="租借" v-model="visible"
               center draggable :before-close="close" width="1000px"
               :close-on-click-modal="false" destroy-on-close>
        <div v-loading="loadding">
            <el-form ref="formRef" :model="formData"
                     label-width="85px" label-right="right"
                     label-suffix=":" status-icon
            >

                <el-form-item label="租借" prop="title" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                    <el-input readonly v-model="formData.title"  maxlength="30" clearable show-word-limit placeholder="请输入" />
                </el-form-item>

                <el-form-item label="用户" prop="username" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                    <el-input readonly v-model="formData.username"  maxlength="30" clearable show-word-limit placeholder="请输入" />
                </el-form-item>

                <el-form-item label="开始时间"  prop="funddate" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                    <el-date-picker v-model="formData.funddate" type="date" maxlength="100"
                         format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
                    placeholder="开始时间" clearable style="width: 200px;"/>
                </el-form-item>
                <el-form-item label="结束时间"  prop="enddate" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                    <el-date-picker v-model="formData.enddate" maxlength="100" type="date" 
                    format="YYYY/MM/DD"
        value-format="YYYY-MM-DD"
                    placeholder="结束时间" clearable style="width: 200px;"/>
                </el-form-item>
                
                
            </el-form>
            <el-row justify="center" class="mt10">
                <el-button @click="close">取 消</el-button>
                <el-button @click="submitForm" type="primary">保 存</el-button>
            </el-row>
        </div>
    </el-dialog>
</template>

<style  scoped>

</style>
