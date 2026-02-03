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
                                                                            shangpinmingcheng: false,
                                                shangpintupian: false,
                                                fenleimingcheng: false,
                                                jieshao: false,
                                                xiangqing: false,
                                                dianpumingcheng: false,
                                                userid: false,
                                                price: false,
                                                onelimittimes: false,
                                                alllimittimes: false,
                                                sfsh: false,
                                                shhf: false,
                                                thumbsupnum: false,
                                                crazilynum: false,
                               },
        formData:{} as any,

                                                                                                                        fenleimingchengOptions: [],
                                                                                            dianpumingchengOptions: [],
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
                                                                                                                    , fenleimingchengOptions
                                                                                        , dianpumingchengOptions
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
                                                                                                                                    if (o == 'shangpinmingcheng') {
                            state.formData.shangpinmingcheng = obj[o];
                            state.roisfalg.shangpinmingcheng = true;
                            continue;
                        }
                                                                                if (o == 'shangpintupian') {
                            state.formData.shangpintupian = obj[o];
                            state.roisfalg.shangpintupian = true;
                            continue;
                        }
                                                                                if (o == 'fenleimingcheng') {
                            state.formData.fenleimingcheng = obj[o];
                            state.roisfalg.fenleimingcheng = true;
                            continue;
                        }
                                                                                if (o == 'jieshao') {
                            state.formData.jieshao = obj[o];
                            state.roisfalg.jieshao = true;
                            continue;
                        }
                                                                                if (o == 'xiangqing') {
                            state.formData.xiangqing = obj[o];
                            state.roisfalg.xiangqing = true;
                            continue;
                        }
                                                                                if (o == 'dianpumingcheng') {
                            state.formData.dianpumingcheng = obj[o];
                            state.roisfalg.dianpumingcheng = true;
                            continue;
                        }
                                                                                if (o == 'userid') {
                            state.formData.userid = obj[o];
                            state.roisfalg.userid = true;
                            continue;
                        }
                                                                                if (o == 'price') {
                            state.formData.price = obj[o];
                            state.roisfalg.price = true;
                            continue;
                        }
                                                                                if (o == 'onelimittimes') {
                            state.formData.onelimittimes = obj[o];
                            state.roisfalg.onelimittimes = true;
                            continue;
                        }
                                                                                if (o == 'alllimittimes') {
                            state.formData.alllimittimes = obj[o];
                            state.roisfalg.alllimittimes = true;
                            continue;
                        }
                                                                                if (o == 'sfsh') {
                            state.formData.sfsh = obj[o];
                            state.roisfalg.sfsh = true;
                            continue;
                        }
                                                                                if (o == 'shhf') {
                            state.formData.shhf = obj[o];
                            state.roisfalg.shhf = true;
                            continue;
                        }
                                                                                if (o == 'thumbsupnum') {
                            state.formData.thumbsupnum = obj[o];
                            state.roisfalg.thumbsupnum = true;
                            continue;
                        }
                                                                                if (o == 'crazilynum') {
                            state.formData.crazilynum = obj[o];
                            state.roisfalg.crazilynum = true;
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
                url:`shangpinguanli/${!state.formData.id ? "save" : "update"}`,
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
                    formData.value.shangpintupian = name+'upload/'+ data.file;
                } catch(e) {

                } finally {
                    loadding.value = false;
                }
            }
            


                                                        
                    request({
                        url: `option/shangpinfenlei/fenleimingcheng`,
                        method: "get"
                    }).then((data) => {
                        if (data && data.code === 0) {
                        state.fenleimingchengOptions = data.data;
                    } else {
                        notify(data.msg,{type:'error'});
                    }
                    });
                                                        
            


                    


                    


                                                        
                    request({
                        url: `option/dianpuxinxi/dianpumingcheng`,
                        method: "get"
                    }).then((data) => {
                        if (data && data.code === 0) {
                        state.dianpumingchengOptions = data.data;
                    } else {
                        notify(data.msg,{type:'error'});
                    }
                    });
                                                        
            


                    


                    


                    


                    


                    


                    


                    


                    


        
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
                                                                                                            
                        <el-form-item label="商品名称" prop="shangpinmingcheng" :rules="{required: true, message: '商品名称为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.shangpinmingcheng" maxlength="30" clearable show-word-limit placeholder="请输入商品名称" :readonly="roisfalg.shangpinmingcheng"/>
                        </el-form-item>
                                                                                                                        

                                                                                <el-form-item label="商品图片" prop="shangpintupian" :rules="{required: true, message: '为必填项', trigger: 'blur'}">

                            <el-upload
                                    class="avatar-uploader"
                                    accept="image/png,image/jpg,image/jpeg"
                                    action="#"
                                    :show-file-list="false"
                                    :http-request="handleUploadImg"
                            >
                                <img style="width: 100px;height: 100px;" v-if="formData.shangpintupian" :src="formData.shangpintupian" class="avatar" />
                                <el-icon v-else class="avatar-uploader-icon"><ele-Plus /></el-icon>

                            </el-upload>
                        </el-form-item>


                                                                                <el-form-item label="分类名称" prop="fenleimingcheng" :rules="{required: true, message: '分类名称为必选项！', trigger: 'blur'}">
                            <el-select
                                    v-model="formData.fenleimingcheng"
                                    clearable
                                    placeholder="请选择分类名称"
                                    style="width: 240px"
                            >
                                <el-option
                                        v-for="(item,index) in fenleimingchengOptions"
                                        v-bind:key="index"
                                        :label="item"
                                        :value="item"
                                />
                            </el-select>
                        </el-form-item>

                                                                                <el-form-item label="介绍" prop="jieshao">
                            <el-input v-model="formData.jieshao" maxlength="100" clearable show-word-limit type="textarea" />
                        </el-form-item>


                                                                                <el-form-item label="详情" prop="xiangqing">

                            <Editor v-model="formData.xiangqing"/>

                        </el-form-item>

                                                                                <el-form-item label="店铺名称" prop="dianpumingcheng" :rules="{required: true, message: '店铺名称为必选项！', trigger: 'blur'}">
                            <el-select
                                    v-model="formData.dianpumingcheng"
                                    clearable
                                    placeholder="请选择店铺名称"
                                    style="width: 240px"
                            >
                                <el-option
                                        v-for="(item,index) in dianpumingchengOptions"
                                        v-bind:key="index"
                                        :label="item"
                                        :value="item"
                                />
                            </el-select>
                        </el-form-item>

                                                                                            
                        <el-form-item label="价格" prop="price" :rules="{required: true, message: '价格为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.price" maxlength="30" clearable show-word-limit placeholder="请输入价格" :readonly="roisfalg.price"/>
                        </el-form-item>
                                                                                                                        

                                                        
                        <el-form-item label="单限" prop="onelimittimes" :rules="{required: true, message: '单限为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.onelimittimes" maxlength="30" clearable show-word-limit placeholder="请输入单限" :readonly="roisfalg.onelimittimes"/>
                        </el-form-item>
                                                                                                                        

                                                        
                        <el-form-item label="库存" prop="alllimittimes" :rules="{required: true, message: '库存为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.alllimittimes" maxlength="30" clearable show-word-limit placeholder="请输入库存" :readonly="roisfalg.alllimittimes"/>
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


                                                                                                                                                                                                                                                                                                                                        
</style>
