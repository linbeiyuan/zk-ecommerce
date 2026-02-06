<script setup lang="ts">
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import { uploadImg } from '@/api/common/media';
    import base from "@/utils/base";
    import { defineAsyncComponent,reactive,ref,toRefs,nextTick } from 'vue';
    import {notify,confirm} from '@/utils/element';
    import {useRoute,useRouter} from 'vue-router'
    import {geren} from '@/utils/menu';
    const router = useRouter();
    const menus=geren.list();
    // console.log("个人菜单",menus)
    const grmenu=[];
    const grmenuesc=[];
 menus.forEach((item)=>{
          item.ykMenu.forEach((i)=>{
            // console.log("个人中心",i.child);
            i.child.forEach((a)=>{
                // console.log(a.tableName)
                grmenuesc.push(a.tableName);
            })
             grmenu.push(i.menu)
          });
     })
                const addORupdate=defineAsyncComponent(()=>import('@/views/address/add-update.vue'));
                        const forumAddORupdate=defineAsyncComponent(()=>import('@/views/forum/add-update.vue'));
                    const state=reactive({
                gr:grmenu,
        gresc:grmenuesc,
                                                                                                                                                                                        ruleForm: {

        },
        formInline: {},
        dataList: [],

        user:{},
                    addresspage:{
                current:1,
                size:10,
                total:0,
            },
            statuslist:['未支付','已支付','已发货','已退款','已完成'],
            orderspage:{
                current:1,
                size:10,
                total:0,
            },
            ordersList:[],
            formorders:{},
            type:'',
            zjzfTableVisible:false,
            czmoney:0,
                            forumpage:{
                current:1,
                size:10,
                total:0,
            },
            forumList:[],
            forumsearchForm:{},
                
        
    })


    const {dataList,ordersList,ruleForm,gr,gresc,
                                    addresspage,
            statuslist,
            formorders,
            orderspage,
            zjzfTableVisible,
            type,
            user,
            czmoney,
                                                                                                                                                                                
                    forumpage,
            forumList,
            forumsearchForm,
                formInline,
        
        

    } = {...toRefs(state)};




    init();

                setTimeout(()=>{
            getaddress();
        getorders();
        },300)

        
        
        
    function init(){
        let sessionTable = Session.get("tableName")
        request({
            url: sessionTable + '/session',
            method: "get"
        }).then((
                data
        ) => {
            if (data && data.code === 0) {

            state.user = data.data;
            state.ruleForm=data.data;

        } else {
            notify(data.msg,{type:'error'});
        }
    });
    }



                function zf(){
            state.zjzfTableVisible=true;
        }
        function gozf(){

            if (!state.type) {
                notify('请选择支付方式',{type:'error'});
                return;
            }
            if (state.czmoney==0) {
                notify('请填写充值金额',{type:'error'});
                return;
            }
            confirm("确认清楚您当前的余额是否正确？").then(()=>{
                let sessionTable = Session.get("tableName");

            let money=state.user.money;
            money=Number(state.czmoney)+Number(money);
            state.user.money=Number(money);
            request({
                url:`${sessionTable}/${!state.user.id ? "save" : "update"}`,
                method:'post',
                data:state.user
            }).then((data)=>{
                notify("充值成功",{type:'success'});
            state.zjzfTableVisible=false;
        })


        })
        }
                function search() {

            getaddress();
        }


        function getaddress(){
            let params = {
                page: state.addresspage.current,
                limit: state.addresspage.addresspageSize,
                sort: 'id',
                userid:state.user.id
            }
            if (state.formInline.name != '' && state.formInline.name != undefined) {
                params['name'] = '%' + state.formInline.name + '%'
            }
            if (state.formInline.phone != '' && state.formInline.phone != undefined) {
                params['phone'] = '%' + state.formInline.phone + '%'
            }

            request({
                url:`address/list`,
                method:'get',
                params
            }).then((data) => {
                if (data && data.code === 0) {
                // console.log(data)
                state.dataList = data.data.list;
                state.addresspage.total = data.data.total;
            } else {
                state.dataList = [];
                state.addresspage.total = 0;
            }
            state.dataListLoading = false;
        });
        }


        const addressupref=ref();

        function add(){

            console.log(1111)
            var title='新增';
            var type='add';
            var item={};
            item.id=0


            addressupref.value.openaddOrupdate(title,item,type);
            ;
        }
        function update(item){
            var title='修改';
            var type='update';

            addressupref.value.openaddOrupdate(title,item,type);

        }



        function  handleDelete(row){

            confirm("此操作将永久删除该信息吗, 是否继续?").then(()=>{
                request({
                            url:`address/delete`,
                    method:'post',
                    data:[row.id]
        }).then((data) => {
                if (data && data.code === 0) {
                notify("删除成功",{type:'success'});

                getaddress();

            } else {
                notify(data.msg,{type:'error'});
            }
        });
        })


        }



        //我的订单

        function getorders(){
            let params = {
                page: state.orderspage.current,
                limit: state.orderspage.size,
                sort: 'id',
                userid:state.user.id

            }

            if (state.formorders.orderid != '' && state.formorders.orderid != undefined) {
                params['orderid'] = '%' + state.formorders.orderid + '%'
            }
            if (state.formorders.status != '' && state.formorders.status != undefined) {
                params['status'] = '%' + state.formorders.status + '%'
            }




            request({
                url:`orders/list`,
                method:'get',
                params
            }).then((data) => {
                if (data && data.code === 0) {
                state.ordersList = data.data.list;
                state.orderspage.total = data.data.total;
            } else {
                state.ordersList = [];
                state.orderspage.total = 0;
            }
            state.dataListLoading = false;
        });
        }


        function searchorders(){
            getorders();
        }

        //支付
        function pay(item){
            request({
                url:`${item.tablename}/info/${item.goodid}`,
                method:'get'
            }).then(({data})=>{
                let goods=data.data;


            if (state.user.money < item.total) {
                notify("余额不足，请充值",{type:'error'});
                return
            }
            if (data.jifen) {
                state.user.jifen = Number(state.user.jifen) + Number(goods.jifen * item.buynumber);
            }
            state.user.money = state.user.money - item.total;
            let sessionTable = Session.get("tableName")
            request({
                url:`${sessionTable}/update`,
                method:'post',
                data:state.user
            }).then(({data})=>{
                item.status = '已支付'
            request({
                url:`orders/update`,
                method:'post',
                data:item
            }).then(({data})=>{

                notify("支付成功",{type:'success'});

            getorders();
        })
        })


        })
        }

        //退款
        function refund(item){

            request({
                url:`${item.tablename}/info/${item.goodid}`,
                method:'get'
            }).then(({data})=>{

                if (data.jifen) {
                state.user.jifen = Number(state.user.jifen) - Number(data.jifen * item.buynumber);
            }


            state.user.money = state.user.money + item.total;
            let sessionTable = Session.get("tableName")
            request({
                url:`${sessionTable}/update`,
                method:'post',
                data:state.user
            }).then((data)=>{
                item.status = '已退款'
            request({
                url:`orders/update`,
                method:'post',
                data:item
            }).then(({data})=>{
                notify("退款成功",{type:'success'});

            getorders();
        })
        })
        })



        }

        //收货

        function upconfirm(item){
            item.status='已完成'
        request({
            url:`orders/update`,
            method:'post',
            data:item
        }).then(({data})=>{



            
                let sessionTable = Session.get("tableName")
                //重新获取用户信息，得到最新的积分数
                request({
                            url: sessionTable + '/session',
                    method: "get"
            }).then((
                    data
            ) => {
                if (data && data.code === 0) {
                state.user = data.data;

            } else {

                notify(data.msg,{type:'error'});
            }
            });

                state.user.jf=state.user.jf+10;
                request({
                    url:`${sessionTable}/update`,
                    method:'post',
                    data: state.user
                }).then((data)=>{
                    notify("收货成功",{type:'success'});
            })




            



            getorders();
        })
        }

        function del(item){
            request({
                url:`orders/delete/`,
                method:'post',
                data:[item.id]
            }).then(({data})=>{
                notify("删除成功",{type:'success'});

            getorders();
        })
        }
           
    const formRef=ref();
    const loadding=ref(false);

    // 提交
    function onSubmit() {
        let sessionTable = Session.get("tableName")
        formRef.value?.validate((valid)=>{

            if(!valid) return;

        request({
            url:`${sessionTable}/${!state.ruleForm.id ? "save" : "update"}`,
            method:'post',
            data:state.ruleForm
        }).then((data)=>{
            notify("操作成功",{type:'success'});
            init();
    })
    })

    }
        setTimeout(()=>{
  getforumlist();
},300)
    
                const forumupref=ref();

        function getforumlist(){
            var params={
                page: state.forumpage.current,
                limit: state.forumpage.size,
                parentid:'0'
            }
            if (state.forumsearchForm.title != '' && state.forumsearchForm.title != undefined) {
                params['title'] = '%' + state.forumsearchForm.title + '%'
            }
            request({
                url:'forum/page?sort=addtime&order=desc',
                method:'get',
                params
            }).then((data)=>{
                state.forumList=data.data.list;
            state.forumpage.total=data.data.total
        })
        }




        function addforum(){
            var type='add';
            var title='新增';
            var item={};
            item.id=0

            forumupref.value.openaddOrupdate(title,item,type);


        }


        function updateforum(item){
            var type='up';
            var title='修改';
            forumupref.value.openaddOrupdate(title,item,type);

        }

        function delforum(item){
            confirm('此操作将永久删除该信息吗, 是否继续?').then(() => {

                request({
                            url:'forum/delete',
                            method:'post',
                            data:[item.id]
                        }).then((data) => {
                if (data && data.code === 0) {

                notify("操作成功",{type:'success'});


                getforumlist();

            } else {
                notify(data.msg,{type:'error'});
            }
        })






        })
        }

        function forumsearch(){
            getforumlist();
        }

        

        
                    
                    
                    
                    
                    
                    
                    
                    
        
function handleClick(tab:any){
    console.log(tab.props.name)
    if(tab.props.name){
        // 特殊处理优惠券路由
        if(tab.props.name === 'coupon') {
            router.push('/coupon')
        } else {
            router.push(`/${tab.props.name}list`)
        }
    }
}

        
        </script>



<template>
  <div class="profile-page">
    <div class="profile-container">
      <div class="profile-header">
        <h1 class="profile-header-title">个人中心</h1>
      </div>

      <div class="profile-tabs">
        <el-tabs type="border-card" @tab-click="handleClick">
                    <el-tab-pane label="我要充值">
        <div class="balance-card">
            <div class="balance-info">
                我的余额：
                <span class="balance-amount">¥{{ user.money || 0 }}</span>
            </div>
            <el-button type="success" size="large" @click="zf()">我要充值</el-button>
        </div>
    </el-tab-pane>

    
                            <el-tab-pane label="收货地址">
                    <el-card class="box-card">
                        <el-form :inline="true" :model="formInline" class="demo-form-inline">
                            <el-form-item>
                                <el-input v-model="formInline.phone" placeholder="联系方式"></el-input>
                            </el-form-item>
                            <el-form-item>
                                <el-input v-model="formInline.name" placeholder="收货人"></el-input>
                            </el-form-item>

                            <el-form-item>
                                <el-button type="primary" @click="search()">查询</el-button>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="success" @click="add()">新增</el-button>
                            </el-form-item>
                        </el-form>
                        <el-table
                                :data="dataList"
                                border
                                style="width: 100%" height="500">
                            <el-table-column
                                    fixed
                                    prop="addtime"
                                    label="日期">
                            </el-table-column>
                            <el-table-column
                                    prop="name"
                                    label="姓名">
                            </el-table-column>
                            <el-table-column
                                    prop="phone"
                                    label="电话">
                            </el-table-column>
                            <el-table-column
                                    prop="address"
                                    label="地址">
                            </el-table-column>

                            <el-table-column
                                    prop="zip"
                                    label="操作">


                                <template #default="{row}">
                                    <el-button
                                            size="mini"
                                            @click="update(row)">编辑</el-button>
                                    <el-button
                                            size="mini"
                                            type="danger"
                                            @click="handleDelete(row)">删除</el-button>
                                </template>
                            </el-table-column>

                        </el-table>

                        <m-page :page="addresspage" @pageChange="getaddress"/>

                    </el-card>


                </el-tab-pane>


            

            
                <el-tab-pane label="我的订单"><el-card class="box-card">
                    <el-form :inline="true" :model="formorders" class="demo-form-inline">
                        <el-form-item>
                            <el-input v-model="formorders.orderid" placeholder="订单编号"></el-input>
                        </el-form-item>
                        <el-form-item label="">
                            <el-select style="width: 200px;" v-model="formorders.status" placeholder="订单状态" clearable >
                                <el-option v-for="(item,index) in statuslist" :label="item" :value="item" :key="index"></el-option>

                            </el-select>
                        </el-form-item>

                        <el-form-item>
                            <el-button type="primary" @click="searchorders()">查询</el-button>
                        </el-form-item>

                    </el-form>


                    <el-table
                            :data="ordersList"
                            border
                            style="width: 100%"   height="600"

                    >
                        <el-table-column
                                fixed
                                prop="addtime"
                                label="日期">
                        </el-table-column>
                        <el-table-column
                                prop="orderid"
                                label="订单编号">
                        </el-table-column>
                        <el-table-column
                                prop="goodname"
                                label="商品名称">
                        </el-table-column>
                        <el-table-column
                                prop="picture"
                                label="图片">

                            <template #default="{row}">

                                <img :src="row.picture" style="width:50px;height: 50px;" alt="">

                            </template>
                        </el-table-column>
                        <el-table-column
                                prop="buynumber"
                                label="数量">
                        </el-table-column>
                        <el-table-column
                                prop="price"
                                label="单价">
                        </el-table-column>
                        <el-table-column
                                prop="total"
                                label="总价格">
                        </el-table-column>
                        <el-table-column
                                prop="status"
                                label="订单状态">
                        </el-table-column>
                        <el-table-column
                                prop="address"
                                label="收获地址">
                        </el-table-column>

                        <el-table-column
                                prop="type"
                                label="订单类型">
                            <template #default="{row}">

                                <el-tag v-if="row.type==2" type="danger">积分订单</el-tag>
                                <el-tag v-if="row.type==1" type="danger">正常订单</el-tag>
                            </template>

                        </el-table-column>
                        <el-table-column
                                prop="zip"
                                label="操作">


                            <template #default="{row}">
                                <el-button v-if="row.status=='未支付'"
                                           size="mini" type="primary"
                                           @click="pay(row)">支付</el-button>

                                <el-tag style="padding-right:20px"  v-if="row.status=='已支付'" type="danger">未发货</el-tag>

                                <el-button v-if="row.status=='已发货'"
                                           size="mini" type="success"
                                           @click="upconfirm(row)">收货</el-button>
                                <el-tag style="padding-right:20px"  v-if="row.status=='已完成'" type="success">已完成</el-tag>
                                <el-tag style="padding-right:20px"  v-if="row.status=='已退款'" type="danger">已退款</el-tag>
                                <el-button
                                        size="mini"  v-if="(row.status=='已支付' || row.status=='未发货' || row.status=='已发货') && row.type==1  "
                                        type="danger"
                                        @click="refund(row)">退款</el-button>
                                <el-button
                                        size="mini"  v-if="row.status=='未支付' "
                                        type="danger"
                                        @click="del(row)">删除</el-button>
                            </template>
                        </el-table-column>

                    </el-table>







                    <m-page :page="orderspage" @pageChange="getorders"/>


                </el-card>
                </el-tab-pane>


            
            
                <el-tab-pane label="我的发布">

                    <el-card>

                        <el-form :inline="true" :model="forumsearchForm" class="demo-form-inline">
                            <el-form-item >
                                <el-input v-model="forumsearchForm.title" placeholder="标题"></el-input>
                            </el-form-item>

                            <el-form-item>
                                <el-button type="primary" @click="forumsearch()">查询</el-button>
                                <el-button type="success" @click="addforum()">发布</el-button>
                            </el-form-item>

                        </el-form>

                        <el-table
                                :data="forumList"
                                style="width: 100%"
                                height="450">
                            <el-table-column
                                    fixed
                                    prop="title"
                                    label="标题"
                            >
                            </el-table-column>
                            <el-table-column
                                    prop="addtime"
                                    label="发布时间"
                            >
                            </el-table-column>
                            <el-table-column
                                    prop="isdone"
                                    label="发布类型"
                            >
                            </el-table-column>


                            <el-table-column label="操作">

                                <template  #default="{row}">
                                    <el-button
                                            size="mini"
                                            @click="updateforum(row)">编辑</el-button>
                                    <el-button
                                            size="mini"
                                            type="danger"
                                            @click="delforum(row)">删除</el-button>
                                </template>

                            </el-table-column>
                        </el-table>





                        <m-page :page="forumpage" @pageChange="getforumlist"/>





                    </el-card>



                </el-tab-pane>

            


            

            

            
<el-tab-pane :label="item" v-for="(item,index) in gr" :name="gresc[index]">

            </el-tab-pane>


            <el-tab-pane label="修改个人信息">
                <div class="profile-form-container">
                    <el-form
                            ref="formRef" :model="ruleForm"
                            label-width="100px" label-suffix=":" status-icon
                    >
                        <el-row>




                                                                                                                                                                                    


                                    <el-col :span="24">
                                        <el-form-item class="input" label="用户名" prop="yonghuming"  :rules="{required: true, message: '用户名为必填项！', trigger: 'blur'}" >
                                            <el-input v-model="ruleForm.yonghuming"
                                                      placeholder="用户名" clearable></el-input>
                                        </el-form-item>
                                    </el-col>
                                                                                            


                                    <el-col :span="24">
                                        <el-form-item class="input" label="密码" prop="mima"  :rules="{required: true, message: '密码为必填项！', trigger: 'blur'}" >
                                            <el-input v-model="ruleForm.mima"
                                                      placeholder="密码" clearable></el-input>
                                        </el-form-item>
                                    </el-col>
                                                                                            


                                    <el-col :span="24">
                                        <el-form-item class="input" label="手机号" prop="shoujihao"  :rules="{required: true, message: '手机号为必填项！', trigger: 'blur'}" >
                                            <el-input v-model="ruleForm.shoujihao"
                                                      placeholder="手机号" clearable></el-input>
                                        </el-form-item>
                                    </el-col>
                                                                                            


                                    <el-col :span="24">
                                        <el-form-item class="input" label="地址" prop="dizhi"  :rules="{required: true, message: '地址为必填项！', trigger: 'blur'}" >
                                            <el-input v-model="ruleForm.dizhi"
                                                      placeholder="地址" clearable></el-input>
                                        </el-form-item>
                                    </el-col>
                                                                                                                                                                                    

















                        </el-row>
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit">提交</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-tab-pane>


        </el-tabs>
      </div>
    </div>
  </div>

            <addORupdate @refresh="getaddress" ref="addressupref"></addORupdate>
                <forumAddORupdate @refresh="getforumlist" ref="forumupref"></forumAddORupdate>
        <el-dialog v-model="zjzfTableVisible" title="支付" width="800">
        <div class="pay-dialog-content">
            <el-alert title="确认支付前请先核对个人余额是否正确" type="success" :closable="false"></el-alert>

            <div class="pay-type-content">
                <div class="pay-type-item" @click="type = '微信支付'">
                    <el-radio v-model="type" label="微信支付"></el-radio>
                    <img src="@/assets/img/test/weixin.png">
                </div>
                <div class="pay-type-item" @click="type = '支付宝支付'">
                    <el-radio v-model="type" label="支付宝支付"></el-radio>
                    <img src="@/assets/img/test/zhifubao.png">
                </div>
                <div class="pay-type-item" @click="type = '建设银行'">
                    <el-radio v-model="type" label="建设银行"></el-radio>
                    <img src="@/assets/img/test/jianshe.png">
                </div>
                <div class="pay-type-item" @click="type = '农业银行'">
                    <el-radio v-model="type" label="农业银行"></el-radio>
                    <img src="@/assets/img/test/nongye.png">
                </div>
                <div class="pay-type-item" @click="type = '中国银行'">
                    <el-radio v-model="type" label="中国银行"></el-radio>
                    <img src="@/assets/img/test/zhongguo.png">
                </div>
                <div class="pay-type-item" @click="type = '交通银行'">
                    <el-radio v-model="type" label="交通银行"></el-radio>
                    <img src="@/assets/img/test/jiaotong.png">
                </div>
            </div>

            <div class="pay-input">
                <el-input v-model="czmoney" placeholder="输入充值金额" size="large" type="number"></el-input>
            </div>

            <div class="pay-button-content">
                <el-button type="primary" size="large" @click="gozf()">确认支付</el-button>
            </div>
        </div>
    </el-dialog>


</template>

<style scoped>
.profile-form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>
