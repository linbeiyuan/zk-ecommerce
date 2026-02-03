<template>
  <div class="bg-gray-60">
    <div class="container mx-auto px-4 py-8 max-w-8xl">
    <div class="main-content">
        <div class="table-content">

            <el-card>
                <el-table
                        :data="storeupList"
                        style="width: 100%;"
                        :cell-style="rowStyle"
                >
                    <el-table-column
                            fixed
                            prop="name"
                            label="收藏名称"
                    >
                    </el-table-column>
                    <el-table-column
                            prop="addtime"
                            label="收藏时间"
                    >
                    </el-table-column>
                    <el-table-column
                            prop="picture"
                            label="图片"
                    >
                        <template  #default="{row}">
                            <img :src="row.picture" style="width: 100px;height: 100px;">
                        </template>
                    </el-table-column>

                    <el-table-column
                            label="操作">

                        <template #default="{row}">
                            <el-button
                                    size="mini"
                                    type="danger"
                                    @click="delstoreup(row)">取消收藏</el-button>
                        </template>

                    </el-table-column>
                </el-table>


                


            </el-card>
            <m-page :page="storeuppage" @pageChange="getstoreup"/>
        </div>
    </div>
    </div>
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
      const state=reactive({
          storeupList:[],
          user:{},
          storeuppage:{
              current:1,
              size:10,
              total:0,
          },
      })


      const {storeupList,user,storeuppage} = {...toRefs(state)};


            let sessionTable = Session.get("tableName")
              request({
                url: sessionTable + '/session',
                method: "get"
            }).then((data) => {
                if (data && data.code === 0) {

                state.user = data.data;
                state.ruleForm=data.data;
            } else {

        notify(data.msg,{type:'error'});
            }
        });





            getstoreup();


           function getstoreup(){
                  request({
                    url:'storeup/list',
                    method:'get',
                    params:{
                        page: state.storeuppage.current,
                        limit: state.storeuppage.size,
                        type: 1,
                        userid: state.user.id
                    }
                }).then((data)=>{
                    state.storeupList=data.data.list;
                state.storeuppage.total=data.data.total;
            })
            }



           function delstoreup(item){
                   confirm('删除该信息吗, 是否继续?').then(() => {

                       request({
                    url:`storeup/delete`,
                    method:'post',
                    data:[item.id]
                }).then((data) => {
                    if (data && data.code === 0) {


                   notify("取消成功",{type:'success'});

                    getstoreup();

                } else {
                   notify(data.msg,{type:'error'});
                }
            });






            })
            }







</script>

