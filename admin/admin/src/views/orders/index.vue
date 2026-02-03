
<script setup lang='ts'>
    import { useRoute,useRouter } from 'vue-router'
    import { reactive, ref,watch,toRefs,defineAsyncComponent } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify,confirm} from '@/utils/element';
    import { isAuth } from '@/utils/utils'
    const router = useRouter();
    const PieChart=defineAsyncComponent(()=>import('@/components/echarts/pieChart.vue'));
    const state=reactive({
        query:{
            orderid:'',
            goodname:''
        },
        loading:false,
        tjdialogTableVisible:false,
        category:{
            data:[]
        },
        orderStatus:'',
        page:{
            current:1,
            size:10,
            total:0
        },
        tableList:[],
    })

    const { query,tableList,page,orderStatus,loading,category,tjdialogTableVisible } = {...toRefs(state)};

    // 获取当前登录用户信息
    const users = Session.get(Key.userInfoKey);

    //监听订单路由携带参数
    watch(() =>
    router.currentRoute.value.path,
            (toPath) => {
        //要执行的方法
        state.orderStatus = router.currentRoute.value.params.status;
        getDateList();
    },{immediate: true,deep: true})






    function getDateList(){
        const params={
            page: state.page.current,
            limit: state.page.size,
            status:state.orderStatus,
        }

        // 如果是商家角色，只查询自己商品的订单
        if (users && users.role === 'shangjia') {
            params['shangjia_userid'] = users.id
        }

        if (state.query.orderid != '' && state.query.orderid != undefined) {
            params['orderid'] = '%' + state.query.orderid + '%'
        }
        if (state.query.goodname != '' && state.query.goodname != undefined) {
            params['goodname'] = '%' + state.query.goodname + '%'
        }
        request({
            url:'orders/page',
            method:'get',
            params
        }).then(({data})=>{

            state.page.total=data.total;
        state.tableList=data.list;
    })
    }


    function handleQuery(){
        getDateList();
    }

    function handleDelete(row:any){
        request({
            url:`orders/delete`,
            method:'post',
            data:[row.id]
        }).then(({data})=>{
            notify("删除成功",{type:'success'});
        getDateList();

    })
    }

    function handleEdit(row:any){
        confirm("确认要发货吗？").then(()=>{

            row.status = "已发货";
        request({
            url:'orders/update',
            method:'post',
            data: row
        }).then((data)=>{
            notify("操作成功",{type:'success'});
        getDateList();
    })



    })
    }

    function handleEdit1(row:any){
        confirm("确认要收货吗？").then(()=>{

            row.status = "已完成";
        request({
            url:'orders/update',
            method:'post',
            data: row
        }).then((data)=>{
            notify("操作成功",{type:'success'});
        getDateList();
    })



    })
    }

    function getfenglei(){

        request({
            url:'group/orders/status',
            method:'get'
        }).then((data)=>{
            // console.log(data.data);
            const newsarr= objArrtransArr(data.data,'status','total');
        state.category.data=newsarr;
        state.loading=false;
        console.log("统计",state.category.data)
    })
    }


    function  objArrtransArr(olddata:any, oldval:any, oldname:any) {
        const newArr:any = [];
        olddata.forEach(item => {
            // 定义数组内部对象形式
            let obj = {};
        obj.name = item[oldval];
        obj.value = item[oldname];
        // 将对象数据推到数组中
        newArr.push(obj);
    });
        return newArr;
    }


    function tj(){
        state.tjdialogTableVisible=true;
        getfenglei();
    }
</script>

<template>
    <el-card shadow="never" class="index">
        <template #header>
            <div class="card_header">

                <b>列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">


                <el-form-item label="订单编号"  prop="orderid">
                    <el-input v-model="query.orderid" maxlength="100" placeholder="请输入编号" clearable style="width: 200px;"/>
                </el-form-item>
                <el-form-item label="商品名称"  prop="goodname">
                    <el-input v-model="query.goodname" maxlength="100" placeholder="商品名称" clearable style="width: 200px;"/>
                </el-form-item>
                <el-form-item>
                    <el-button icon="ele-Search" @click="handleQuery()" type="primary">查询</el-button>
                    <el-button @click="tj()" type="success">统计</el-button>
                </el-form-item>
            </el-form>

            <el-table
                    class="w100"
                    ref="tableListRef"
                    :data="tableList"
                    border>



                <el-table-column header-align="center"  align="center" prop="orderid" label="订单编号">

                    <template #default="{row}">
                        {{row.orderid}}
                    </template>

                </el-table-column>
                <el-table-column header-align="center"  align="center" prop="goodname" label="商品名称">

                    <template #default="{row}">
                        {{row.goodname}}
                    </template>

                </el-table-column>

                <el-table-column header-align="center"  align="center" prop="picture" label="商品图片">

                    <template #default="{row}">
                        <img v-if="row.picture" :src="row.picture" width="100" height="100">
                        <div v-else>无图片</div>
                    </template>

                </el-table-column>

                <el-table-column header-align="center"  align="center" prop="buynumber" label="购买数量">

                    <template #default="{row}">
                        {{row.buynumber}}
                    </template>

                </el-table-column>
                <el-table-column header-align="center"  align="center" prop="price" label="价格">

                    <template #default="{row}">
                        {{row.price}}
                    </template>

                </el-table-column>

                <el-table-column header-align="center"  align="center" prop="total" label="总价格">

                    <template #default="{row}">
                        {{row.total}}
                    </template>

                </el-table-column>

                <el-table-column header-align="center"  align="center" prop="status" label="状态">

                    <template #default="{row}">
                        {{row.status}}
                    </template>

                </el-table-column>


                <el-table-column fixed="right" align="center" label="操作" width="160">
                    <template #default="{row}">
                        <el-button  v-if="isAuth('orders'+'/'+orderStatus,'发货')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning" link>发货</el-button>
                        <el-button  v-if="isAuth('orders'+'/'+orderStatus,'确认收货')" icon="ele-Edit" @click.stop="handleEdit1(row)" type="warning" link>确认收货</el-button>
                        <el-popconfirm width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
                            <template #reference>
                                <el-button icon="ele-Delete" type="danger" link>删除</el-button>
                            </template>
                        </el-popconfirm>
                    </template>
                </el-table-column>
            </el-table>

            <!-- 分页 -->
            <m-page :page="page" @pageChange="getDateList"/>

        </div>
    </el-card>

    <el-dialog v-model="tjdialogTableVisible" title="统计" width="800" destroy-on-close
               center>


        <PieChart
                title="订单统计"
                subtitle="订单统计分析"
                :data="category.data"
        />



    </el-dialog>


</template>

<style  scoped>

</style>
