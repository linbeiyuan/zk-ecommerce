import { defineStore } from 'pinia';
import { GetToken } from '@/api/auth';
import { Session, Local } from '@/utils/storage';

export const Key = {
    accessTokenKey: 'accessToken',
    userInfoKey: 'userInfo',
     isLoingKey: '0'
}

export const useAuthStore = defineStore('auth', {
    state: () => {
        return {
            accessToken: Session.get(Key.accessTokenKey),
            users:Session.get(Key.userInfoKey),
            isLogin:Session.get(Key.isLoingKey)
        }
    },

    actions: {
      
        // 登录操作
        userLogin (loginData:any,url:string) {
            return new Promise((resolve, reject) => {
                GetToken(loginData,url).then((res: any) => {
                    // console.log("返回token"+res.token);
                    // const {data} = res.token;
                    
                    // 访问令牌
                    // const { access_token } = data;
                    // this.accessToken = access_token;
                    // console.log("保存token:"+res.token);
                    this.accessToken = res.token;
                    // // 保存到session
                     Session.set(Key.accessTokenKey, res.token);
                     Session.set(Key.isLoingKey,'1')
                    // 正常响应钩子
                    resolve(res);
                }).catch((error: Error) => {
                    reject(error);
                });
            });
        },


    }
});
