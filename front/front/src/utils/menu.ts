const menu = {
    list() {
        return [{"frontMenu":[{"child": [{
            "buttons":["查看","查看评论","回复"],
            "menu": "商品管理",
            "menuJump": "列表",
            "tableName": "shangpinguanli"
        }], "menu": "商品管理"
    },{"child": [{
            "buttons":["查看","查看评论","回复"],
            "menu": "店铺信息",
            "menuJump": "列表",
            "tableName": "dianpuxinxi"
        }], "menu": "店铺信息"
    },{"child": [{
            "buttons":["查看"],
            "menu": "积分商店",
            "menuJump": "列表",
            "tableName": "jifenshangdian"
        }], "menu": "积分商店"
    },{"child": [{
            "buttons":["删除","查看"],
            "menu": "我的收藏管理",
            "menuJump": "列表",
            "tableName": "wodeshouzangguanli"
        }], "menu": "我的收藏管理"
    },{
                "child": [{"buttons": ["查看"], "menu": "平台通知", "tableName": "news"}],
                "menu": "平台通知"
            },{
                "child": [{"buttons": ["查看"], "menu": "购物论坛管理", "tableName": "forum"}],
                "menu": "购物论坛"
            },{
                "child": [{"buttons": ["查看"], "menu": "在线留言", "tableName": "messagess"}],
                "menu": "在线留言"
            }],"roleName": "用户", "tableName": "yonghu"},{"backMenu":[{"child": [{
            "buttons":["查看", "修改", "删除"],
            "menu": "商品管理评论",
            "menuJump": "列表",
            "tableName": "discussshangpinguanli"
        }], "menu": "商品管理评论"
    },{"child": [{
            "buttons":["新增","删除","修改","查看","出入库","查看评论","回复"],
            "menu": "商品管理",
            "menuJump": "列表",
            "tableName": "shangpinguanli"
        }], "menu": "商品管理"
    },{"child": [{
            "buttons":["查看", "修改", "删除"],
            "menu": "店铺信息评论",
            "menuJump": "列表",
            "tableName": "discussdianpuxinxi"
        }], "menu": "店铺信息评论"
    },{"child": [{
            "buttons":["新增","删除","查看","修改","查看评论","回复"],
            "menu": "店铺信息",
            "menuJump": "列表",
            "tableName": "dianpuxinxi"
        }], "menu": "店铺信息"
    },{"child": [{
            "buttons":["新增","删除","修改","查看"],
            "menu": "问诊",
            "menuJump": "列表",
            "tableName": "wenzhen"
        }], "menu": "问诊"
    }],"frontMenu":[{
                "child": [{"buttons": ["查看"], "menu": "平台通知", "tableName": "news"}],
                "menu": "平台通知"
            },{
                "child": [{"buttons": ["查看"], "menu": "购物论坛管理", "tableName": "forum"}],
                "menu": "购物论坛"
            },{
                "child": [{"buttons": ["查看"], "menu": "在线留言", "tableName": "messagess"}],
                "menu": "在线留言"
            },{
                "child": [{"buttons": ["查看"], "menu": "平台通知", "tableName": "news"}],
                "menu": "平台通知"
            },{
                "child": [{"buttons": ["查看"], "menu": "购物论坛管理", "tableName": "forum"}],
                "menu": "购物论坛"
            },{
                "child": [{"buttons": ["查看"], "menu": "在线留言", "tableName": "messagess"}],
                "menu": "在线留言"
            }],"roleName": "商家", "tableName": "shangjia"},{"backMenu":[{"child": [{
            "buttons":["查看", "修改", "删除"],
            "menu": "商品管理评论",
            "menuJump": "列表",
            "tableName": "discussshangpinguanli"
        }], "menu": "商品管理评论"
    },{"child": [{
            "buttons":["新增","删除","修改","查看","出入库","查看评论","回复","审核"],
            "menu": "商品管理",
            "menuJump": "列表",
            "tableName": "shangpinguanli"
        }], "menu": "商品管理"
    },{"child": [{
            "buttons":["新增","修改","删除","查看"],
            "menu": "商品分类",
            "menuJump": "列表",
            "tableName": "shangpinfenlei"
        }], "menu": "商品分类"
    },{"child": [{
            "buttons":["查看", "修改", "删除"],
            "menu": "店铺信息评论",
            "menuJump": "列表",
            "tableName": "discussdianpuxinxi"
        }], "menu": "店铺信息评论"
    },{"child": [{
            "buttons":["删除","修改","查看","查看评论","回复","审核"],
            "menu": "店铺信息",
            "menuJump": "列表",
            "tableName": "dianpuxinxi"
        }], "menu": "店铺信息"
    },{"child": [{
            "buttons":["新增","删除","修改","查看","出入库"],
            "menu": "积分商店",
            "menuJump": "列表",
            "tableName": "jifenshangdian"
        }], "menu": "积分商店"
    },{"child": [{
            "buttons":["新增","删除","修改","查看"],
            "menu": "用户",
            "menuJump": "列表",
            "tableName": "yonghu"
        }], "menu": "用户"
    },{"child": [{
            "buttons":["删除","新增","修改","查看"],
            "menu": "商家",
            "menuJump": "列表",
            "tableName": "shangjia"
        }], "menu": "商家"
    },{
                "child": [{"buttons": [ "查看", "修改", "删除"], "menu": "购物论坛管理", "tableName": "forum"}],
                "menu": "购物论坛管理"
            },{
                "child": [{"buttons": ["回复", "查看", "修改", "删除"], "menu": "在线留言", "tableName": "messagess"}],
                "menu": "在线留言"
            },{
                "child": [{"buttons": ["查看", "删除"], "menu": "出入库", "tableName": "crk"}],
                "menu": "出入库"
            },{
                "child": [{"buttons": ["查看"], "menu": "未支付订单", "tableName": "orders/未支付"}, {
                    "buttons": ["查看", "发货"],
                    "menu": "已支付订单",
                    "tableName": "orders/已支付"
                }, {"buttons": ["查看"], "menu": "已完成订单", "tableName": "orders/已完成"}, {
                    "buttons": ["查看"],
                    "menu": "已取消订单",
                    "tableName": "orders/已取消"
                }, {"buttons": ["查看"], "menu": "已退款订单", "tableName": "orders/已退款"}, {
                    "buttons": ["查看"],
                    "menu": "已发货订单",
                    "tableName": "orders/已发货"
                }], "menu": "订单管理"
            },{"child":[{
            "buttons": ["新增", "查看", "修改", "删除"],
            "menu": "轮播图管理",
            "tableName": "config"
        },{
                        "buttons": ["新增", "查看", "修改", "删除"],
                        "menu": "平台通知", "tableName": "news"
                    }],
                "menu": "系统管理"
            }],"roleName": "管理员", "tableName": "users"},{"ykMenu":[{
                "child": [{"buttons": ["查看"], "menu": "平台通知", "tableName": "news"}],
                "menu": "平台通知"
            }],"roleName": "游客", "tableName": "游客"}]
    }
}

const geren={
    list(){
        return [{"ykMenu":[],"roleName": "个人中心", "tableName": "个人中心"}]
    }
}
export {
    menu,geren
}
