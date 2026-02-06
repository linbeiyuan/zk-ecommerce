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



        <!-- 优惠券选择区域 -->
        <div class="cart-coupon-area">
            <el-button type="primary" size="small" @click="selectCoupon" style="margin-bottom: 10px;">
                选择优惠券
            </el-button>
            <div class="coupon-selected" v-if="selectedCoupon">
                <div class="coupon-info">
                    <span class="coupon-name">{{ selectedCoupon.name }}</span>
                    <span class="coupon-discount">-¥{{ selectedCoupon.discount_amount }}</span>
                    <el-button size="small" type="text" @click="removeCoupon">取消</el-button>
                </div>
            </div>
        </div>

        <!-- 价格汇总区域 -->
        <div class="cart-price-summary">
            <div class="price-row">
                <span class="price-label">商品总计：</span>
                <span class="price-value">¥{{ totalPrice }}</span>
            </div>
            <div class="price-row" v-if="selectedCoupon">
                <span class="price-label">优惠券：</span>
                <span class="price-value discount">-¥{{ selectedCoupon.discount_amount }}</span>
            </div>
            <div class="price-row total-row">
                <span class="price-label">应付总额：</span>
                <span class="price-value total">¥{{ finalPrice }}</span>
            </div>
        </div>

        <div class="cart-total">
           <el-button type="danger" style="width: 150px;" @click="onform()">结算</el-button>
        </div>
    </div>

</el-dialog>

    <!-- 优惠券选择对话框 -->
    <el-dialog title="选择优惠券" v-model="couponDialogVisible" width="600px">
        <div class="coupon-select-list">
            <div v-if="availableCoupons.length > 0">
                <h4 style="margin-bottom: 15px; color: #333;">可用优惠券</h4>
                <div
                    v-for="coupon in availableCoupons"
                    :key="coupon.id"
                    class="coupon-item"
                    :class="{ 'selected': state.selectedCoupon && state.selectedCoupon.id === coupon.id }"
                    @click="chooseCoupon(coupon)"
                >
                    <div class="coupon-left">
                        <div class="amount">¥{{ coupon.discount_amount }}</div>
                        <div class="condition">满{{ coupon.condition_amount }}元</div>
                    </div>
                    <div class="coupon-right">
                        <div class="name">{{ coupon.name }}</div>
                        <div class="expire">有效期至：{{ formatDate(coupon.expire_time) }}</div>
                    </div>
                    <div class="check-icon" v-if="state.selectedCoupon && state.selectedCoupon.id === coupon.id">
                        ✓
                    </div>
                </div>
            </div>

            <div v-if="unavailableCoupons.length > 0" style="margin-top: 20px;">
                <h4 style="margin-bottom: 15px; color: #999;">不可用优惠券</h4>
                <div
                    v-for="coupon in unavailableCoupons"
                    :key="coupon.id"
                    class="coupon-item disabled"
                >
                    <div class="coupon-left">
                        <div class="amount">¥{{ coupon.discount_amount }}</div>
                        <div class="condition">满{{ coupon.condition_amount }}元</div>
                    </div>
                    <div class="coupon-right">
                        <div class="name">{{ coupon.name }}</div>
                        <div class="reason">{{ coupon.reason }}</div>
                    </div>
                </div>
            </div>
        </div>
        <template #footer>
            <el-button @click="couponDialogVisible = false">取消</el-button>
            <el-button type="primary" @click="confirmCoupon">确定</el-button>
        </template>
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
         selectedCoupon: null,
     })

const couponDialogVisible = ref(false)
const availableCoupons = ref([])
const unavailableCoupons = ref([])
const tempSelectedCoupon = ref(null)


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

     ordersRef.value.openordersinit(state.selectedCoupon);

 }




defineExpose({
    openinit
})

// 选择优惠券
const selectCoupon = async () => {
    try {
        // 获取可用优惠券
        const res = await request({
            url: 'coupon/available',
            method: 'get',
            params: {
                total_amount: totalPrice.value
            }
        })

        if (res.code === 0) {
            const { available, unavailable } = res.data

            if (available.length === 0 && unavailable.length === 0) {
                notify('暂无可用优惠券，去领取中心领取吧', {type: 'info'})
                return
            }

            if (available.length === 0) {
                notify('暂无满足条件的优惠券', {type: 'warning'})
                return
            }

            // 显示优惠券选择对话框
            showCouponDialog(available, unavailable)
        }
    } catch (error) {
        notify('获取优惠券失败', {type: 'error'})
    }
}

// 显示优惠券选择对话框
const showCouponDialog = (available, unavailable) => {
    availableCoupons.value = available
    unavailableCoupons.value = unavailable
    tempSelectedCoupon.value = state.selectedCoupon
    couponDialogVisible.value = true
}

// 选择优惠券
const chooseCoupon = (coupon) => {
    tempSelectedCoupon.value = coupon
}

// 确认选择优惠券
const confirmCoupon = () => {
    state.selectedCoupon = tempSelectedCoupon.value
    couponDialogVisible.value = false
    if (state.selectedCoupon) {
        notify(`已选择优惠券：${state.selectedCoupon.name}`, {type: 'success'})
    }
}

// 格式化日期
const formatDate = (dateStr) => {
    if (!dateStr) return ''
    const date = new Date(dateStr)
    return date.toLocaleDateString('zh-CN')
}

// 取消优惠券
const removeCoupon = () => {
    state.selectedCoupon = null
}

// 计算实付金额
const finalPrice = computed(() => {
    if (state.selectedCoupon) {
        return Math.max(0, totalPrice.value - state.selectedCoupon.discount_amount)
    }
    return totalPrice.value
})














</script>

<style scoped>
/* 优惠券选择对话框样式 */
.coupon-select-list {
    max-height: 500px;
    overflow-y: auto;
}

.coupon-item {
    display: flex;
    align-items: center;
    padding: 15px;
    margin-bottom: 10px;
    border: 2px solid #ff6b6b;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
    background: white;
}

.coupon-item:hover {
    transform: translateX(5px);
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}

.coupon-item.selected {
    border-color: #ff6b6b;
    background: linear-gradient(135deg, #fff5f5 0%, #ffe8e8 100%);
}

.coupon-item.disabled {
    opacity: 0.5;
    cursor: not-allowed;
    border-color: #ddd;
}

.coupon-item.disabled:hover {
    transform: none;
    box-shadow: none;
}

.coupon-left {
    width: 100px;
    text-align: center;
    border-right: 2px dashed #ff6b6b;
    padding-right: 15px;
    margin-right: 15px;
}

.coupon-item.disabled .coupon-left {
    border-right-color: #ddd;
}

.coupon-left .amount {
    font-size: 24px;
    font-weight: bold;
    color: #ff6b6b;
}

.coupon-left .condition {
    font-size: 12px;
    color: #999;
    margin-top: 5px;
}

.coupon-right {
    flex: 1;
}

.coupon-right .name {
    font-size: 16px;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
}

.coupon-right .expire,
.coupon-right .reason {
    font-size: 13px;
    color: #999;
}

.check-icon {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    width: 24px;
    height: 24px;
    background: #ff6b6b;
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}

/* 购物车优惠券区域样式 */
.cart-coupon-area {
    margin: 20px 0;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 8px;
}

.coupon-selected {
    margin-top: 10px;
}

.coupon-selected .coupon-info {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px;
    background: white;
    border: 1px solid #ff6b6b;
    border-radius: 6px;
}

.coupon-selected .coupon-name {
    flex: 1;
    font-size: 14px;
    color: #333;
    font-weight: 500;
}

.coupon-selected .coupon-discount {
    font-size: 16px;
    color: #ff6b6b;
    font-weight: bold;
}

/* 价格汇总区域样式 */
.cart-price-summary {
    margin: 20px 0;
    padding: 15px;
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
}

.price-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    font-size: 14px;
}

.price-row .price-label {
    color: #666;
}

.price-row .price-value {
    color: #333;
    font-weight: 500;
}

.price-row .price-value.discount {
    color: #ff6b6b;
}

.price-row.total-row {
    border-top: 1px solid #e0e0e0;
    margin-top: 10px;
    padding-top: 15px;
}

.price-row.total-row .price-label {
    font-size: 16px;
    font-weight: bold;
    color: #333;
}

.price-row.total-row .price-value.total {
    font-size: 20px;
    font-weight: bold;
    color: #ff6b6b;
}


</style>

