<script setup lang=ts>

import { Session } from '@/utils/storage';
      import {ref,onMounted,reactive,toRefs, nextTick} from 'vue';
      import request from "@/utils/request";
       import {notify} from '@/utils/element'

       const formRef=ref();
       const state=reactive({
                ruleForm: {},
                flag: '',
                user:{},
                rules: {
                    password: [
                        {
                            required: true,
                            message: "密码不能为空",
                            trigger: "blur"
                        }
                    ],
                    newpassword: [
                        {
                            required: true,
                            message: "新密码不能为空",
                            trigger: "blur"
                        }
                    ],
                    repassword: [
                        {
                            required: true,
                            message: "确认密码不能为空",
                            trigger: "blur"
                        }
                    ]
                }
      })
      const { ruleForm,flag,rules } = {...toRefs(state)};




      const tableName=Session.get("tableName");
     
      nextTick(()=>{

      state.flag = tableName;
     request({
        url:`${tableName}/session`,
        method:'POST'
      }).then((data) => { 
            state.user = data.data;
    });
   

      }) 
       
function onUpdateHandler(){
    formRef.value?.validate((valid:boolean)=>{
  
            if(!valid) return;


            var password = "";
                        if (state.user.mima) {
                            password = state.user.mima;
                        } else if (state.user.password) {
                            password = state.user.password;
                        }
                        if (state.ruleForm.password != password) {
                          
                            notify("原密码错误",{type:'error'});
                            return;
                        }
                        if (state.ruleForm.newpassword != state.ruleForm.repassword) {
                          
                            notify("两次密码输入不一致",{type:'error'});
                            return;
                        }
                        state.user.password = state.ruleForm.newpassword;
                        state.user.mima = state.ruleForm.newpassword;

                         request({
                            url:`${tableName}/update`,
                            method:'post',
                            data:state.user
                        
                        }).then((data)=>{
                              console.log(data.code);
                            if (data && data.code === 0) {
                                notify("修改密码成功,下次登录系统生效",{type:'success'});
                            }else{
                                notify(data.msg,{type:'error'});
                            }

                        })



    })
}

</script>

<template>
    <div>
        <el-form
                class="detail-form-content"
                ref="formRef"
                :rules="rules"
                :model="ruleForm"
                label-width="80px"
        >
            <el-form-item label="原密码" prop="password">
                <el-input v-model="ruleForm.password"></el-input>
            </el-form-item>
            <el-form-item label="新密码" prop="newpassword">
                <el-input v-model="ruleForm.newpassword"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="repassword">
                <el-input v-model="ruleForm.repassword"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onUpdateHandler">确 定</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>



     


<style lang="scss" scoped>
</style>
