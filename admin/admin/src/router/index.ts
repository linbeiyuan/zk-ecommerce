
import { createRouter, createWebHistory,createWebHashHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router';
import { Session } from '@/utils/storage';
import { Key } from '@/stores/auth';

export const dynamicRoutes: RouteRecordRaw[] = [
    {
        path: "/",
        name: "layout", // layout 的 children 数组为用户菜单页面的集合
        redirect: "/home",
        component: () => import('@/layout/index.vue'),
        children: [
            {
                path: "/home",
                name: "home",
                meta: {
                    hideInMenu: false, // 该菜单是否隐藏；true 为隐藏
                    title: "首页",
                    cache: true, // 为true，则缓存菜单
                    icon: "&#xe611;", // 图标
                },
                component: () => import("@/views/home.vue"),
            },
            {
                path: "/cen",
                name: "cen",
                meta: {
                    title: "个人信息",
                    icon: "&#xe7fc;", // 图标
                },
                redirect:'/center',
                children: [
                    {
                        path: "/center",
                        name: "center",
                        meta: {
                            title: "个人信息",
                            icon: "&#xe90f;", // 图标
                        },
                        component: () => import("@/views/center.vue"),
                    },

                ],
            },
            {
                path: "/updatePassword",
                name: "updatePassword",
                meta: {
                    title: "修改密码",
                    icon: "&#xe7fc;", // 图标
                },
                redirect:'/updatePassword',
                children: [
                    {
                        path: "/updatePassword",
                        name: "updatePassword",
                        meta: {
                            title: "修改密码",
                            icon: "&#xe90f;", // 图标
                        },
                        component: () => import("@/views/update-password.vue"),
                    },

                ],
            },




                            {
                    path: "/crk",
                    name: "crk",
                    meta: {
                        title: "出入库管理",
                        icon: "&#xe7fc;", // 图标
                    },
                    redirect:'/crk',
                    children: [
                        {
                            path: "/crk",
                            name: "crk",
                            meta: {
                                title: "出入库管理",
                                icon: "&#xe90f;", // 图标
                            },
                            component: () => import("@/views/crk/index.vue"),
                        },

                    ],
                },
            

            {
                path: "/forum",
                name: "forum",
                meta: {
                    title: "购物论坛管理",
                    icon: "&#xe7fc;", // 图标
                },
                redirect:'/forum',
                children: [
                    {
                        path: "/forum",
                        name: "forum",
                        meta: {
                            title: "购物论坛管理",
                            icon: "&#xe90f;", // 图标
                        },
                        component: () => import("@/views/forum/index.vue"),
                    },

                ],
            },


            
                
                    {
                        path: "/orders/:status",
                        name: "orders",
                        meta: {
                            title: "订单管理",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/orders',
                        children: [
                            {
                                path: "/orders/:status",
                                name: "orders",
                                meta: {
                                    title: "订单管理",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/orders/index.vue"),
                            },

                        ],
                    },
                    {
                        path: "/salesStatistics",
                        name: "salesStatistics",
                        meta: {
                            title: "销量统计",
                            icon: "&#xe7fc;", // 图标
                        },
                        component: () => import("@/views/salesStatistics/index.vue"),
                    },
                    {
                        path: "/letter",
                        name: "letter",
                        meta: {
                            title: "联系",
                            icon: "&#xe7fc;", // 图标
                        },
                        component: () => import("@/views/letter/list.vue"),
                    },


                
            
                                    {
                        path: "/news",
                        name: "news",
                        meta: {
                            title: "平台通知",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/news',
                        children: [
                            {
                                path: "/news",
                                name: "news",
                                meta: {
                                    title: "平台通知",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/news/index.vue"),
                            },

                        ],
                    },

                
            
                                    {
                        path: "/wodeshouzangguanli",
                        name: "wodeshouzangguanli",
                        meta: {
                            title: "我的收藏",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/wodeshouzangguanli',
                        children: [
                            {
                                path: "/wodeshouzangguanli",
                                name: "wodeshouzangguanli",
                                meta: {
                                    title: "我的收藏",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/storeup/index.vue"),
                            },

                        ],
                    },
                
            
                 		 {
                        path: "/wenzhen",
                        name: "wenzhen",
                        meta: {
                            title: "问诊",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/wenzhen',
                        children: [
                            {
                                path: "/wenzhen",
                                name: "wenzhen",
                                meta: {
                                    title: "问诊",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/wd/index.vue"),
                            },
                        ],
                    },
                
            
                                    {
                        path: "/messagess",
                        name: "messagess",
                        meta: {
                            title: "在线留言",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/messagess',
                        children: [
                            {
                                path: "/messagess",
                                name: "messagess",
                                meta: {
                                    title: "在线留言",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/messagess/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/shangpinguanli",
                        name: "shangpinguanli",
                        meta: {
                            title: "商品管理",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/shangpinguanli',
                        children: [
                            {
                                path: "/shangpinguanli",
                                name: "shangpinguanli",
                                meta: {
                                    title: "商品管理",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/shangpinguanli/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/discussshangpinguanli",
                        name: "/discussshangpinguanli",
                        meta: {
                            title: "商品管理评论",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/discussshangpinguanli',
                        children: [
                            {
                                path: "/discussshangpinguanli",
                                name: "discussshangpinguanli",
                                meta: {
                                    title: "商品管理评论",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/discussshangpinguanli/index.vue"),
                            },

                        ],
                    },





                
            
                                    {
                        path: "/shangpinfenlei",
                        name: "shangpinfenlei",
                        meta: {
                            title: "商品分类",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/shangpinfenlei',
                        children: [
                            {
                                path: "/shangpinfenlei",
                                name: "shangpinfenlei",
                                meta: {
                                    title: "商品分类",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/shangpinfenlei/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/dianpuxinxi",
                        name: "dianpuxinxi",
                        meta: {
                            title: "店铺信息",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/dianpuxinxi',
                        children: [
                            {
                                path: "/dianpuxinxi",
                                name: "dianpuxinxi",
                                meta: {
                                    title: "店铺信息",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/dianpuxinxi/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/discussdianpuxinxi",
                        name: "/discussdianpuxinxi",
                        meta: {
                            title: "店铺信息评论",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/discussdianpuxinxi',
                        children: [
                            {
                                path: "/discussdianpuxinxi",
                                name: "discussdianpuxinxi",
                                meta: {
                                    title: "店铺信息评论",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/discussdianpuxinxi/index.vue"),
                            },

                        ],
                    },





                
            
                                    {
                        path: "/jifenshangdian",
                        name: "jifenshangdian",
                        meta: {
                            title: "积分商店",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/jifenshangdian',
                        children: [
                            {
                                path: "/jifenshangdian",
                                name: "jifenshangdian",
                                meta: {
                                    title: "积分商店",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/jifenshangdian/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/yonghu",
                        name: "yonghu",
                        meta: {
                            title: "用户",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/yonghu',
                        children: [
                            {
                                path: "/yonghu",
                                name: "yonghu",
                                meta: {
                                    title: "用户",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/yonghu/index.vue"),
                            },

                        ],
                    },
                
            
                                    {
                        path: "/shangjia",
                        name: "shangjia",
                        meta: {
                            title: "商家",
                            icon: "&#xe7fc;", // 图标
                        },
                        redirect:'/shangjia',
                        children: [
                            {
                                path: "/shangjia",
                                name: "shangjia",
                                meta: {
                                    title: "商家",
                                    icon: "&#xe90f;", // 图标
                                },
                                component: () => import("@/views/shangjia/index.vue"),
                            },

                        ],
                    },
                
                        {
                path: "/config",
                name: "config",
                meta: {
                    title: "系统管理",
                    icon: "&#xe7fc;", // 图标
                },
                redirect:'/config',
                children: [
                    {
                        path: "/config",
                        name: "config",
                        meta: {
                            title: "轮播图列表",
                            icon: "&#xe90f;", // 图标
                        },
                        component: () => import("@/views/config/index.vue"),
                    },

                ],
            },



            {
                path: '/401',
                name: 'NoPermission',
                component: () => import('@/views/error/401.vue'),
                meta: {
                    title: '401页面',
                    icon: 'ele-Warning',
                    cache: true,
                    hidden: false,
                }
            },
            {
                path: '/:path(.*)*', //  404匹配不存在的路由
                name: 'NotFound',
                component: () => import('@/views/error/404.vue'),
                meta: {
                    title: '未找到此页面',
                    cache: true,
                    hidden: true,
                }
            },

        ],
    },
    {
        path:'/login',
        name:'Login',
        component:()=>import('@/views/login/index.vue')
    }

]

const router = createRouter({
    // 参数获取的是 vite.config.ts 中base 属性值
    history: createWebHashHistory(),
    routes: dynamicRoutes,
});


router.beforeEach((to,from)=>{
    // const token = localStorage.getItem('token');
    //用户未登录，且跳转的目标路由不是登陆页面：则跳转登录页面/login


    const token=Session.get(Key.accessTokenKey);
    console.log(token);
    if(!token && (to.path !=='/login')){
        //通过return返回一个跳转的路由对象，重定向到指定路由
        //  return router.push({path:'/login'});
        //  return {path:'/login'}


        return {path:'/login'}


    }
    //已登录,正常进入目标路由
    return true;


})

// 路由后置守卫

export default router
