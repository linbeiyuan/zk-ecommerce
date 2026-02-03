<script setup lang="ts">
    import { defineAsyncComponent,reactive,ref,toRefs,onMounted,computed } from 'vue';
    import { toRaw } from "@vue/reactivity";
    import { Key } from '@/stores/auth';
    import { Session } from '@/utils/storage';
    import request from "@/utils/request";
    import {notify,confirm} from '@/utils/element';
    import { isgrAuth } from '@/utils/utils';
    import {exportExcel} from '@/utils/exportExcel';
    import printJS from 'print-js'

    const AddEdit=defineAsyncComponent(()=>import('@/views/shangjia/add-edit.vue'));



        







    const state=reactive({
        query:{
          userid:"",
                                                                            yonghuming:'',
                                                                                                                        
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
    const { query,tableList,page,isdel
                                  } = {...toRefs(state)};

    //进入执行
 let sessionTable = Session.get("tableName")
        request({
            url: sessionTable + '/session',
            method: "get"
        }).then((
                data
        ) => {
            if (data && data.code === 0) {

            state.query.userid=data.data.id;
            getDateList();
        } else {
            notify(data.msg,{type:'error'});
        }
    });
    //获取列表
    function getDateList(){
        const params={
            page: state.page.current,
            limit: state.page.size,
            userid:state.query.userid
                                }


                                                                            if (state.query.yonghuming != '' && state.query.yonghuming != undefined) {
                    params['yonghuming'] = '%' + state.query.yonghuming + '%'
                }
                                                                                                                                request({
            url:'shangjia/page',
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

    function download(file) {
        window.open(`${file}`)
    }

    //删除

    function handleDelete(row:any){

        request({
            url:`shangjia/delete`,
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
            url:`shangjia/delete`,
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
        editRef.value.open('新增','','add');
    }
    function handleEdit(row:any){
        editRef.value.open('修改',row.id,'up',row);
    }

        

        


        
    

</script>

<template>
  <div class="bg-gray-60">
    <div class="container mx-auto px-4 py-8 max-w-8xl">
    <el-card shadow="never" class="index">
        <template #header>
            <div class="card_header">

                <b>列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">
                <el-form-item label="用户ID"  prop="yonghuming">
                            <el-input readonly="true" v-model="query.userid" maxlength="100" placeholder="用户ID" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                                            
                        <el-form-item label="用户名"  prop="yonghuming">
                            <el-input v-model="query.yonghuming" maxlength="100" placeholder="请输入用户名" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                                                                                                                                                                        <el-form-item>
                    <el-button icon="ele-Search" @click="handleQuery()" type="primary">查询</el-button>
                    <el-button v-if="isgrAuth('shangjia','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                    <el-button v-if="isgrAuth('shangjia','新增')" icon="ele-Plus" type="success" @click="add()">新增</el-button>
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



                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="yonghuming" label="用户名">

                                    <template #default="{row}">
                                        {{row.yonghuming}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="mima" label="密码">

                                    <template #default="{row}">
                                        {{row.mima}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="shoujihao" label="手机号">

                                    <template #default="{row}">
                                        {{row.shoujihao}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="shangjiamingcheng" label="商家名称">

                                    <template #default="{row}">
                                        {{row.shangjiamingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="money" label="余额">

                                    <template #default="{row}">
                                        {{row.money}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="jf" label="积分">

                                    <template #default="{row}">
                                        {{row.jf}}
                                    </template>

                                </el-table-column>

                                                                                                        <el-table-column fixed="right" align="center" label="操作" width="160">
                    <template #default="{row}">
                        <el-button v-if="isgrAuth('shangjia','修改')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning" link>修改</el-button>
                        <el-popconfirm  v-if="isgrAuth('shangjia','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
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

    

    </div>
  </div>
</template>

<style scoped>

</style>
