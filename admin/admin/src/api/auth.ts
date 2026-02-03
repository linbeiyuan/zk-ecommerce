import request from "@/utils/request";
import { Session } from '@/utils/storage';
import { Key } from '@/stores/auth';
export function GetToken(data:any,url:string){
    return request({
        url:`${url}`,
        method:'POST',
        data
    })
}

export function GetUsersToken(){
       const tableName=Session.get("tableName");
     return request({
        url:`${tableName}/session`,
        method:'POST'
     })
}