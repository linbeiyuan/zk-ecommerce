import { Session } from '@/utils/storage';
import {menu,geren} from './menu';
/**
 * 是否有权限
 * @param {*} key
 */
export function isAuth(tableName:any,key:any) {
    let role = Session.get("role");
    if(!role){
        role = '管理员';
    }
    let menus = menu.list();
    for(let i=0;i<menus.length;i++){
        if(menus[i].roleName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    // for(let i=0;i<menus.length;i++){
    //     if(menus[i].roleName==role){
    //         for(let j=0;j<menus[i].backMenu.length;j++){
    //             if(menus[i].backMenu[j].tableName==tableName){
    //                 let buttons = menus[i].backMenu[j].child[0].buttons.join(',');
    //                 return buttons.indexOf(key) !== -1 || false
    //             }
    //         }
    //     }
    // }
    return false;
}

export function isgrAuth(tableName:any,key:any) {
    
    let role = Session.get("role");
    if(!role){
        role = '管理员';
    }
    let menus = geren.list();
    for(let i=0;i<menus.length;i++){
        // if(menus[i].roleName==role){
            // console.log(tableName)
            for(let j=0;j<menus[i].ykMenu.length;j++){
                for(let k=0;k<menus[i].ykMenu[j].child.length;k++){
                    if(tableName==menus[i].ykMenu[j].child[k].tableName){
                        
                        let buttons = menus[i].ykMenu[j].child[k].buttons.join(',');
                        console.log(buttons);
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        // }
    }
    return false;
}

