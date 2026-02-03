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

  const AddEdit=defineAsyncComponent(()=>import('@/views/shangpinfenlei/add-edit.vue'));
        const state=reactive({
          query:{
                                                                                fenleimingcheng:'',
                                                    fenleitupian:'',
                    
    },
    page:{
      current:1,
      size:10,
      total:0
    },
          tableList:[],
    ids:[] as any[],
    isdel:true,
      
        })
  const { query,tableList,page,isdel
                          } = {...toRefs(state)};


      


  //进入执行
  getDateList();
  //获取列表
  function getDateList(){
    const params={
      page: state.page.current,
      limit: state.page.size,
                            }


                                                            if (state.query.fenleimingcheng != '' && state.query.fenleimingcheng != undefined) {
              params['fenleimingcheng'] = '%' + state.query.fenleimingcheng + '%'
            }
                                      if (state.query.fenleitupian != '' && state.query.fenleitupian != undefined) {
              params['fenleitupian'] = '%' + state.query.fenleitupian + '%'
            }
                    request({
      url:'shangpinfenlei/page',
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
      url:`shangpinfenlei/delete`,
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
      url:`shangpinfenlei/delete`,
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
<div class="page-background">
    <el-card shadow="never">
        <template #header>
            <div class="card_header">
                <b>商品分类列表</b>
            </div>
        </template>
        <div class="layout-padding">
            <el-form inline :model="query" label-suffix=":">

                                                                                                            
                        <el-form-item label="分类名称"  prop="fenleimingcheng">
                            <el-input v-model="query.fenleimingcheng" maxlength="100" placeholder="请输入分类名称" clearable style="width: 200px;"/>
                        </el-form-item>
                                                        
                        <el-form-item label="分类图片"  prop="fenleitupian">
                            <el-input v-model="query.fenleitupian" maxlength="100" placeholder="请输入分类图片" clearable style="width: 200px;"/>
                        </el-form-item>
                                                    <el-form-item>
                  <div class="button-container">
                    <el-button icon="ele-Search" @click="handleQuery()" class="button button-7">查询</el-button>
                    <el-button  class="button button-6" v-if="isAuth('shangpinfenlei','删除')" icon="ele-Delete" @click="listdel()" :disabled="isdel" type="danger">多选删除</el-button>
                    <el-button class="button button-8" v-if="isAuth('shangpinfenlei','新增')" icon="ele-Plus" type="success" @click="add()">新增</el-button>
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



                                                                                                                                                                                                <el-table-column header-align="center"  align="center" prop="fenleimingcheng" label="分类名称">

                                    <template #default="{row}">
                                        {{row.fenleimingcheng}}
                                    </template>

                                </el-table-column>

                                                                                                                                    

                            <el-table-column header-align="center"  align="center" prop="fenleitupian" label="分类图片">

                                <template #default="{row}">
                                    <img v-if="row.fenleitupian" :src="row.fenleitupian" width="100" height="100">
                                    <div v-else>无图片</div>
                                </template>

                            </el-table-column>
                                                                            <el-table-column fixed="right" align="center" label="操作" width="400">
                    <template #default="{row}">
                                                                        <el-button class="button button-8" v-if="isAuth('shangpinfenlei','修改')" icon="ele-Edit" @click.stop="handleEdit(row)" type="warning">修改</el-button>
                        <el-popconfirm  v-if="isAuth('shangpinfenlei','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
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
