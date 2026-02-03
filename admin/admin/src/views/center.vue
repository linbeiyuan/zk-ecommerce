<script setup lang="ts">
      import { Session } from '@/utils/storage';
      import {ref,onMounted,reactive,toRefs, nextTick} from 'vue';
      import request from "@/utils/request";
       import {notify} from '@/utils/element';
       import { uploadImg } from '@/api/common/media';

      import base from "@/utils/base";

      
      const state=reactive({
                ruleForm: {},
                flag: '',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                })
   
      const { ruleForm,flag
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 } = {...toRefs(state)};
     
      const tableName=Session.get("tableName");
     
      nextTick(()=>{

      state.flag = tableName;
     request({
        url:`${tableName}/session`,
        method:'GET'
      }).then((data) => { 
            state.ruleForm = data.data;
    });
   

      })





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

    function onUpdateHandler(){


                                                                                                                if ((!state.ruleForm.yonghuming) && 'yonghu' == state.flag) {

                        notify('用户名不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.mima) && 'yonghu' == state.flag) {

                        notify('密码不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.shoujihao) && 'yonghu' == state.flag) {

                        notify('手机号不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.dizhi) && 'yonghu' == state.flag) {

                        notify('地址不能为空',{type:'error'})
                        return
                    }
                                                                                                                                                                                                    if ((!state.ruleForm.yonghuming) && 'shangjia' == state.flag) {

                        notify('用户名不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.mima) && 'shangjia' == state.flag) {

                        notify('密码不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.shoujihao) && 'shangjia' == state.flag) {

                        notify('手机号不能为空',{type:'error'})
                        return
                    }
                                                                if ((!state.ruleForm.shangjiamingcheng) && 'shangjia' == state.flag) {

                        notify('商家名称不能为空',{type:'error'})
                        return
                    }
                                                                                            
           request({
             url:`${tableName}/update`,
             method:'post',
             data:state.ruleForm
           }).then((data)=>{
            notify('修改信息成功',{type:'success'})
           })



    }




</script>
<template>
    <div>
        <el-form
                class="detail-form-content"
                ref="RefForm"
                :model="ruleForm"
                label-width="80px"
        >
            <el-row>

                                                                                                                                                                            <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="用户名" prop="yonghuming">
                                                            <el-input v-model="ruleForm.yonghuming" placeholder="用户名" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="密码" prop="mima">
                                                            <el-input v-model="ruleForm.mima" placeholder="密码" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="手机号" prop="shoujihao">
                                                            <el-input v-model="ruleForm.shoujihao" placeholder="手机号" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="地址" prop="dizhi">
                                                            <el-input v-model="ruleForm.dizhi" placeholder="地址" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="余额" prop="money">
                                                            <el-input v-model="ruleForm.money" placeholder="余额" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='yonghu'" label="积分" prop="jf">
                                                            <el-input v-model="ruleForm.jf" placeholder="积分" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                                                                                                                                                    <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="用户名" prop="yonghuming">
                                                            <el-input v-model="ruleForm.yonghuming" placeholder="用户名" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="密码" prop="mima">
                                                            <el-input v-model="ruleForm.mima" placeholder="密码" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="手机号" prop="shoujihao">
                                                            <el-input v-model="ruleForm.shoujihao" placeholder="手机号" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="商家名称" prop="shangjiamingcheng">
                                                            <el-input v-model="ruleForm.shangjiamingcheng" placeholder="商家名称" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="余额" prop="money">
                                                            <el-input v-model="ruleForm.money" placeholder="余额" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                                        <el-col :span="12">
                        <el-form-item v-if="flag=='shangjia'" label="积分" prop="jf">
                                                            <el-input v-model="ruleForm.jf" placeholder="积分" clearable></el-input>
                                </el-form-item>
                                </el-col>
                                                                                                        <el-form-item v-if="flag=='users'" label="用户名" prop="username">
                    <el-input v-model="ruleForm.username"
                              placeholder="用户名"></el-input>
                </el-form-item>
                <el-col :span="24">
                    <el-form-item>
                        <el-button type="primary" @click="onUpdateHandler">修 改</el-button>
                    </el-form-item>
                </el-col>
            </el-row>
        </el-form>
    </div>
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
