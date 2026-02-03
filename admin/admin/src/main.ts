import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
// 整合ElementPlus
import ElementPlus from 'element-plus';
// @ts-ignore 忽略ts检查
import zhCn from 'element-plus/dist/locale/zh-cn.mjs';
import { useElIcon } from '@/utils/setGlobal';
import Layui from '@layui/layui-vue'
import '@layui/layui-vue/lib/index.css'
// 导入全局样式
import '@/styles/index.scss';
const app = createApp(App);
import './assets/main.css';
import '@fortawesome/fontawesome-free/css/all.css';
app.use(createPinia());
app.use(router);
app.use(Layui);
// 使用ElementPlus，并且中文
app.use(ElementPlus, {locale: zhCn});
useElIcon(app); // 注册ElementPlus图标
app.mount('#app');
