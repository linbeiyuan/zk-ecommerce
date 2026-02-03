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

    const AddEdit=defineAsyncComponent(()=>import('@/views/shangpinguanli/add-edit.vue'));



        







    const state=reactive({
        query:{
          userid:"",
                                                                            shangpinmingcheng:'',
                                                                                                                                dianpumingcheng:'',
                                                                                                                                                                                    
    },
    page:{
        current:1,
                size:10,
                total:0
    },
                    tableList:[],
            ids:[],
            isdel:true,
                        sfshVisiable:false,
                formData:{},
        
            })
    const { query,tableList,page,isdel
                                    ,sfshVisiable,
            formData
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


                                                                            if (state.query.shangpinmingcheng != '' && state.query.shangpinmingcheng != undefined) {
                    params['shangpinmingcheng'] = '%' + state.query.shangpinmingcheng + '%'
                }
                                                                                                                                if (state.query.dianpumingcheng != '' && state.query.dianpumingcheng != undefined) {
                    params['dianpumingcheng'] = '%' + state.query.dianpumingcheng + '%'
                }
                                                                                                                                                                                            request({
            url:'shangpinguanli/page',
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
            url:`shangpinguanli/delete`,
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
            url:`shangpinguanli/delete`,
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

        
        function shDialog(row:any){
            state.sfshVisiable=true;
            state.formData=row;


        }

        function shHandler(){
            confirm("确认要审核吗？").then(()=>{

                request({
                            url:'shangpinguanli/update',
                            method:'post',
                            data:state.formData
        }).then((data)=>{
                state.sfshVisiable=false;
            notify("操作成功",{type:'success'});
            getDateList();
        })

        })
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
                                                                                                            
                        <el-form-item label="商品名称"  prop="yonghuming">
                            <el-input v-model="query.shangpinmingcheng" maxlength="100" placeholder="请输入商品名称" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                                                                                                                                        
                        <el-form-item label="店铺名称"  prop="yonghuming">
                            <el-input v-model="query.dianpumingcheng" maxlength="100" placeholder="请输入店铺名称" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                                                                                                                                                                                                                                                                                    <el-form-item>
                    <el-button icon="ele-Search" @click="handleQuery()" type="primary">查询</el-button>
                    <el-button v-if="isgrAuth('shangpinguanli','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                    <el-button v-if="isgrAuth('shangpinguanli','新增')" icon="ele-Plus" type="success" @click="add()">新增</el-button>
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



                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="shangpinmingcheng" label="商品名称">

                                    <template #default="{row}">
                                        {{row.shangpinmingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                    

                            <el-table-column header-align="center"  align="center" prop="shangpintupian" label="商品图片">

                                <template #default="{row}">
                                    <img v-if="row.shangpintupian" :src="row.shangpintupian" width="100" height="100">
                                    <div v-else>无图片</div>
                                </template>

                            </el-table-column>
                                                                                                                                                                    <el-table-column header-align="center"  align="center" prop="fenleimingcheng" label="分类名称">

                                    <template #default="{row}">
                                        {{row.fenleimingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="dianpumingcheng" label="店铺名称">

                                    <template #default="{row}">
                                        {{row.dianpumingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="userid" label="用户id">

                                    <template #default="{row}">
                                        {{row.userid}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="price" label="价格">

                                    <template #default="{row}">
                                        {{row.price}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="onelimittimes" label="单限">

                                    <template #default="{row}">
                                        {{row.onelimittimes}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="alllimittimes" label="库存">

                                    <template #default="{row}">
                                        {{row.alllimittimes}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                
                                <el-table-column header-align="center"  align="center" prop="sfsh" label="审核状态">

                                    <template #default="{row}">
                                        <span style="margin-right:10px">{{row.sfsh=='是'?'通过':'未通过'}}</span>
                                    </template>

                                </el-table-column>
                                <el-table-column  v-if="isgrAuth('shangpinguanli','审核')" header-align="center"  align="center" prop="sfsh" label="审核">

                                    <template #default="{row}">
                                        <el-button type="text" icon="el-icon-edit" size="small" @click="shDialog(row)">审核
                                        </el-button>
                                    </template>

                                </el-table-column>


                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="shhf" label="审核回复">

                                    <template #default="{row}">
                                        {{row.shhf}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="thumbsupnum" label="赞">

                                    <template #default="{row}">
                                        {{row.thumbsupnum}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="crazilynum" label="踩">

                                    <template #default="{row}">
                                        {{row.crazilynum}}
                                    </template>

                                </el-table-column>

                                                                                                        <el-table-column fixed="right" align="center" label="操作" width="160">
                    <template #default="{row}">
                        <el-button v-if="isgrAuth('shangpinguanli','修改')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning" link>修改</el-button>
                        <el-popconfirm  v-if="isgrAuth('shangpinguanli','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
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

    
        <el-dialog
                title="审核"
                v-model="sfshVisiable"
                width="50%">
            <el-form ref="form" :model="formData" label-width="80px">
                <el-form-item label="审核状态">
                    <el-select v-model="formData.sfsh" placeholder="审核状态">
                        <el-option label="通过" value="是"></el-option>
                        <el-option label="不通过" value="否"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="内容">
                    <el-input type="textarea" :rows="8" v-model="formData.shhf"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
        <el-button @click="shDialog">取 消</el-button>
        <el-button type="primary" @click="shHandler">确 定</el-button>
      </span>
        </el-dialog>

    

    </div>
  </div>
</template>

<style scoped>

</style>
