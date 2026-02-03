<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import base from "@/utils/base";
    import { uploadImg } from '@/api/common/media';
    import request from "@/utils/request";
    import {notify} from '@/utils/element'
    import { Session } from '@/utils/storage';
    const Editor=defineAsyncComponent(()=>import('@/components/editor/index.vue'));
                                                                                                                                                                                                        
            import iconTeam from '@/assets/1.png';
            import AMapLoader from '@amap/amap-jsapi-loader';
            const ruleFormRef=ref();

                                                                                                        const formRef=ref();
    const state=reactive({
        loadding:false,//加载框
        visible:false,//隐藏显示
        roisfalg:{
                                                                            dianpumingcheng: false,
                                                tupian: false,
                                                nicheng: false,
                                                shangjiadianhua: false,
                                                dianpujianjie: false,
                                                dianpudizhi: false,
                                                userid: false,
                                                lat: false,
                                                lnt: false,
                                                conent: false,
                                                sfsh: false,
                                                shhf: false,
                               },
        formData:{} as any,

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        visibledw:false,
                visibles:false,
                ruleForm:{
                    conent:"",
                    x:"",
                    y:""
                },
                list:[],
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,visibledw,
                ruleForm,
                visibles,
                list
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
                                                                                                                                    if (o == 'dianpumingcheng') {
                            state.formData.dianpumingcheng = obj[o];
                            state.roisfalg.dianpumingcheng = true;
                            continue;
                        }
                                                                                if (o == 'tupian') {
                            state.formData.tupian = obj[o];
                            state.roisfalg.tupian = true;
                            continue;
                        }
                                                                                if (o == 'nicheng') {
                            state.formData.nicheng = obj[o];
                            state.roisfalg.nicheng = true;
                            continue;
                        }
                                                                                if (o == 'shangjiadianhua') {
                            state.formData.shangjiadianhua = obj[o];
                            state.roisfalg.shangjiadianhua = true;
                            continue;
                        }
                                                                                if (o == 'dianpujianjie') {
                            state.formData.dianpujianjie = obj[o];
                            state.roisfalg.dianpujianjie = true;
                            continue;
                        }
                                                                                if (o == 'dianpudizhi') {
                            state.formData.dianpudizhi = obj[o];
                            state.roisfalg.dianpudizhi = true;
                            continue;
                        }
                                                                                if (o == 'userid') {
                            state.formData.userid = obj[o];
                            state.roisfalg.userid = true;
                            continue;
                        }
                                                                                if (o == 'lat') {
                            state.formData.lat = obj[o];
                            state.roisfalg.lat = true;
                            continue;
                        }
                                                                                if (o == 'lnt') {
                            state.formData.lnt = obj[o];
                            state.roisfalg.lnt = true;
                            continue;
                        }
                                                                                if (o == 'conent') {
                            state.formData.conent = obj[o];
                            state.roisfalg.conent = true;
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
                url:`dianpuxinxi/${!state.formData.id ? "save" : "update"}`,
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
                    formData.value.tupian = name+'upload/'+ data.file;
                } catch(e) {

                } finally {
                    loadding.value = false;
                }
            }
            


                    


                    


                    


                    


                    


                                function getxy(){

                const params={
                    page: 1,
                    limit:1000,
                }
                request({
                    url:"dianpuxinxi/page",
                    method:"get",
                    params
                }).then(({data})=>{
                    // console.log(data.data);
                    state.list=data.list;
            })
            }

            let map;

            function initmap(){
                AMapLoader.load({
                    key: "637042e311014714fd266be0fae5624a", // 申请好的Web端开发者Key，首次调用 load 时必填
                    version: "1.4.15", // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
                    plugins: [          //需要使用的插件
                        'AMap.ToolBar',
                        'AMap.Scale',
                        'AMap.Geolocation',
                        'AMap.PlaceSearch',
                        'AMap.AutoComplete',
                        'AMap.Geocoder',
                        'AMap.CitySearch',
                        "AMap.Marker"
                    ], //需要使用的的插件列表，如比例尺'AMap.Scale'，支持添加多个如：['...','...']
                })
                        .then((AMap) => {
                    map = new AMap.Map("container", {
                        // 设置地图容器id
                        viewMode: "3D", // 是否为3D地图模式
                        zoom: 18, // 初始化地图级别
                        center: [116.397428, 39.90923], // 初始化地图中心点位置
                    });






                //添加定位功能
                AMap.plugin('AMap.Geolocation', () => {
                    const geolocation = new AMap.Geolocation({
                        enableHighAccuracy: true, // 是否使用高精度定位
                        timeout: 10000, // 定位超时时间
                        buttonPosition:'RB',    //定位按钮的停靠位置
                        buttonOffset: new AMap.Pixel(10, 20),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
                        zoomToAccuracy: true,   //定位成功后是否自动调整地图视野到定位点
                    });

                // 获取当前定位
                geolocation.getCurrentPosition((status, result) => {
                    if (status === 'complete') {
                    const { lng, lat } = result.position;
                    // this.currentLocation = `经度: ${lng}, 纬度: ${lat}`;
                    map.setCenter([lng, lat]); // 将地图中心点设置为当前位置

                    var markerPoint = new AMap.Marker({
                        position: [lng, lat], // 经纬度
                        offset: new AMap.Pixel(-12, -32), // 标记点偏移量
                        // icon: '//vdata.amap.com/icons/b18/1/2.png', // 添加 Icon 图标 URL（不加icon应该有默认标记）
                    })
                    map.add(markerPoint)

                } else {
                    console.error('定位失败:', result.message);
                }
            });
            });


                //    console.log("坐标系",state.list);

                state.list.map((data) => {
                    console.log(data.lat,data.lnt,data.conent)
                const marker = new AMap.Marker({
                    position: new AMap.LngLat(data.lnt,data.lat),
                    title: data.conent, // 鼠标滑过点标记时的文字提示
                    icon: iconTeam, // 引入上面的图片
                    // conent: markerconent.value, // 引入上面HTML要素字符串
                    offset: new AMap.Pixel(-15,-15)
                })
                // 窗口信息
                const infoWindow = new AMap.InfoWindow({
                    isCustom: true, // 自定义窗口,窗口外框以及内容完全按照conent所设的值添加
                    closeWhenClickMap: true, // 是否在鼠标点击地图关闭窗口
                    content: `<div style="background-color:lch(8 12.53 21.29 / 0.2);;width: 80px;height: 80px;border-radius: 6px;line-height: 80px;text-align: center;font-size:12px;">${data.conent}</div>`,
                    offset: new AMap.Pixel(0,-15)
                })
                // 给marker添加click事件
                marker.on("click",(e) => {
                    infoWindow.open(
                        map,
                        // 窗口信息的位置
                        marker.getPosition(data.lnt, data.lat)
                );
            })
                // 给map添加zoomend事件,当缩放级别时触发
                map.on("zoomend",(e) => {
                    // 关闭信息窗体
                    map.clearInfoWindow(infoWindow);
            })
                marker.setMap(map);
            })


                map.on('click', (event) => {
                    // 获取点击的坐标
                    const lng = event.lnglat.getLng();
                const lat = event.lnglat.getLat();
                state.formData.lnt=lng;
                state.formData.lat=lat;
                state.visibles=true;
            })


            })
            .catch((e) => {
                    console.log(e);
            });
            }

            function dwxz(){
                state.visibledw=true;
                getxy();
                initmap();

            }

            function closes(){
                state.visibledw=false;
            }

            function closess(){
                state.visibles=false;
            }


            function submitFormdw(){
                ruleFormRef.value?.validate((valid:boolean)=>{
                    if(!valid) return;
                    state.formData.conent=state.ruleForm.conent;
                    closess();
                    closes();





                })

            }

            


                    


                    


                    


                    


        
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
                                                                                                            
                        <el-form-item label="店铺名称" prop="dianpumingcheng" :rules="{required: true, message: '店铺名称为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.dianpumingcheng" maxlength="30" clearable show-word-limit placeholder="请输入店铺名称" :readonly="roisfalg.dianpumingcheng"/>
                        </el-form-item>
                                                                                                                        

                                                                                <el-form-item label="图片" prop="tupian" :rules="{required: true, message: '为必填项', trigger: 'blur'}">

                            <el-upload
                                    class="avatar-uploader"
                                    accept="image/png,image/jpg,image/jpeg"
                                    action="#"
                                    :show-file-list="false"
                                    :http-request="handleUploadImg"
                            >
                                <img style="width: 100px;height: 100px;" v-if="formData.tupian" :src="formData.tupian" class="avatar" />
                                <el-icon v-else class="avatar-uploader-icon"><ele-Plus /></el-icon>

                            </el-upload>
                        </el-form-item>


                                                        
                        <el-form-item label="昵称" prop="nicheng" :rules="{required: true, message: '昵称为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.nicheng" maxlength="30" clearable show-word-limit placeholder="请输入昵称" :readonly="roisfalg.nicheng"/>
                        </el-form-item>
                                                                                                                        

                                                        
                        <el-form-item label="商家电话" prop="shangjiadianhua" :rules="{required: true, message: '商家电话为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.shangjiadianhua" maxlength="30" clearable show-word-limit placeholder="请输入商家电话" :readonly="roisfalg.shangjiadianhua"/>
                        </el-form-item>
                                                                                                                        

                                                                                <el-form-item label="店铺简介" prop="dianpujianjie">
                            <el-input v-model="formData.dianpujianjie" maxlength="100" clearable show-word-limit type="textarea" />
                        </el-form-item>


                                                        
                        <el-form-item label="店铺地址" prop="dianpudizhi" :rules="{required: true, message: '店铺地址为必填项！', trigger: 'blur'}">
                            <el-input v-model="formData.dianpudizhi" maxlength="30" clearable show-word-limit placeholder="请输入店铺地址" :readonly="roisfalg.dianpudizhi"/>
                        </el-form-item>
                                                                                                                        

                                                                                            
                        <el-form-item label="地图定位" prop="luxian">
                            <el-button @click="dwxz">打开地图</el-button>
                        </el-form-item>
                        <el-form-item label="坐标x" prop="lnt" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                            <el-input readonly="true" v-model="formData.lnt" maxlength="30" clearable show-word-limit placeholder="请输入标题" />
                        </el-form-item>
                        <el-form-item label="坐标y" prop="lat" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                            <el-input readonly="true" v-model="formData.lat" maxlength="30" clearable show-word-limit  />
                        </el-form-item>
                        <el-form-item  label="介绍" prop="conent" :rules="{required: true, message: '为必填项！', trigger: 'blur'}">
                            <el-input readonly="true" v-model="formData.conent" maxlength="30" clearable show-word-limit  />
                        </el-form-item>
                                                                                                                                                                                    


                
            </el-form>
            <el-row justify="center" class="mt10">
                <el-button @click="close">取 消</el-button>
                <el-button @click="submitForm" type="primary">保 存</el-button>
            </el-row>
        </div>
    </el-dialog>

            
            
            
            
            
            
            
            
            
                        <el-dialog :title="`定位`" v-model="visibledw"
                       center draggable :before-close="closes" width="1000px"
                       :close-on-click-modal="false" destroy-on-close align-center>
                <div id="container" class="mapDisplay"></div>
            </el-dialog>


            <el-dialog :title="`填写名称`" v-model="visibles"
                       center draggable :before-close="closess"
                       :close-on-click-modal="false" destroy-on-close align-center>

                <el-form
                        ref="ruleFormRef"
                        :model="ruleForm"
                        status-icon
                        label-width="auto"
                        class="demo-ruleForm"
                >
                    <el-form-item label="定位名称" prop="conent" :rules="{required: true, message: '定位名称为必填项！', trigger: 'blur'}">
                        <el-input v-model.number="ruleForm.conent" />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" v-loading="loadding" @click="submitFormdw()" >
                            确认
                        </el-button>
                        <el-button @click="closess()">取消</el-button>
                    </el-form-item>
                </el-form>



            </el-dialog>
        
            
            
            
            
    

</template>

<style lang="scss" scoped>


                                                                                                                                                                                                        
            #container{
                width: 100%;
                height: 600px;
            }

                                                                                                    
</style>
