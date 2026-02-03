import { defineStore } from 'pinia';
import {GetUsersToken} from '@/api/auth'
export const useSocketStore = defineStore('socket', {
    state: () => ({
        socket: null
    }),
    actions: {
        async initializeSocket(userId, nicheng, role) {
            // 假设你有一个函数来初始化 socket
            this.socket = connectSocket(userId, nicheng, role);
        },
    },
});

function connectSocket(userId, nicheng, role) {
    useSocketStore.socket = new WebSocket("ws://localhost:8080/pyzkds/consultation?role=" + role + "&userid=" + userId + "&nicheng=" + nicheng);
    useSocketStore.socket.onopen = () => {
        console.log('WebSocket连接已打开');
        useSocketStore.socket.send(JSON.stringify({ type: 'JOIN', userId:  userId, role: role, nicheng: nicheng}));
    };

    useSocketStore.socket.onmessage = (event) => {
    };

    useSocketStore.socket.onclose = () => {
        console.log('WebSocket连接已关闭');
    };

    useSocketStore.socket.onerror = (error) => {
        console.error('WebSocket错误:', error);
    };
    return useSocketStore.socket;
}
