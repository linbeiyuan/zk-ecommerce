<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import base from "@/utils/base";
    import { uploadImg } from '@/api/common/media';
    import request from "@/utils/request";
    import {notify} from '@/utils/element'
    import { Session } from '@/utils/storage';
    const Editor=defineAsyncComponent(()=>import('@/components/editor/index.vue'));


                            
    const formRef=ref();
    const state=reactive({
        loadding:false,//加载框
        visible:false,//隐藏显示
        formData:{} as any,                                                                                                                                                                                                                                                                                                    title:'新增',
        type:'add',
        crkformData:{
            name:"",
            tablename:"",
            sl:0,
            refid:"",
            crkzt:""
        },
        crkzt:['出库','入库']
    })
    const initData={

    }
    const {
        loadding,
        visible,
        formData,
        title,
        type,
        crkformData                                                                                                                                          
                                                                                                                                                        } = {...toRefs(state)};


    function open(title:string,type:string,tablename:string,formData?:any){
        state.title=title;
        state.type=type;
        state.crkformData.name=formData.mingcheng,
        state.crkformData.refid=formData.id;
        state.crkformData.tablename=tablename;
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
            // state.loadding=true;


               console.log("==============",state.crkformData)

             if(state.crkformData.crkzt=='出库'){
                 
                 if(state.formData.alllimittimes<state.crkformData.sl){
                    notify("出库数量不足",{type:'error'});
                    return;
                 }else{
                    state.loadding=true;
                    state.formData.alllimittimes=state.formData.alllimittimes-state.crkformData.sl;
                     request({
              url:`${state.crkformData.tablename}/update`,
              method:'post',
              data:state.formData
            }).then((data)=>{

                request({
              url:`crk/add`,
              method:'post',
              data:state.crkformData
            }).then((data)=>{
                notify("操作成功",{type:'success'});
              state.loadding=false;
              close();
              emit("refresh");
            })
             
              
            })

                 }
             }else{
                state.loadding=true;
                    state.formData.alllimittimes=Number(state.formData.alllimittimes)+Number(state.crkformData.sl);
                     request({
              url:`${state.crkformData.tablename}/update`,
              method:'post',
              data:state.formData
            }).then(({data})=>{

               
                request({
              url:`crk/add`,
              method:'post',
              data:state.crkformData
            }).then((data)=>{
                notify("操作成功",{type:'success'});
              state.loadding=false;
              close();
              emit("refresh");
            })
            })
             }




        })

    }

    defineExpose({
        open
    })


                    

            


                    


                    


                    


        


</script>

<template>
    <el-dialog :title="`${title}`" v-model="visible"
               center draggable :before-close="close" width="1000px"
               :close-on-click-modal="false" destroy-on-close>
        <div v-loading="loadding">
            <el-form ref="formRef" :model="crkformData"
                     label-width="85px" label-right="right"
                     label-suffix=":" status-icon
            >
                                                                                                            
                        <el-form-item label="名称" prop="name" :rules="{required: true, message: '名称为必填项！', trigger: 'blur'}">
                            <el-input v-model="crkformData.name" maxlength="30" clearable show-word-limit placeholder="请输入名称"/>
                        </el-form-item>
                                                                                                                        
                        <el-form-item label="出入库" prop="crkzt"  :rules="{required: true, message: '为必填项', trigger: 'blur'}">
            <el-select v-model="crkformData.crkzt" placeholder="选择" style="width: 240px">
                  <el-option
                    v-for="item in state.crkzt"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
             </el-select>
          </el-form-item>


                                                        
                        <el-form-item label="数量" prop="sl" :rules="{required: true, message: '出入库数量为必填项！', trigger: 'blur'}">
                            <el-input v-model="crkformData.sl" maxlength="30" clearable show-word-limit placeholder="请输入出入库数量"/>
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
