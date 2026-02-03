/**
 * pinia 状态类型定义
 */
declare interface LayoutConfigState {
    isCollapse: boolean; // 是否展开菜单
    globalTitle: string; // 网站主标题
    isFullscreen: boolean; // 是否全屏状态：true是
    isDrak: boolean; // 是否暗黑主题：true是
}

// 登录数据类型
declare interface LoginData {
    username: string;
    password: string;
    role:string,
    valicode:string
 }
 