import * as axios from 'axios'

declare module 'axios'{
    //自行扩展axios返回的数据类型
    export interface AxiosResponse<T=any>{
        code:number;
        message:string;
        data:T;
    }
}

