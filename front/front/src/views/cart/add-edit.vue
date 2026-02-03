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
        roisfalg:{
                                                                            tablename: false,
                                                userid: false,
                                                goodid: false,
                                                goodname: false,
                                                picture: false,
                                                buynumber: false,
                                                price: false,
                                                discountprice: false,
                               },
        formData:{} as any,

                                                                                                                                                                                                                                                                                                                                                                                                                                        title:'新增',
        type:'add',
        id:''
    })
    const initData={

    }
    const {
        loadding,
        visible,
        formData,
        title,
        type,
        id,
        roisfalg
                                                                                                                                                                                                                                                                                                                                                                                                                                    } = {...toRefs(state)};


    function open(title:string,id:any,type:string,formData?:any)
    {

        state.title = title;
        state.type = type;
        state.id = id;
        state.formData = {...formData,...initData }
        ;
        state.visible = true;
        if (state.type == 'cross') {
            var obj = Session.get('crossObj');
            for (var o in obj) {
                                                                                                                                    if (o == 'tablename') {
                            state.formData.tablename = obj[o];
                            state.roisfalg.tablename = true;
                            continue;
                        }
                                                                                if (o == 'userid') {
                            state.formData.userid = obj[o];
                            state.roisfalg.userid = true;
                            continue;
                        }
                                                                                if (o == 'goodid') {
                            state.formData.goodid = obj[o];
                            state.roisfalg.goodid = true;
                            continue;
                        }
                                                                                if (o == 'goodname') {
                            state.formData.goodname = obj[o];
                            state.roisfalg.goodname = true;
                            continue;
                        }
                                                                                if (o == 'picture') {
                            state.formData.picture = obj[o];
                            state.roisfalg.picture = true;
                            continue;
                        }
                                                                                if (o == 'buynumber') {
                            state.formData.buynumber = obj[o];
                            state.roisfalg.buynumber = true;
                            continue;
                        }
                                                                                if (o == 'price') {
                            state.formData.price = obj[o];
                            state.roisfalg.price = true;
                            continue;
                        }
                                                                                if (o == 'discountprice') {
                            state.formData.discountprice = obj[o];
                            state.roisfalg.discountprice = true;
                            continue;
                        }
                                                }


        }
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
                url:`cart/${!state.formData.id ? "save" : "update"}`,
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


                                                                                                                                                                                                                
</style>
