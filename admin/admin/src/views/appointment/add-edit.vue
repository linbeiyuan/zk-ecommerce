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
               url:`appointment/${!state.formData.id ? "save" : "update"}`,
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