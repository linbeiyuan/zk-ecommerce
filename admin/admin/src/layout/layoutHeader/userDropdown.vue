<script setup lang="ts">
import { Key } from '@/stores/auth';
import { Session } from '@/utils/storage';
import { useFullscreen,useDark } from '@vueuse/core'
import {useLayoutConfigStore} from '@/stores/layoutConfig'
import {ref,inject} from 'vue';
import {useRouter} from 'vue-router'
import { storeToRefs } from 'pinia';
const layoutConfig=useLayoutConfigStore();
const {isCollapse,globalTitle}=storeToRefs(layoutConfig)
const val=ref(false);
const router=useRouter();
const LayoutConfigStore=useLayoutConfigStore();
  

//切换全屏模式->https://www.vueusejs.com/core/useFullscreen/  或者https://vueuse.org/core/useFullscreen/
const { isFullscreen,toggle:toggleFullscreen } = useFullscreen();
    

   async function handleToggleFullscreen(){
      await toggleFullscreen();
    //  console.log('isFullscreen',isFullscreen.value);
    LayoutConfigStore.isFullscreen=isFullscreen.value;
     
    }
   //返回值是boolean值，当前是否位暗黑模式，并且会将这个状态值保存到localstorege中
   //会自动监听isDark变化，来设置对应的主题模式
const isDark=useDark({
  valueDark:'auto',//暗黑时在html元素的class属性值
  valueLight:'',//高亮时在html元素的class属性值
  initialValue:'auto'//初始属性:auto(高亮模式)|dark
});

    function changeDark(val:boolean){
     // console.log('val',val);
      LayoutConfigStore.isDrak=val;
    }

   
   const props= defineProps<{
        id:number,
        img:string,
        uname:string
    }>();


    function tc(){
       Session.remove(Key.accessTokenKey);
       Session.remove(Key.userInfoKey);
       router.push("/login")
    }
const avatarUrl = 'https://ai-public.mastergo.com/ai/img_res/8a1e2c786bb03b4538d64309baaaa932.jpg';
const showUserMenu = ref(false);
let hideTimer: number | null = null;

// 鼠标进入显示菜单
function handleMouseEnter() {
  if (hideTimer) {
    clearTimeout(hideTimer);
    hideTimer = null;
  }
  showUserMenu.value = true;
}

// 鼠标离开2秒后隐藏菜单
function handleMouseLeave() {
  hideTimer = setTimeout(() => {
    showUserMenu.value = false;
  }, 2000);
}

</script>

<template>
  <header class="fixed top-0 left-0 right-0 h-16 shadow-md z-50 flex items-center justify-between px-6 animated-gradient">
    <div class="flex items-center">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" class="h-8 w-8 mr-3">
        <path d="M19.43,12.98c.04-.32.07-.64.07-.98s-.03-.66-.07-.98l2.11-1.65c.19-.15.24-.42.12-.64l-2-3.46c-.12-.22-.39-.3-.61-.22l-2.49,1c-.52-.4-1.08-.73-1.69-.98l-.38-2.65C14.46,2.18,14.25,2,14,2h-4c-.25,0-.46.18-.49.42l-.38,2.65c-.61.25-1.17.59-1.69.98l-2.49-1c-.23-.09-.49,0-.61.22l-2,3.46c-.13.22-.07.49.12.64l2.11,1.65c-.04.32-.07.65-.07.98s.03.66.07.98l-2.11,1.65c-.19-.15-.24.42-.12.64l2,3.46c.12.22.39.3.61.22l2.49-1c.52.4,1.08.73,1.69.98l.38,2.65c.03.24.24.42.49.42h4c.25,0,.46-.18.49-.42l.38-2.65c.61-.25,1.17-.59,1.69-.98l2.49,1c.23.09.49,0,.61-.22l2-3.46c.12-.22.07-.49-.12-.64l-2.11-1.65Z"/>
      </svg>
      <h1 class="text-xl text-white font-medium">基于CI/CD的电商管理平台</h1>
    </div>
    <div class="flex items-center">
      <span style="margin-right: 20px; color: white;">{{ Session.get("role") }} : {{ Session.get("adminName") }}</span>
      <div class="relative" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
        <img :src="avatarUrl" class="w-10 h-10 rounded-full cursor-pointer">
        <div v-show="showUserMenu" class="absolute top-12 right-0 bg-white shadow-lg rounded-lg py-2 w-40">
            <a @click="router.push('/center')" class="block px-4 py-2 hover:bg-gray-100">个人信息</a>
            <a @click="tc" class="block px-4 py-2 hover:bg-gray-100">退出登录</a>
        </div>
      </div>
    </div>
  </header>

</template>

<style scoped>
.animated-gradient {
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
</style>