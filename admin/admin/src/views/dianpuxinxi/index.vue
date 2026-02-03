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

  const AddEdit=defineAsyncComponent(()=>import('@/views/dianpuxinxi/add-edit.vue'));
        const state=reactive({
          query:{
                                                                                dianpumingcheng:'',
                                                                        nicheng:'',
                                                                                                                                                                                                        
    },
    page:{
      current:1,
      size:10,
      total:0
    },
          tableList:[],
    ids:[] as any[],
    isdel:true,
              sfshVisiable:false,
        formData:{},
      
        })
  const { query,tableList,page,isdel
                          ,sfshVisiable,
        formData
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

    // 如果是商家角色，只查询自己的店铺
    if (users && users.role === 'shangjia') {
      params['userid'] = users.id
    }

                                                            if (state.query.dianpumingcheng != '' && state.query.dianpumingcheng != undefined) {
              params['dianpumingcheng'] = '%' + state.query.dianpumingcheng + '%'
            }
                                                      if (state.query.nicheng != '' && state.query.nicheng != undefined) {
              params['nicheng'] = '%' + state.query.nicheng + '%'
            }
                                                                                                                                                                    request({
      url:'dianpuxinxi/page',
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
      url:`dianpuxinxi/delete`,
      method:'post',
      data:[row.id]
    }).then(({data})=>{
      notify("删除成功",{type:'success'});
      getDateList();

    })
  }

const multipleSelection = ref<any[]>([]);

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
      url:`dianpuxinxi/delete`,
      method:'post',
      data:ids
    }).then(({data})=>{
      notify("删除成功",{type:'success'});
      getDateList();

    })
  }


  const editRef=ref();


      


  function add(){
    editRef.value.open('新增','add');
  }
  function handleEdit(row:any){
    editRef.value.open('修改','up',row);
  }

      
      function shDialog(row:any){
        state.sfshVisiable=true;
        state.formData=row;


      }

      function shHandler(){
        confirm("确认要审核吗？").then(()=>{

          request({
            url:'dianpuxinxi/update',
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
<div class="page-background">
    <el-card shadow="never">
        <template #header>
            <div class="card_header">
                <b>店铺信息列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">

                                                                                                            
                        <el-form-item label="店铺名称"  prop="dianpumingcheng">
                            <el-input v-model="query.dianpumingcheng" maxlength="100" placeholder="请输入店铺名称" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                            
                        <el-form-item label="昵称"  prop="nicheng">
                            <el-input v-model="query.nicheng" maxlength="100" placeholder="请输入昵称" clearable style="width: 200px;"/>
                        </el-form-item>
                                                                                                                                                                                                                                                                                                                                                                                        <el-form-item>
                  <div class="button-container">
                    <el-button icon="ele-Search" @click="handleQuery()" class="button button-7">查询</el-button>
                    <el-button  class="button button-6" v-if="isAuth('dianpuxinxi','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                    <el-button class="button button-8" v-if="isAuth('dianpuxinxi','新增')" icon="ele-Plus" type="success" @click="add()">新增</el-button>
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
                :row-class-name="tableRowClassName"
                stripe
                :row-style="{height:'80px'}"
                border
                highlight-current-row
                class="custom-table"
                    @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" />



                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="dianpumingcheng" label="店铺名称">

                                    <template #default="{row}">
                                        {{row.dianpumingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                    

                            <el-table-column header-align="center"  align="center" prop="tupian" label="图片">

                                <template #default="{row}">
                                    <img v-if="row.tupian" :src="row.tupian" width="100" height="100">
                                    <div v-else>无图片</div>
                                </template>

                            </el-table-column>
                                                                                                                                                                    <el-table-column header-align="center"  align="center" prop="nicheng" label="昵称">

                                    <template #default="{row}">
                                        {{row.nicheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="shangjiadianhua" label="商家电话">

                                    <template #default="{row}">
                                        {{row.shangjiadianhua}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="dianpudizhi" label="店铺地址">

                                    <template #default="{row}">
                                        {{row.dianpudizhi}}
                                    </template>

                                </el-table-column>

                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="userid" label="用户id">

                                    <template #default="{row}">
                                        {{row.userid}}
                                    </template>

                                </el-table-column>


                                                                                                                                                                
                                <el-table-column header-align="center"  align="center" prop="sfsh" label="审核状态">

                                    <template #default="{row}">
                                        <span style="margin-right:10px">{{row.sfsh=='是'?'通过':'未通过'}}</span>
                                    </template>

                                </el-table-column>
                                <el-table-column  v-if="isAuth('dianpuxinxi','审核')" header-align="center"  align="center" prop="sfsh" label="审核">

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

                                                                                                        <el-table-column fixed="right" align="center" label="操作" width="400">
                    <template #default="{row}">
                                                                        <el-button class="button button-8" v-if="isAuth('dianpuxinxi','修改')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning">修改</el-button>
                        <el-popconfirm  v-if="isAuth('dianpuxinxi','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
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

</template>

<style scoped>
.page-background {
	padding: 20px;
	background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
	background-size: 400% 400%;
	animation: gradient 15s ease infinite;
  height: 100%;
}

@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}

	50% {
		background-position: 100% 50%;
	}

	100% {
		background-position: 0% 50%;
	}
}

:deep(.el-card) {
	background-color: rgba(255, 255, 255, 0.9);
}

.button-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 20px;
}

.button {
	padding: 10px 20px;
	border: 2px solid #1f2937;
	border-radius: 8px;
	font-size: 16px;
	cursor: pointer;
	transition: all 0.2s ease-in-out;
	font-weight: 600;
	box-shadow: 4px 4px 0px #1f2937;
	text-transform: uppercase;
	letter-spacing: 1px;
}

.button:hover {
	transform: translate(2px, 2px);
	box-shadow: 2px 2px 0px #1f2937;
}

.button:active {
	transform: translate(4px, 4px);
	box-shadow: 0px 0px 0px #1f2937;
}


/* 不同样式的按钮 */
.button-6 {
	background: #ef4444;
	color: white;
}

.button-7 {
	background: #3b82f6;
	color: white;
}

.button-8 {
	background: #22c55e;
	color: white;
}
</style>
