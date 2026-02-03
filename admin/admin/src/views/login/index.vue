<template>
  <section>
    <div class="box" :class="{ 'login-success': isLoginSuccess }">
      <div class="square" style="--i:0;"></div>
      <div class="square" style="--i:1;"></div>
      <div class="square" style="--i:2;"></div>
      <div class="square" style="--i:3;"></div>
      <div class="square" style="--i:4;"></div>
      <div class="square" style="--i:5;"></div>

      <div class="container">
        <div class="form">
          <h2>电商平台管理系统</h2>
          <form @submit.prevent="handleSubmit">
            <div class="inputBx">
              <input type="text" required v-model="loginData.username">
              <span class="floating-label">账号</span>
              <i class="icon-slot">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" fill="currentColor">
                  <path
                    d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z" />
                </svg>
              </i>
            </div>
            <div class="inputBx password">
              <input id="password-input" :type="showPassword ? 'text' : 'password'" required
                v-model="loginData.password">
              <span class="floating-label">密码</span>
              <a href="#" class="password-control" @click.prevent="togglePassword" :class="{ view: showPassword }"></a>
              <i class="icon-slot">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" fill="currentColor">
                  <path
                    d="M144 144v48H304V144c0-44.2-35.8-80-80-80s-80 35.8-80 80zM80 192V144C80 64.5 144.5 0 224 0s144 64.5 144 144v48h16c35.3 0 64 28.7 64 64V448c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V256c0-35.3 28.7-64 64-64H80z" />
                </svg>
              </i>
            </div>

            <!-- Captcha -->
            <div class="inputBx captcha-box">
              <div class="input-wrapper">
                <input type="text" required v-model="formData.captcha" maxlength="4">
                <span class="floating-label">验证码</span>
                <i class="icon-slot">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" fill="currentColor">
                    <path
                      d="M0 256C0 220.7 28.7 192 64 192H192c0-35.3 28.7-64 64-64s64 28.7 64 64H448c35.3 0 64 28.7 64 64s-28.7 64-64 64H320c0 35.3-28.7 64-64 64s-64-28.7-64-64H64c-35.3 0-64-28.7-64-64zm192-96a96 96 0 1 0 0 192 96 96 0 1 0 0-192z" />
                  </svg>
                </i>
              </div>
              <div ref="captchaRef" @click="refreshCaptcha" class="captcha-image">
                <div class="relative">
                  <span v-for="(char, index) in captchaCode" :key="index" :style="{
                    color: getRandomColor(),
                    transform: `rotate(${Math.random() * 30 - 15}deg)`,
                    marginRight: '4px',
                    display: 'inline-block',
                    userSelect: 'none'
                  }" class="captcha-char">{{ char }}</span>
                </div>
                <!-- Interference lines -->
                <div v-for="n in 3" :key="n" :style="{
                  position: 'absolute',
                  width: '100%',
                  height: '2px',
                  background: getRandomColor(),
                  top: `${Math.random() * 100}%`,
                  left: 0,
                  transform: `rotate(${Math.random() * 360}deg)`
                }"></div>
                <!-- Interference dots -->
                <div v-for="n in 20" :key="`dot-${n}`" :style="{
                  position: 'absolute',
                  width: '2px',
                  height: '2px',
                  background: getRandomColor(),
                  top: `${Math.random() * 100}%`,
                  left: `${Math.random() * 100}%`,
                  borderRadius: '50%'
                }"></div>
              </div>
            </div>
            <div v-if="captchaError" class="captcha-error-msg">验证码错误，请重新输入</div>


            <!-- Role selection -->
            <div class="inputBx">
              <div class="roles-container">
                <span v-for="item in menus" :key="item.roleName">
                  <label class="role-label" v-if="item.roleName !== '游客' &&item.roleName !== '用户'">
                    <input type="radio" :value="item.roleName" v-model="loginData.role">
                    <span class="role-name">{{ item.roleName }}</span>
                  </label>
                </span>
              </div>
            </div>

            <div class="inputBx">
              <input type="submit" @click="handleSubmit" value="登录" :disabled="!isFormValid">
            </div>
          </form>

          <p>没有账号?
                
                        /
                                    <a href="#" @click.prevent="register('shangjia', '商家注册')">商家注册</a>
                                  </p>
        </div>
      </div>
    </div>
  </section>
  <Register ref="RegisterRef" />
</template>
<script lang="ts" setup>
import { ref, reactive, computed, toRefs, defineAsyncComponent, onMounted } from 'vue';
import { isUsername, isPassword } from '@/utils/validate';
import { useAuthStore } from '@/stores/auth';
import { useRouter, useRoute } from 'vue-router';
import { Session } from '@/utils/storage';
import type { FormRules } from 'element-plus/es/components/form/src/types';
import menu from "@/utils/menu";
import { notify, confirm } from '@/utils/element';
const Register = defineAsyncComponent(() => import('@/views/login/register.vue'));
const authStore = useAuthStore();
const isLoginSuccess = ref(false);

const router = useRouter();
const route = useRoute();

const formRef = ref();

const state = reactive({
  loading: false,
  registerloading: false,
  loginData: {
    username: '',
    password: '',
    role: ''
  } as LoginData,
  tableName: ''
});

const menus = menu.list();

const { loading, loginData, tableName } = { ...toRefs(state) };
const RegisterRef = ref();
function register(tableName: any, title: string) {
  RegisterRef.value.open(tableName, title);
}
const backgroundUrl = 'https://ai-public.mastergo.com/ai/img_res/8cfadc098b6d4c07a01819809ef3e25d.jpg';
const showPassword = ref(false);
const formData = ref({

  captcha: ''
});
const captchaRef = ref<HTMLDivElement | null>(null);
const captchaCode = ref('');
const captchaError = ref(false);
const getRandomChar = () => {
  const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  return chars[Math.floor(Math.random() * chars.length)];
};
const getRandomColor = () => {
  const colors = ['#000', '#333', '#666'];
  return colors[Math.floor(Math.random() * colors.length)];
};
const generateCaptcha = () => {
  let code = '';
  for (let i = 0; i < 4; i++) {
    code += getRandomChar();
  }
  return code;
};
const refreshCaptcha = () => {
  captchaCode.value = generateCaptcha();
  captchaError.value = false;
  formData.value.captcha = '';
};
onMounted(() => {
  refreshCaptcha();
});
const isFormValid = computed(() => {
  return state.loginData.username &&
    state.loginData.password &&
    state.loginData.role &&
    formData.value.captcha;
});
const togglePassword = () => {
  showPassword.value = !showPassword.value;
};
const handleSubmit = async () => {
  if (!isFormValid.value) return;
  if (formData.value.captcha.toUpperCase() !== captchaCode.value) {
    captchaError.value = true;
    refreshCaptcha();
    return;
  }
  captchaError.value = false;

  for (let i = 0; i < menus.length; i++) {
    if (menus[i].roleName == loginData.value.role) {
      state.tableName = menus[i].tableName;
    }
  }

  const res = await authStore.userLogin(state.loginData, `${state.tableName}/login`);
  isLoginSuccess.value = true;
  // console.log('submitForm', res);
  // 跳转到来源地址  login?redirect=/home
  setTimeout(() => {
    Session.set("tableName", state.tableName);
    Session.set("role", state.loginData.role);
    Session.set("adminName", state.loginData.username);
    router.replace({ path: <string>route.query?.redirect || '/' });
  }, 1500)

};

</script>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=El+Messiri:wght@700&display=swap');

* {
  margin: 0;
  padding: 0;
  font-family: 'El Messiri', sans-serif;
}

.fas {
  width: 32px;
}

section {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
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

.box {
  position: relative;

  .square {
    position: absolute;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(5px);
    box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    animation: square 10s linear infinite;
    animation-delay: calc(-1s * var(--i));
  }

  @keyframes square {

    0%,
    100% {
      transform: translateY(-20px);
    }

    50% {
      transform: translateY(20px);
    }
  }

  .square:nth-child(1) {
    width: 100px;
    height: 100px;
    top: -15px;
    right: -45px;
  }

  .square:nth-child(2) {
    width: 150px;
    height: 150px;
    top: 105px;
    left: -125px;
    z-index: 2;
  }

  .square:nth-child(3) {
    width: 60px;
    height: 60px;
    bottom: 85px;
    right: -45px;
    z-index: 2;
  }

  .square:nth-child(4) {
    width: 50px;
    height: 50px;
    bottom: 35px;
    left: -95px;
  }

  .square:nth-child(5) {
    width: 50px;
    height: 50px;
    top: -15px;
    left: -25px;
  }

  .square:nth-child(6) {
    width: 85px;
    height: 85px;
    top: 165px;
    right: -155px;
    z-index: 2;
  }
}

.container {
  position: relative;
  padding: 50px;
  width: 360px;
  min-height: 380px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  border-radius: 10px;
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.2);
}

.container::after {
  content: '';
  position: absolute;
  top: 5px;
  right: 5px;
  bottom: 5px;
  left: 5px;
  border-radius: 5px;
  pointer-events: none;
  background: linear-gradient(to bottom, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.1) 2%);
}

.form {
  position: relative;
  width: 100%;
  height: 100%;

  h2 {
    color: #fff;
    letter-spacing: 2px;
    margin-bottom: 30px;
    text-align: center;
    font-size: 30px;
  }

  .inputBx {
    position: relative;
    width: 100%;
    margin-bottom: 20px;

    input {
      width: 100%;
      box-sizing: border-box;
      outline: none;
      border: none;
      border: 1px solid rgba(255, 255, 255, 0.2);
      background: rgba(255, 255, 255, 0.2);
      padding: 8px 10px;
      padding-left: 40px;
      border-radius: 15px;
      color: #fff;
      font-size: 16px;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }

    .password-control {
      position: absolute;
      top: 11px;
      right: 10px;
      display: inline-block;
      width: 20px;
      height: 20px;
      background: url(https://snipp.ru/demo/495/view.svg) 0 0 no-repeat;
      transition: 0.5s;
    }

    .view {
      background: url(https://snipp.ru/demo/495/no-view.svg) 0 0 no-repeat;
      transition: 0.5s;
    }

    .icon-slot {
      position: absolute;
      top: 10px;
      left: 13px;
      width: 16px;
      height: 16px;
      color: #fff;
    }

    .fas {
      position: absolute;
      top: 13px;
      left: 13px;
    }

    input[type="submit"] {
      background: #fff;
      color: #111;
      max-width: 100px;
      padding: 8px 10px;
      box-shadow: none;
      letter-spacing: 1px;
      cursor: pointer;
      transition: 1.5s;
    }

    input[type="submit"]:disabled {
      background: #ccc;
      cursor: not-allowed;
    }

    input[type="submit"]:hover:not(:disabled) {
      background: linear-gradient(115deg,
          rgba(0, 0, 0, 0.10),
          rgba(255, 255, 255, 0.25));
      color: #fff;
      transition: .5s;
    }

    input::placeholder {
      color: #fff;
    }

    span.floating-label {
      position: absolute;
      left: 30px;
      padding: 10px;
      display: inline-block;
      color: #fff;
      transition: .5s;
      pointer-events: none;
    }

    input:focus~span.floating-label,
    input:valid~span.floating-label {
      transform: translateX(-30px) translateY(-25px);
      font-size: 12px;
    }

    &.captcha-box {
      display: flex;
      align-items: center;
      gap: 10px;

      .input-wrapper {
        flex-grow: 1;
        position: relative;

        input {
          width: 100%;
        }
      }

      .captcha-image {
        width: 80px;
        height: 32px;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.75);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .captcha-image .captcha-char {
        font-size: 0.9rem;
        font-weight: bold;
      }
    }

    .roles-container {
      display: flex;
      gap: 10px;
      padding: 10px;
      background: rgba(255, 255, 255, 0.2);
      border-radius: 15px;
      justify-content: center;
      flex-wrap: nowrap;
    }

    .role-label {
      display: flex;
      align-items: center;
      color: #fff;
      cursor: pointer;

      input[type="radio"] {
        width: auto;
        margin-right: 5px;
        accent-color: #fff;
      }

      .role-name {
        position: static;
        padding: 0;
        pointer-events: auto;
        transition: none;
      }
    }

  }

  .captcha-error-msg {
    color: #ff4d4d;
    font-size: 12px;
    margin-top: -15px;
    margin-bottom: 10px;
  }


  p {
    color: #fff;
    font-size: 15px;
    margin-top: 5px;

    a {
      color: #fff;
    }

    a:hover {
      background-color: #000;
      background-image: linear-gradient(to right, #434343 0%, black 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }
}

.box.login-success .container {
  animation: fadeOutAndShrink 1s forwards;
}

.box.login-success .square {
  animation: scatter 1.5s forwards ease-out;
}

@keyframes fadeOutAndShrink {
  from {
    opacity: 1;
    transform: scale(1);
  }

  to {
    opacity: 0;
    transform: scale(0.5);
  }
}

@keyframes scatter {
  to {
    transform: translate(var(--tx), var(--ty)) scale(0.5);
    opacity: 0;
  }
}

.box.login-success .square:nth-child(1) {
  --tx: 100vw;
  --ty: -100vh;
}

.box.login-success .square:nth-child(2) {
  --tx: -100vw;
  --ty: -100vh;
}

.box.login-success .square:nth-child(3) {
  --tx: 100vw;
  --ty: 100vh;
}

.box.login-success .square:nth-child(4) {
  --tx: -100vw;
  --ty: 100vh;
}

.box.login-success .square:nth-child(5) {
  --tx: -100vw;
  --ty: -50vh;
}

.box.login-success .square:nth-child(6) {
  --tx: 100vw;
  --ty: 50vh;
}
</style>
