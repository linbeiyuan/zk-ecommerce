import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
// 整合ElementPlus
import ElementPlus from 'element-plus';
// @ts-ignore 忽略ts检查
import zhCn from 'element-plus/dist/locale/zh-cn.mjs';
import { useElIcon } from '@/utils/setGlobal';


// 导入前台布局样式

const app = createApp(App);
import './assets/main.css';
import '@fortawesome/fontawesome-free/css/all.css';
import 'swiper/css';
import 'swiper/css/pagination';
// 导入全局样式
import '@/styles/index.scss';
import '@/styles/front-layout.css';
app.use(createPinia());
app.use(router);

// 使用ElementPlus，并且中文
app.use(ElementPlus, {locale: zhCn});
useElIcon(app); // 注册ElementPlus图标
app.mount('#app');
