# 前端 Admin Dockerfile
FROM node:18-alpine as build

WORKDIR /app

# 复制 package.json
COPY package*.json ./

# 安装依赖
RUN npm install --registry=https://registry.npmmirror.com

# 复制源码
COPY . .

# 构建
RUN npm run build

# 生产环境
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
