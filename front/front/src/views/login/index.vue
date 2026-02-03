

<!-- 代码已包含 CSS：使用 TailwindCSS , 安装 TailwindCSS 后方可看到布局样式效果 -->
<template>
    <div class="fixed inset-0 flex items-center justify-center" v-if="dialogFormVisible" style="z-index: 999;">
    <div class="absolute inset-0 bg-black bg-opacity-50" @click="closeModal"></div>
    <div class="relative bg-white w-[480px] rounded-lg shadow-xl p-8">
      <!-- 系统标题 -->
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-gray-800">电商平台登录</h2>
        <div class="mt-2 h-[1px] bg-gray-200"></div>
      </div>
      <!-- 登录表单 -->
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- 角色选择 -->
        <div class="flex items-center justify-center space-x-8">
          <!-- <label class="flex items-center cursor-pointer" v-for="item in menus" type="radio">
          <input v-if="item.tableName!='users' && item.roleName!='游客'" v-model="role" value="admin" class="w-4 h-4 text-blue-600">
          <span v-if="item.tableName!='users' && item.roleName!='游客'" class="ml-2">{{item.roleName}}</span>
          </label> -->
          <label class="flex items-center cursor-pointer" v-for="item in menus" type="radio">
        <span>
    <input v-if="item.tableName!='users' && item.roleName!='游客' && item.roleName!='商家'" type="radio" v-model="role" :value="item.roleName" class="w-4 h-4 text-blue-600">
    <span v-if="item.tableName!='users' && item.roleName!='游客' && item.roleName!='商家'" class="ml-2">{{item.roleName}}</span>
        </span>
          </label>
          <!-- <label class="flex items-center cursor-pointer">
          <input type="radio" v-model="role" value="guest" class="w-4 h-4 text-blue-600">
          <span class="ml-2">访客</span>
          </label> -->
        </div>
        <!-- 用户名输入框 -->
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <i class="fas fa-user text-gray-400"></i>
          </div>
          <input
              type="text"
              v-model="loginData.username"
              class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              :class="{'border-red-500': errors.username}"
              placeholder="请输入用户名"
          >
          <p v-if="errors.username" class="mt-1 text-sm text-red-500">{{ errors.username }}</p>
        </div>
        <!-- 密码输入框 -->
        <div class="relative mb-6">
          <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <i class="fas fa-lock text-gray-400"></i>
          </div>
          <input
              :type="showPassword ? 'text' : 'password'"
              v-model="loginData.password"
              class="w-full pl-10 pr-10 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              :class="{'border-red-500': errors.password}"
              placeholder="请输入密码"
          >
          <button
              type="button"
              class="absolute inset-y-0 right-0 pr-3 flex items-center"
              @click="togglePassword"
          >
            <i :class="['fas', showPassword ? 'fa-eye-slash' : 'fa-eye', 'text-gray-400']"></i>
          </button>
          <p v-if="errors.password" class="mt-1 text-sm text-red-500">{{ errors.password }}</p>
        </div>
        <!-- 验证码 -->
        <div class="flex space-x-4">
          <div class="flex-1 relative">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <i class="fas fa-shield-alt text-gray-400"></i>
            </div>
            <input
                type="text"
                v-model="loginData.valicode"
                class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                :class="{'border-red-500': errors.captcha}"
                placeholder="请输入验证码"
                maxlength="4"
            >
            <p v-if="errors.captcha" class="mt-1 text-sm text-red-500">{{ errors.captcha }}</p>
          </div>
          <div
              class="w-32 h-10 bg-gray-100 rounded-lg flex items-center justify-center cursor-pointer select-none"
              @click="refreshCaptcha"
              :style="{
                  fontFamily: 'monospace',
                  fontSize: '20px',
                  fontWeight: 'bold',
                  letterSpacing: '4px',
                  background: `linear-gradient(${captchaRotation}deg, #f0f0f0, #e0e0e0)`,
                  position: 'relative',
                  overflow: 'hidden'
                  }"
          >
        <span
            v-for="(char, index) in captchaCode"
            :key="index"
            :style="{
                transform: `rotate(${Math.random() * 30 - 15}deg)`,
                display: 'inline-block',
                color: `hsl(${Math.random() * 360}, 70%, 40%)`
                }"
        >{{ char }}</span>
            <div class="absolute inset-0" style="background: radial-gradient(circle at 50% 50%, transparent 80%, rgba(255,255,255,0.3) 100%)"></div>
          </div>
        </div>
        <!-- 按钮区域 -->
        <div class="flex space-x-4">
          <button
              type="submit"
              class="flex-1 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors duration-200 !rounded-button whitespace-nowrap"
              :disabled="isLoading"
          >
            <span v-if="!isLoading">登录</span>
            <i v-else class="fas fa-spinner fa-spin"></i>
          </button>
          <button
              type="button"
              @click="closeModal"
              class="flex-1 bg-gray-200 text-gray-700 py-2 rounded-lg hover:bg-gray-300 transition-colors duration-200 !rounded-button whitespace-nowrap"
          >
            取消
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
<script lang="ts" setup>
  import { ref, reactive, toRefs,defineAsyncComponent,onMounted } from 'vue';
  import { isUsername, isPassword } from '@/utils/validate';
  import { useAuthStore } from '@/stores/auth';
  import { useRouter, useRoute } from 'vue-router';
  import { Session } from '@/utils/storage';
  import type { FormRules } from 'element-plus/es/components/form/src/types';
  import {menu} from "@/utils/menu";


  const router = useRouter();
  const route = useRoute();

  const formRef = ref();

  const state = reactive({
    loading: false,
    registerloading:false,
    loginData: {
      username: '',
      password: '',
      role:''
    } as LoginData,
    tableName:'',
    dialogFormVisible:false
  });

  const menus = menu.list();

  const { loading,loginData,tableName,dialogFormVisible } = {...toRefs(state)};
  function showlogin(){
    state.dialogFormVisible=true;
  }

  defineExpose({
    showlogin
  })
  const authStore = useAuthStore();
  const showModal = ref(true);
  const username = ref('');
  const password = ref('');
  const role = ref('user');
  const captchaInput = ref('');
  const captchaCode = ref('');
  const captchaRotation = ref(0);

  const generateCaptcha = () => {
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let result = '';
    for (let i = 0; i < 4; i++) {
      result += chars[Math.floor(Math.random() * chars.length)];
    }
    return result;
  };

  const refreshCaptcha = () => {
    captchaCode.value = generateCaptcha();
    captchaRotation.value = Math.random() * 10 - 5;
  };

  onMounted(() => {
    refreshCaptcha();
  });
  const showPassword = ref(false);
  const isLoading = ref(false);
  const errors = ref({
    username: '',
    password: '',
    captcha: ''
  });
  const closeModal = () => {
    state.dialogFormVisible = false;
  };
  const togglePassword = () => {
    showPassword.value = !showPassword.value;
  };
  const validateForm = () => {
    let isValid = true;
    errors.value = {
      username: '',
      password: '',
      captcha: ''
    };
    if (!state.loginData.username) {
      errors.value.username = '请输入用户名';
      isValid = false;
    }
    if (!state.loginData.password) {
      errors.value.password = '请输入密码';
      isValid = false;
    }
    if (!state.loginData.valicode) {
      errors.value.captcha = '请输入验证码';
      isValid = false;
    } else if (state.loginData.valicode.toUpperCase() !== captchaCode.value) {
      errors.value.captcha = '验证码错误';
      isValid = false;
    }
    return isValid;
  };
  const handleSubmit = async () => {
    if (!validateForm()) return;
    isLoading.value = true;
    try {
      // 模拟登录请求

      state.loginData.role=role.value;

      console.log(role.value);

      for (let i = 0; i < menus.length; i++) {
        if (menus[i].roleName == loginData.value.role) {
          state.tableName = menus[i].tableName;
        }
      }

      const res = await authStore.userLogin(state.loginData,`${state.tableName}/login`);
      // console.log('submitForm', res);
      // 跳转到来源地址  login?redirect=/home
      Session.set("tableName",state.tableName);
      Session.set("role", state.loginData.role);
      Session.set("adminName", state.loginData.username);
      window.location.reload();

      // await new Promise(resolve => setTimeout(resolve, 1500));
      // console.log('登录信息:', {
      // username: username.value,
      // password: password.value,
      // role: role.value
      // });
    } catch (error) {
      console.error('登录失败:', error);
    } finally {
      isLoading.value = false;
      refreshCaptcha();
      state.loginData.valicode = '';
    }
  };
</script>


