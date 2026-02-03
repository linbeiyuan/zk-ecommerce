<script setup lang="ts">

import {ref,onMounted,reactive,toRefs, nextTick} from 'vue';
    import { defineAsyncComponent } from 'vue';
    import { Key } from '@/stores/auth';
     import { Session } from '@/utils/storage';
import request from "@/utils/request";
       import {notify} from '@/utils/element'

     const editRef=ref();
       const ConfigEdit=defineAsyncComponent(()=>import('./add-update.vue'));
   const state=reactive({
       tableList:[],
       query:{},
       loading:false,
       page:{
        current:1,
        size:10,
        total:0
    },
   })
   const { tableList,query,loading,page } = {...toRefs(state)};
     getconfig();

     function getconfig(){

        const params={
            page: state.page.current,
            limit: state.page.size,  
        }

        state.loading=true;
        request({
            url:`config/list`,
            method:'get',
            params
        }).then(({data})=>{
            state.loading=false;
            state.page.total=data.total;
            state.tableList=data.list;
        })
     }

     function handleAdd(){
        editRef.value.open('新增','add')
     }

     function handleEdit(row:any){
        editRef.value.open('修改','up',row)
     }

     function handleDelete(id:number){
        request({
        url:`config/delete`,
        method:'post',
        data:[id]
     }).then(({data})=>{
        notify("删除成功",{type:'success'});
        getconfig();

     })
     }

</script>



<template>

<el-card shadow="never" class="index">
        <template #header>
            <div class="card_header">
                <b>轮播图列表</b>
            </div>
        </template>
       


        <el-form inline  label-suffix=":" :model="query">
           
            <el-form-item>
                <el-button @click="handleAdd()" icon="ele-Plus" type="success" >新增</el-button>
            </el-form-item>
        </el-form>

        <el-table
            class="w100"
            ref="tableListRef"
            v-loading="loading"
            :data="tableList"
            :height="550"
            border
            stripe>
            <el-table-column header-align="center" align="center" prop="name" label="名称" show-overflow-tooltip/>
          
            <el-table-column header-align="center" align="center" prop="value" label="图片">

                <template #default="{row}">
                    <img v-if="row.value" :src="row.value" style="width: 100px;height: 100px;" alt="">
                    <p v-else>无图片</p>
                </template>
            </el-table-column>
  



            <el-table-column fixed="right" align="center" label="操作">
                <template #default="{row}">
                    <el-button @click.stop="handleEdit(row)" type="warning" icon="ele-Edit" link>修改</el-button>
                    <el-popconfirm @confirm="handleDelete(row.id)" width="auto" :title="`确定永久删除【${row.name}】吗？`">
                        <template #reference>
                            <el-button  icon="ele-Delete" type="danger" link>删除</el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table>
          
          
                
       <!-- 分页 -->
       <m-page :page="page" @pageChange="getconfig"/>
       
        <ConfigEdit ref="editRef" @refresh="getconfig"/>


    </el-card>


    
</template>