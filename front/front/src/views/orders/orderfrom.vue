<template>

    <el-dialog title="" v-model="open"  :append-to-body="true">

        <div class="container">
            <h1>订单提交</h1>
            <div id="paymentForm">
                <div class="address-section">



                </div>
                <div class="address-section">

                    <div>
                        <label for="paymentMethod">选择地址：</label>
                        <el-select v-model="value" clearable placeholder="请选择" @change="dzxz(value)" style="width: 600px;">
                            <el-option
                                    v-for="item in addressList"
                                    :key="item.id"
                                    :label="(item.address+','+item.name+','+item.phone)"
                                    :value="(item.address+','+item.name+','+item.phone)">
                            </el-option>
                        </el-select>

                    </div>

                </div>
                <h2>商品列表</h2>
                <table>
                    <thead>
                    <tr>
                        <th>商品名称</th>
                        <th>单价</th>
                        <th>数量</th>
                        <th>小计</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(item,index) in dataList" :key="index">
                        <td>{{ item.goodname }}</td>
                        <td>¥{{item.price}}</td>
                        <td>{{item.buynumber}}</td>
                        <td>¥{{item.buynumber*item.price}}</td>
                    </tr>

                    </tbody>
                    <tfoot>
                    <tr v-if="selectedCoupon">
                        <td colspan="3" style="text-align: right;">商品总计</td>
                        <td>¥{{totalPrice}}</td>
                    </tr>
                    <tr v-if="selectedCoupon">
                        <td colspan="3" style="text-align: right; color: #ff6b6b;">优惠券</td>
                        <td style="color: #ff6b6b;">-¥{{selectedCoupon.discount_amount}}</td>
                    </tr>
                    <tr>
                        <td colspan="3" style="text-align: right; font-weight: bold;">总价</td>
                        <td style="font-weight: bold; color: #ff6b6b;">¥{{finalPrice}}</td>
                    </tr>
                    </tfoot>
                </table>
                <div class="form-group">
                    <button type="button" @click="payClick()">提交订单</button>
                </div>
            </div>
        </div>

    </el-dialog>
</template>

<script setup>


    import { defineAsyncComponent,reactive,ref,toRefs,computed } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify,confirm} from '@/utils/element';
    import { isAuth } from '@/utils/utils'


    const state=reactive({
        open:false,
        user:{},
        dataList:[],
        addressList:[],
        ismo:1,
        value:'',
        address:'',
        orderId:[],
        flag:true,
        orders:{},
        totalPrice:0,
        selectedCoupon:null
    });

    const {open,user,dataList,addressList,ismo,value,address,orderId,flag,orders,totalPrice,selectedCoupon} = {...toRefs(state)};


    state.totalPrice=computed(()=>{
        state.total=0;

    for (var item of state.dataList) {

        state.total += item.price * item.buynumber
    }
    return state.total;
    })

    // 计算实付金额
    const finalPrice = computed(() => {
        if (state.selectedCoupon) {
            return Math.max(0, state.totalPrice - state.selectedCoupon.discount_amount)
        }
        return state.totalPrice
    })




    let sessionTable = Session.get("tableName")

    request({
        url: sessionTable + '/session',
        method: "get"
    }).then((data) => {
        if (data && data.code === 0) {
        state.user = data.data;

    } else {
        notify(data.msg,{type:'error'});
    }
    });


    function openordersinit(coupon){

        state.open=true;
        state.selectedCoupon = coupon;
        getlist();
        getaddress();
        state.orderId.splice(0, state.orderId.length);
        console.log("数组："+state.orderId)
    }


    function getlist(){
        request({
            url:"cart/list",
            method:'get',
            params:{
                page: 1,
                limit: 100,
                userid: state.user.id
            }
        }).then((data) => {
            if (data && data.code === 0) {
            state.dataList = data.data.list;


        } else {
            notify(data.msg,{type:'error'});
        }
    })
    }


    function getaddress(){
        request({
            url:"address/list",
            method:'get',
            data:{
                userid:state.user.id
            }
        }).then((data) => {
            if (data && data.code === 0) {
            state.addressList = data.data.list;


        } else {
            notify(data.msg,{type:'error'});
        }
    })
    }



    function dzxz(val){
        state.address=val;
    }


    function payClick(){

        if(state.address==''){
            notify("请选择收货地址",{type:'error'});
            return
        }



        for (let [index,item] of state.dataList.entries()) {

            state.orderId.push(genTradeNo());
            console.log(state.orderId)

            //查询商品
            request({
                url:`${item.tablename}/info/${item.goodid}`,
                method:'get'
            }).then((data) => {
                if (data && data.code === 0) {

                // let data = data.data;
                data.data.alllimittimes = data.data.alllimittimes - item.buynumber;

                //减少库存
                request({
                    url:`${item.tablename}/update`,
                    method:'post',
                    data: data.data
                }).then((data) => {
                    if (data && data.code === 0) {

                    // 添加订单信息
                    state.orders= {
                        orderid: state.orderId[index],
                        tablename: item.tablename,
                        userid: state.user.id,
                        goodid: item.goodid,
                        goodname: item.goodname,
                        picture: item.picture,
                        buynumber: item.buynumber,
                        discountprice: item.price,
                        price: item.price,
                        total: finalPrice.value,
                        discounttotal: finalPrice.value,
                        type: 1,
                        address: state.address,
                        status: '未支付',
                        coupon_id: state.selectedCoupon ? state.selectedCoupon.id : null,
                        coupon_discount: state.selectedCoupon ? state.selectedCoupon.discount_amount : 0
                    }

                    //新增订单
                    request({
                        url:`orders/add`,
                        method:'post',
                        data:state.orders
                    }).then((data) => {
                        if (data && data.code === 0) {

                        // 如果使用了优惠券，更新优惠券状态
                        if (state.selectedCoupon) {
                            request({
                                url: 'coupon/use',
                                method: 'post',
                                data: {
                                    user_coupon_id: state.selectedCoupon.id,
                                    orderid: state.orderId[index]
                                }
                            }).catch(err => {
                                console.error('更新优惠券状态失败:', err)
                            })
                        }

                        console.log("余额"+state.user.money);
                        console.log("总价"+state.totalPrice);
                        if (state.user.money < state.totalPrice) {
                            confirm('余额不足，请先充值').then(() => {
                                //点击确认
                                if (item.id) {


                                request({
                                    url:`cart/delete`,
                                    method:'post',
                                    data:[item.id]
                                }).then((data) => {
                                    if (data && data.code === 0) {


                                    notify("请去个人中心付款",{type:'success'});
                                    state.flag=false;



                                    state.open=false;

                                } else {

                                    notify(data.msg,{type:'error'});
                                }
                            })




                            }

                        }).catch(() => {

                                //点击取消
                                if (item.id) {

                                state.orders.status='已取消';
                                request({
                                    url:`cart/delete`,
                                    method:'post',
                                    data:[item.id]
                                }).then((data) => {
                                    if (data && data.code === 0) {
                                    if(state.flag){
                                        notify("已取消",{type:'success'});
                                        state.flag=false;
                                    }


                                    state.open=false;

                                } else {

                                    notify(data.msg,{type:'error'});
                                }
                            })




                            }

                        });

                        }else{




                            // 支付成功，增加用户积分（1元 = 5积分）
                            state.user.jf = Number(state.user.jf || 0) + Number(item.price * item.buynumber) * 5;
                            state.user.money = state.user.money - state.totalPrice;


                            let sessionTable = Session.get("tableName")
                            request({
                                url:`${sessionTable}/update`,
                                method:'post',
                                data:state.user
                            }).then((data) => {
                                if (data && data.code === 0) {


                                state.orders.status = '已支付'
                                console.log(state.orderId[index])
                                request({
                                    url:`orders/list`,
                                    method:'get',
                                    params:{
                                        orderid: state.orderId[index],
                                        page: 1,
                                        limit: 1,
                                    }
                                }).then((data)=>{

                                    state.orders.id = data.data.list[0].id;
                                request({
                                    url:`orders/update`,
                                    method:'post',
                                    data:state.orders
                                }).then((data)=>{
                                    if (data && data.code === 0) {
                                    request({
                                        url:`cart/delete`,
                                        method:'post',
                                        data:[item.id]
                                    }).then((data) => {
                                        if (data && data.code === 0) {
                                        notify("支付成功",{type:'success'});

                                        state.open=false;




                                        //

                                    } else {
                                        notify(data.msg,{type:'error'});
                                    }
                                })



                                }


                            })
                            })



                            } else {
                                notify(data.msg,{type:'error'});
                            }
                        })

                        }

                    } else {
                        notify(data.msg,{type:'error'});
                    }
                })





                } else {
                    notify(data.msg,{type:'error'});
                }
            })




            } else {
                notify(data.msg,{type:'error'});
            }
        })


        }

    }





    function genTradeNo() {
        var date = new Date();
        var tradeNo = date.getFullYear().toString() + (date.getMonth() + 1).toString() +
                date.getDate().toString() + date.getHours().toString() + date.getMinutes().toString() +
                date.getSeconds().toString() + date.getMilliseconds().toString();
        for (var i = 0; i < 5; i++) //5位随机数，用以加在时间戳后面。
        {
            tradeNo += Math.floor(Math.random() * 10);
        }
        return tradeNo;
    }




    defineExpose({
        openordersinit
    })






</script>


<style scoped>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        margin-bottom: 30px;
        font-size: 2.5em;
        color: #333;
    }
    .form-group {
        margin-bottom: 20px;
    }
    .form-group label {
        display: block;
        margin-bottom: 10px;
        font-size: 1.2em;
        color: #555;
    }
    .form-group input, .form-group select {
        width: 100%;
        padding: 12px;
        box-sizing: border-box;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 1em;
    }
    .form-group button {
        width: 100%;
        padding: 15px;
        background-color: #ff5000;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2em;
        transition: background-color 0.3s;
    }
    .form-group button:hover {
        background-color: #e64500;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 30px;
        background-color: #fff;
        border-radius: 10px;
    }
    table, th, td {
        border: 1px solid #ddd;
    }
    th, td {
        padding: 15px;
        text-align: left;
    }
    th {
        background-color: #f5f5f5;
        font-size: 1.2em;
        color: #333;
    }
    tfoot td {
        font-size: 1.2em;
        font-weight: bold;
        color: #333;
    }
    .address-section {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .address-section h2 {
        margin-top: 0;
        color: #333;
    }
    .address-section p {
        margin: 10px 0;
        color: #555;
    }


</style>