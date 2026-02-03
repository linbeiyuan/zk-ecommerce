<template>
    <div>
       <el-dialog title="购物车" v-model="open" append-to-body :close-on-click-modal="false" :close-on-press-escape="false">
        <div class="cart">
        <h1>购物车</h1>
        <div class="cart-item" v-for="(item,index) in dataList" :key="index">
            <img :src="item.picture" alt="商品图片">
            <div class="item-details">
                <h3>{{ item.goodname }}</h3>
                <!-- <p>描述：{{ item. }}</p> -->
            </div>
            <div class="quantity">
                <button @click="reduceCartNum(index)">-</button>
                <input type="text" v-model="item.buynumber" readonly>
                <button @click="addCartNum(index)">+</button>
            </div>
            <div class="item-price">{{item.price}}</div>
            <button class="remove-item" @click="deleteCart(index)">删除</button>
        </div>

 
    
        <div class="cart-total">
            总计：¥<span id="total" >{{totalPrice}}</span>
        </div>
        <div class="cart-total">
           <el-button type="danger" style="width: 150px;" @click="onform()">结算</el-button>
        </div>
    </div>

</el-dialog>
    
     <OrdersFrom ref="ordersRef"></OrdersFrom>

</div>
</template>

<script setup>
import { defineAsyncComponent,reactive,ref,toRefs,computed } from 'vue';
import { toRaw } from "@vue/reactivity";
import { Key } from '@/stores/auth';
import { Session } from '@/utils/storage';
import request from "@/utils/request";
import {notify,confirm} from '@/utils/element';
import { isAuth } from '@/utils/utils'
import { ElLoading } from 'element-plus'
const OrdersFrom=defineAsyncComponent(()=>import('@/views/orders/orderfrom.vue'));
     const state=reactive({
         open:false,
         dataList:[],
         user:{},
         total:0,
         openOrdersDialog:false,
         detailTable: '${tableName}',
     })


const {open,dataList,user,total,openOrdersDialog,detailTable} = {...toRefs(state)};

    const totalPrice=computed(()=>{
        state.total=0;

            for (var item of state.dataList) {

                state.total += item.price * item.buynumber
            }
                 return state.total;
    })
    // computed: {
    //
    //         totalPrice: function() {
    //
    //
    //         }
    //     },


let sessionTable = Session.get("tableName")
    request({
        url: sessionTable + '/session',
        method: "get"
    }).then((data) => {
        if (data && data.code === 0) {
        state.user = data.data;
        console.log("用户ID:"+state.user.id)
    } else {
    notify(data.msg,{type:'error'});
    }
});



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
 


             // 添加数量
            function addCartNum(index) {
                // 查询对应的商品的详情信息，判断是否有商品限次，库存的判断
                 var item = state.dataList[index];
                    request({
                    url:`${item.tablename}/info/${item.goodid}`,
                    method:"get"

                 }).then((data) => {

                  
            if (data && data.code === 0) {

                if (data.data.onelimittimes && data.data.onelimittimes > 0 && data.data.onelimittimes <= item.buynumber) {


                    notify(`每人单次只能购买${data.data.onelimittimes}次`,{type:'error'});
                        return
                    }else{
                     
                    }

                    if (data.data.alllimittimes && data.data.alllimittimes > 0 && data.data.alllimittimes <= item.buynumber) {
                        notify(`商品已售罄`,{type:'error'});
                        return
                    }   
                    item.buynumber = item.buynumber + 1;


                         request({
                    url:`cart/update`,
                    method:"post",
                    data:item
                  }).then((data) => {
            if (data && data.code === 0) {
            
        } else {
                        notify(data.msg,{type:'error'});
        }
    });

            
        } else {
                    notify(data.msg,{type:'error'});
        }
    });
                 
    
    
      
           
           
                }



        // 减少数量
       function reduceCartNum(index) {
                var item = state.dataList[index];
                if (item.buynumber > 1) {
                    item.buynumber = item.buynumber - 1;
                       request({
                    url:`cart/update`,
                    method:"post",
                    data:item
                  }).then((data) => {
            if (data && data.code === 0) {
            
        } else {
                        notify(data.msg,{type:'error'});
        }
    });
                }
            }
  
 // 删除
 function deleteCart(index) {
                var item = state.dataList[index];
        request({
                    url:`cart/delete`,
                    method:"post",
                    data:[item.id]
                  }).then((data) => {
            if (data && data.code === 0) {
                getlist()
        } else {
         notify(data.msg,{type:'error'});
        }
    });
            }


function openinit(){
   state.open=true;
    state.total=0;
    getlist();


}

const ordersRef=ref();
 function onform(){
      state.open=false;

     ordersRef.value.openordersinit();

 }




defineExpose({
    openinit
})
















</script>


