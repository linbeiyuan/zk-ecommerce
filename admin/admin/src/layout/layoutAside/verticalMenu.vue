<script setup lang="ts" name="LayoutVerticalMenu">
import {useRoute,useRouter} from 'vue-router'
import {useLayoutConfigStore} from '@/stores/layoutConfig'
import { toRaw } from "@vue/reactivity";
import { storeToRefs } from 'pinia';
import menu from '@/utils/menu'
import { Session } from '@/utils/storage';
import { reactive,toRefs,ref } from 'vue';
const route=useRoute();
const router = useRouter();
const layoutConfig=useLayoutConfigStore();
const {isCollapse}=storeToRefs(layoutConfig);
//  console.log('isCollapse',isCollapse.value);

const props= defineProps<{
  type:number
}>();


const state=reactive({
  menuList: [] as any[],
  dynamicMenuRoutes: [] as any[],
  role: '',
  icon:[
    'ele-Calendar',
    'ele-Box',
    'ele-Money',
    'ele-Refrigerator',
    'ele-Cpu',
    'ele-Football',
    'ele-Brush',
    'ele-Suitcase',
    'ele-Monitor',
    'ele-BrushFilled',
    'ele-DataBoard',
    'ele-DataLine',
    'ele-Reading',
    'ele-FirstAidKit',
    'ele-ScaleToOriginal',
    'ele-ShoppingTrolley',
    'ele-Timer',
    'ele-Sunset',
    'ele-SwitchFilled',
    'ele-Dish',
    'ele-Dessert',
    'ele-Burger',
    'ele-GobletSquare',
    'ele-Cherry',

  ]
})

const { menuList,dynamicMenuRoutes,role,icon} = {...toRefs(state)};
const menus = menu.list()
state.menuList = toRaw(menus);
console.log("菜单",state.menuList);

state.role = Session.get('role')
function menuHandler(name:any) {
  // console.log("跳转页面:"+name);

  name = '/'+name
  router.push(name)
}


const showUserMenu = ref(false);
const submenuOpen = ref({
  pets: true,
  appointments: false
});

const toggleSubmenu = (menu: string) => {
  submenuOpen.value[menu as keyof typeof submenuOpen.value] = !submenuOpen.value[menu as keyof typeof submenuOpen.value];
};

</script>

<template>


  <!-- 左侧菜单 -->
  <aside class="fixed left-0 top-16 bottom-0 w-56 overflow-y-auto shadow backdrop-blur-sm custom-aside-bg">
    <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-400 via-cyan-400 to-blue-400"></div>
    <nav class="py-4 px-4 bg-gradient-radial from-white/10 via-white/20 to-transparent backdrop-blur-md">
  <span v-for="(item,index) in menuList" :key="item.roleName">
    <span v-if="role==item.roleName">
<a style="cursor:pointer" @click="menuHandler(`home`)" class="group flex items-center px-6 py-4 mb-4 hover:bg-white/20 relative overflow-hidden text-blue-50 hover:text-white border border-white/20 rounded-lg before:content-[''] before:absolute before:inset-0 before:border before:border-dashed before:border-blue-300/50 before:rounded-lg before:scale-105 before:opacity-0 hover:before:opacity-100 before:transition-all backdrop-blur-sm">
<div class="absolute left-0 top-0 w-1 h-full bg-blue-400 transform scale-y-0 group-hover:scale-y-100 transition-transform duration-300"></div>
<i class="fas fa-users mr-3 text-blue-300"></i>
<span class="relative font-medium py-2 text-lg">
<span class="relative">首页</span>
<span class="absolute bottom-0 left-0 w-0 h-0.5 bg-blue-400 group-hover:w-full transition-all duration-300"></span>
</span>
</a>
<a  style="cursor:pointer" @click="menuHandler(`center`)" class="group flex items-center px-6 py-4 mb-4 hover:bg-white/20 relative overflow-hidden text-blue-50 hover:text-white border border-white/20 rounded-lg before:content-[''] before:absolute before:inset-0 before:border before:border-dashed before:border-blue-300/50 before:rounded-lg before:scale-105 before:opacity-0 hover:before:opacity-100 before:transition-all backdrop-blur-sm">
<div class="absolute left-0 top-0 w-1 h-full bg-cyan-400 transform scale-y-0 group-hover:scale-y-100 transition-transform duration-300"></div>
<i class="fas fa-paw mr-3 text-blue-300"></i>
<span class="relative font-medium py-2 text-lg">
<span class="relative">个人中心</span>
<span class="absolute bottom-0 left-0 w-0 h-0.5 bg-cyan-400 group-hover:w-full transition-all duration-300"></span>
</span>
</a>
<a style="cursor:pointer" @click="menuHandler(`updatePassword`)" class="group flex items-center px-6 py-4 mb-4 hover:bg-white/20 relative overflow-hidden text-blue-50 hover:text-white border border-white/20 rounded-lg before:content-[''] before:absolute before:inset-0 before:border before:border-dashed before:border-blue-300/50 before:rounded-lg before:scale-105 before:opacity-0 hover:before:opacity-100 before:transition-all backdrop-blur-sm">
<div class="absolute left-0 top-0 w-1 h-full bg-cyan-400 transform scale-y-0 group-hover:scale-y-100 transition-transform duration-300"></div>
<i class="fas fa-calendar-alt mr-3 text-blue-300"></i>
<span class="relative font-medium py-2 text-lg">
<span class="relative">修改密码</span>
<span class="absolute bottom-0 left-0 w-0 h-0.5 bg-cyan-400 group-hover:w-full transition-all duration-300"></span>
</span>
</a>
<span v-for=" (menu,index) in item.backMenu" :key="menu.menu">
<a style="cursor:pointer" v-for=" (child,sort) in menu.child" :key="sort" @click="menuHandler(child.tableName)" class="group flex items-center px-6 py-4 mb-4 hover:bg-white/20 relative overflow-hidden text-blue-50 hover:text-white border border-white/20 rounded-lg before:content-[''] before:absolute before:inset-0 before:border before:border-dashed before:border-blue-300/50 before:rounded-lg before:scale-105 before:opacity-0 hover:before:opacity-100 before:transition-all backdrop-blur-sm">
<div class="absolute left-0 top-0 w-1 h-full bg-cyan-400 transform scale-y-0 group-hover:scale-y-100 transition-transform duration-300"></div>
<i class="mr-3 text-blue-300">
  <SvgIcon :name="icon[index]" />
</i>
<span class="relative font-medium py-2 text-lg">
<span class="relative">{{ child.menu }}</span>
<span class="absolute bottom-0 left-0 w-0 h-0.5 bg-cyan-400 group-hover:w-full transition-all duration-300"></span>
</span>
</a>
</span>
</span>
</span>
    </nav>
  </aside>
</template>

<style scoped>
.custom-aside-bg {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  animation: gradient 10s ease infinite;
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
.menu-item {
  transition: all 0.3s;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>