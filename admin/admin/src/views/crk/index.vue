<script setup lang="ts">
  import { defineAsyncComponent,reactive,ref,toRefs,onMounted,computed } from 'vue';
  import { toRaw } from "@vue/reactivity";
  import { Key } from '@/stores/auth';
  import { Session } from '@/utils/storage';
  import request from "@/utils/request";
  import {notify,confirm} from '@/utils/element';
  import { isAuth } from '@/utils/utils';
  import {exportExcel} from '@/utils/exportExcel';
  import printJS from 'print-js'

  const AddEdit=defineAsyncComponent(()=>import('@/views/yonghu/add-edit.vue'));
        const state=reactive({
          crkzt:['出库','入库'],
          query:{
            name:'',
            crkzt:''                          
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

  // 获取当前登录用户信息
  const users=Session.get(Key.userInfoKey);

  //进入执行
  getDateList();
  //获取列表
  function getDateList(){
    const params={
      page: state.page.current,
      limit: state.page.size,
        }

    // 如果是商家角色，只查询自己商品的出入库记录
    if (users && users.role === 'shangjia') {
      params['shangjia_userid'] = users.id
    }

         if (state.query.name != '' && state.query.name != undefined) {
              params['name'] = '%' + state.query.name + '%'
            }

            if (state.query.crkzt != '' && state.query.crkzt != undefined) {
              params['crkzt'] = '%' + state.query.crkzt + '%'
            }
   request({
      url:'crk/page',
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
      url:`crk/delete`,
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
      url:`crk/delete`,
      method:'post',
      data:ids
    }).then(({data})=>{
      notify("删除成功",{type:'success'});
      getDateList();

    })
  }

  const editRef=ref();


      




      

      


      
      

</script>
<template>
    <el-card shadow="never">
        <template #header>
            <div class="card_header">
                <b>列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">

                                                                                                            
                        <el-form-item label="名称"  prop="zhanghao">
                            <el-input v-model="query.name" maxlength="100" placeholder="请输入名称" clearable style="width: 200px;"/>
                        </el-form-item>
                        <el-form-item label="出入库" prop="crkzt">
            <el-select clearable v-model="query.crkzt" placeholder="选择" style="width: 240px">
                  <el-option
                    v-for="item in state.crkzt"
                    :key="item"
                    :label="item"
                    :value="item"
                  />
             </el-select>
          </el-form-item>                                                             <el-form-item>
                  <div class="button-container">
                    <el-button icon="ele-Search" @click="handleQuery()" class="button button-7">查询</el-button>
                    <el-button  class="button button-6" v-if="isAuth('yonghu','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                                                                                                          </div>

                </el-form-item>


              

            </el-form>



            <el-table
                ref="tableListRef"
                :data="tableList"
                :header-cell-style="{
            textAlign: 'center',
            height: '60px',
            background: '#a4a7f7bd',
            color: '#ffffff'
        }"
                style="width: 100%"
                stripe
                :row-style="{height:'80px'}"
                border
                highlight-current-row
                class="custom-table"
                    @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" />



                             <el-table-column header-align="center"  align="center" prop="name" label="名称">

                                    <template #default="{row}">
                                        {{row.name}}
                                    </template>

                                </el-table-column>

                                 <el-table-column header-align="center"  align="center" prop="sl" label="数量">

                                    <template #default="{row}">
                                        {{row.sl}}
                                    </template>

                                </el-table-column>
                                <el-table-column header-align="center"  align="center" prop="sl" label="出入库">

                                    <template #default="{row}">
                                        {{row.crkzt}}
                                    </template>

                                    </el-table-column>
                       <el-table-column fixed="right" align="center" label="操作" width="400">
                    <template #default="{row}">
                        <el-popconfirm width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
                            <template #reference>
                                <el-button class="button button-6" icon="ele-Delete" type="danger">删除</el-button>
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
  .button-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 20px;
  }

  .button {
    padding: 0px 20px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease;
  }

  .button:hover {
    transform: scale(1.05);
  }

  /* 不同样式的按钮 */
  .button-6 {
    background: linear-gradient(45deg, #ff9a9e, #fad0c4);
    color: white;
  }

  .button-7 {
    background: linear-gradient(45deg, #a1c4fd, #c2e9fb);
    color: white;
  }

  .button-8 {
    background: linear-gradient(45deg, #84fab0, #8fd3f4);
    color: white;
  }
</style>
