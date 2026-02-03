<script setup lang="ts">
     import { defineAsyncComponent,reactive,ref,toRefs } from 'vue';
     import { toRaw } from "@vue/reactivity";
     import { Key } from '@/stores/auth';
     import { Session } from '@/utils/storage';
     import request from "@/utils/request";
     import {notify,confirm} from '@/utils/element';
     import { isAuth } from '@/utils/utils';
     import {exportExcel} from '@/utils/exportExcel';
     import printJS from 'print-js'
     import { layer } from '@layui/layui-vue';
     const AddEdit=defineAsyncComponent(()=>import('@/views/appointment/add-edit.vue'));
const state=reactive({
    query:{
                                
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
const { query,tableList,page,ids
     } = {...toRefs(state)};
    
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
        if (state.query.username != '' && state.query.username != undefined) {
            params['username'] = '%' + state.query.username + '%'
        }

    request({
        url:'appointment/page',
        method:'post',
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


    layer.confirm("是否要删除",
                 {
                     btn: [
                         {text:'确认', callback: (id) => {
                             request({
                     url:`appointment/delete`,
                         method:'post',
                 data:[row.id]
     }).then(({data})=>{
             layer.msg("删除成功", { time: 1000, icon: 1 })
         layer.close(id);
         getDateList();

     })
     }
     },
         {text:'取消', callback: (id) => {

             layer.close(id); }
         }
     ]
     }
     );


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

    if(state.ids.length==0){
          layer.msg("多选删除项不能为空", { icon : 2, time: 1000})
          return;
      }else{
          request({
              url:`appointment/delete`,
              method:'post',
              data:state.ids
          }).then(({data})=>{
              notify("删除成功",{type:'success'});
          getDateList();

      })
      }


   
  }


const users=Session.get(Key.userInfoKey);

const editRef=ref();




const columns = ref([

{ title:"选项", width: "55px", type: "checkbox", fixed: "left" },
{ title:"预约名称",key:"title"},
{ title:"预约人",key:"username"},
{ title:"状态",key:"type"},
{ title:"操作", width: "150px", customSlot:"operator", key:"operator", fixed: "right", ignoreExport: true }]);




         


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

        
                <el-form-item label="预约名称"  prop="title">
                    <el-input v-model="query.title" maxlength="100" placeholder="预约名称" clearable style="width: 200px;"/>
                </el-form-item>
                <el-form-item label="预约人"  prop="username">
                    <el-input v-model="query.username" maxlength="100" placeholder="预约人" clearable style="width: 200px;"/>
                </el-form-item>


                <el-form-item>
                <lay-button type="primary" @click="handleQuery()">查询</lay-button>
                <lay-button v-if="isAuth('qichexinxi','删除')" type="danger" @click="listdel()">多选删除</lay-button>
                            </el-form-item>
        </el-form>





        <div style="height: 400px;">
             <lay-table :height="'100%'"
                        :columns="columns"
                        :data-source="tableList"
                        v-model:selected-keys="ids">
                 <template v-slot:operator="{ row }">
                     <lay-button size="xs" type="danger" @click="handleDelete(row)" >删除</lay-button>
                 </template>

             </lay-table>
         </div>



        <!-- <el-table
            class="w100"
            ref="tableListRef"
            :data="tableList"
            border
            stripe
            @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="55" />



            <el-table-column header-align="center"  align="center" prop="title" label="预约名称">

        <template #default="{row}">
            {{row.title}}
        </template>

    </el-table-column>

    


 

                <el-table-column header-align="center"  align="center" prop="username" label="用户名">

        <template #default="{row}">
            {{row.username}}
        </template>

    </el-table-column>

                <el-table-column header-align="center"  align="center" prop="type" label="状态">

        <template #default="{row}">
            {{row.type}}
        </template>

    </el-table-column>

                        <el-table-column fixed="right" align="center" label="操作" width="160">
                <template #default="{row}">
                    <el-popconfirm  v-if="isAuth('appointment','删除')"  width="auto" @confirm="handleDelete(row)"  :title="`确定永久删除吗？`">
                        <template #reference>
                            <el-button icon="ele-Delete" type="danger" link>删除</el-button>
                        </template>
                    </el-popconfirm>
                </template>
            </el-table-column>
        </el-table> -->

        <!-- 分页 -->
        <m-page :page="page" @pageChange="getDateList"/>

        <AddEdit ref="editRef" @refresh="getDateList"/>
    </div>
</el-card>


</template>

<style scoped>

</style>