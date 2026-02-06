
<script setup lang="ts">
import {menu} from '@/utils/menu'
import { toRaw } from "@vue/reactivity";
import { Session } from '@/utils/storage';
import { ref,reactive,toRefs,defineAsyncComponent } from "vue";
import {GetUsersToken} from '@/api/auth'
   import {useRoute,useRouter} from 'vue-router'
   import { Key } from '@/stores/auth';
const Register=defineAsyncComponent(()=>import('@/views/register/index.vue'));
const Login=defineAsyncComponent(()=>import('@/views/login/index.vue'));

const Cart=defineAsyncComponent(()=>import('@/views/cart/cart.vue'));
   const route=useRoute();
   const router = useRouter();
const state=reactive({
  menuList: [],
  role:"",
  user: {},
islogin:''
})
state.role = Session.get('role')
const { menuList,role,user,islogin} = {...toRefs(state)};
const menus = menu.list()
state.menuList = toRaw(menus);
 if(Session.get(Key.isLoingKey)==null){
    state.islogin='0';
}else{
    state.islogin=Session.get(Key.isLoingKey);
}
console.log(state.menuList);

   function menuHandler(name:any) {
      name = '/'+name
      router.push(name)
    }

       if(state.islogin=='1'){
        getutoken();
    }


    async function getutoken(){
  try {
    const {data} = await GetUsersToken();
    state.user=data;
      } catch (error) {

     }

    }
    const CartRef=ref();
    function gwc() {
        CartRef.value.openinit();
    }
            const WdRef=ref();
    function wd() {
      WdRef.value.openaddOrupdate();
    }
   

const LoginRef=ref();
function dl(){
  LoginRef.value.showlogin();
}
const RegisterRef=ref();
function  register(tableName) {
  RegisterRef.value.open(tableName);
}

    function tc(){
       Session.remove(Key.accessTokenKey);
       Session.remove("tableName");
        Session.remove("role");
        Session.remove("adminName");
        Session.set(Key.isLoingKey,'0');
        state.islogin='0';
       router.push("/")
    }
</script>
<template>



  <!-- 导航栏 - 美食主题 -->
  <nav>
    <div>
      <!-- Logo - 顶部 -->
      <div>
        <i class="fas fa-mountain text-2xl" style="color: #ff6b35;"></i>
        <span style="font-size: 18px; font-weight: 700; color: #ff6b35;">基于CI/CD的电商管理平台</span>
      </div>

      <!-- 菜单和按钮 - 同一行 -->
      <div>
        <!-- 菜单 - 未登录 -->
        <div v-if="islogin=='0'">
          <div v-for="item in menuList" :key="item.roleName">
            <div v-if="'游客'==item.roleName">
              <a @click="menuHandler(`home`)">首页</a>
              <a v-for="(menu, index1) in item.ykMenu" :key="index1" @click="menuHandler(menu.child[0]?.tableName)">{{ menu.menu }}</a>
            </div>
          </div>
        </div>

        <!-- 菜单 - 已登录 -->
        <div v-if="islogin=='1'">
          <div v-for="item in menuList" :key="item.roleName">
            <div v-if="role==item.roleName">
              <a @click="menuHandler(`home`)">首页</a>
              <a v-for="(menu, index1) in item.frontMenu" :key="index1" @click="menuHandler(menu.child[0]?.tableName)">{{ menu.menu }}</a>
              <a @click="menuHandler('grzx')">个人中心</a>
              <a @click="gwc()">购物车</a>
              <a @click="menuHandler('aichat')">AI购物助手</a>
                          </div>
          </div>
        </div>

        <!-- 按钮 -->
        <div>
          <button v-if="islogin=='0'" @click="dl()">登录</button>
          <button v-if="islogin=='0'" @click="register('yonghu')">注册用户</button>
        
          <button v-if="islogin=='1'" @click="tc">退出</button>
        </div>
      </div>
    </div>
  </nav>




  <Register ref="RegisterRef" v-if="islogin=='0'"></Register>
  <Login ref="LoginRef" v-if="islogin=='0'"></Login>


    <Cart ref="CartRef" v-if="islogin=='1'"></Cart>
    
</template>

<style scoped>

</style>
