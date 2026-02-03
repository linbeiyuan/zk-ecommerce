<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify} from '@/utils/element';
    import { isAuth } from '@/utils/utils'



    const AddEdit=defineAsyncComponent(()=>import('@/views/news/add-edit.vue'));
    const state=reactive({
        query:{
            title:''
        },
        page:{
            current:1,
            size:10,
            total:0
        },
        tableList:[],
        ids:[],
        isdel:true,

    })
    const { query,tableList,page,isdel } = {...toRefs(state)};

    //进入执行
    getDateList();
    //获取列表
    function getDateList(){
        const params={
            page: state.page.current,
            limit: state.page.size,
        }


        if (state.query.title != '' && state.query.title != undefined) {
            params['title'] = '%' + state.query.title + '%'
        }
        request({
            url:'news/page',
            method:'get',
            params
        }).then(({data})=>{

            state.page.total=data.total;
        state.tableList=data.list;
    })
    }
    //查询
    function handleQuery(){
        getDateList();
    }

    //删除

    function handleDelete(row:any){

        request({
            url:`news/delete`,
            method:'post',
            data:[row.id]
        }).then(({data})=>{
            notify("删除成功",{type:'success'});
        getDateList();

    })
    }

    const multipleSelection = ref<[]>([]);

    function handleSelectionChange(val:any){
        multipleSelection.value=val;
        const list=toRaw(multipleSelection.value)
        list.forEach((item)=>{
            state.ids.push(item.id);
    })

        if(list.length==0){
            state.ids=[];
            state.isdel=true
        }else{
            state.isdel=false
        }

    }


    function listdel(){
        const ids=toRaw(state.ids)
        request({
            url:`news/delete`,
            method:'post',
            data:ids
        }).then(({data})=>{
            notify("删除成功",{type:'success'});
        getDateList();

    })
    }


    const users=Session.get(Key.userInfoKey);

    const editRef=ref();

    function add(){
        editRef.value.open('新增','add');
    }
    function handleEdit(row:any){
        editRef.value.open('修改','up',row);
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


                <el-form-item label="标题"  prop="title">
                    <el-input v-model="query.title" maxlength="100" placeholder="请输入标题" clearable style="width: 200px;"/>
                </el-form-item>
                <el-form-item>
                    <el-button icon="ele-Search" @click="handleQuery()" type="primary">查询</el-button>
                    <el-button v-if="isAuth('news','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                    <el-button v-if="isAuth('news','新增')" icon="ele-Plus" type="success" @click="add()">新增</el-button>
                </el-form-item>
            </el-form>

            <el-table
                    class="w100"
                    ref="tableListRef"
                    :data="tableList"
                    border
                    stripe
                    @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" />



                <el-table-column header-align="center"  align="center" prop="biaoti" label="标题">

                    <template #default="{row}">
                        {{row.title}}
                    </template>

                </el-table-column>



                <el-table-column header-align="center"  align="center" prop="tupian" label="图片">

                    <template #default="{row}">
                        <img v-if="row.picture" :src="row.picture" width="100" height="100">
                        <div v-else>无图片</div>
                    </template>

                </el-table-column>
                <el-table-column fixed="right" align="center" label="操作" width="160">
                    <template #default="{row}">
                        <el-button v-if="isAuth('news','修改')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning" link>修改</el-button>
                        <el-popconfirm  v-if="isAuth('news','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
                            <template #reference>
                                <el-button icon="ele-Delete" type="danger" link>删除</el-button>
                            </template>
                        </el-popconfirm>
                    </template>
                </el-table-column>
            </el-table>

            <!-- 分页 -->
            <m-page :page="page" @pageChange="getDateList"/>

            <AddEdit ref="editRef" @refresh="getDateList"/>
        </div>
    </el-card>
</template>

<style scoped>

</style>