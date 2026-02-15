# Docker Compose 配置模板

> 本文档提供 docker-compose.yml 的通用模板，用于一键启动所有服务，放在项目根目录

---

## 目录

1. [Python + 前端项目模板](#python--前端项目模板)
2. [Java + 前端项目模板](#java--前端项目模板)
3. [纯后端项目模板](#纯后端项目模板)
4. [配置说明](#配置说明)
5. [使用步骤](#使用步骤)

---

## Python + 前端项目模板

### 完整版（后端 + 前端 + 数据库）

```yaml
version: '3.8'

services:
  # 后端服务
  backend:
    build: ./[后端目录名]
    container_name: [符合命名规则随便起即可，尽量zk-backend]
    ports:
      - "[后端端口]:8000"
    volumes:
      - ./[后端目录名]:/app
    environment:
      - DEBUG=1
      - DATABASE_URL=mysql://[数据库用户名]:[数据库密码]@db:3306/[数据库名]
    depends_on:
      - db
    networks:
      - [符合命名规则随便起即可，尽量zk-network]

  # 前端服务（如果有多个前端，如管理员后台和用户前台，复制此段）
  frontend:
    build: ./[前端目录名]
    container_name: [符合命名规则随便起即可，尽量zk-frontend]
    ports:
      - "[前端端口]:80"
    depends_on:
      - backend
    networks:
      - [符合命名规则随便起即可，尽量zk-network]

  # MySQL 数据库
  db:
    image: mysql:8.0
    container_name: [符合命名规则随便起即可，尽量zk-db]
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=[root密码]
      - MYSQL_DATABASE=[数据库名]
      - MYSQL_USER=[数据库用户名]
      - MYSQL_PASSWORD=[数据库密码]
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - [符合命名规则随便起即可，尽量zk-network]

  # Redis 缓存（可选，用于缓存、会话存储、验证码等）
  redis:
    image: redis:7-alpine
    container_name: [符合命名规则随便起即可，尽量zk-redis]
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis-data:/data
    networks:
      - [符合命名规则随便起即可，尽量zk-network]

networks:
  [项目名]-network:
    driver: bridge

volumes:
  mysql-data:
  redis-data:
```

### 简化版（仅后端 + 前端，无数据库）

```yaml
version: '3.8'

services:
  # 后端服务
  backend:
    build: ./[后端目录名]
    container_name: [项目名]-backend
    ports:
      - "[后端端口]:8000"
    volumes:
      - ./[后端目录名]:/app
    environment:
      - DEBUG=1
    networks:
      - [项目名]-network

  # 前端服务
  frontend:
    build: ./[前端目录名]
    container_name: [项目名]-frontend
    ports:
      - "[前端端口]:80"
    depends_on:
      - backend
    networks:
      - [项目名]-network

networks:
  [项目名]-network:
    driver: bridge
```

---

## Java + 前端项目模板

### Spring Boot + Vue/React

```yaml
version: '3.8'

services:
  # Java 后端服务
  backend:
    build: ./[后端目录名]
    container_name: [符合命名规则随便起即可]
    ports:
      - "[后端端口]:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=dev
      - SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/[数据库名]
      - SPRING_DATASOURCE_USERNAME=[数据库用户名]
      - SPRING_DATASOURCE_PASSWORD=[数据库密码]
    depends_on:
      - db
    networks:
      - [项目名]-network

  # 前端服务
  frontend:
    build: ./[前端目录名]
    container_name: [项目名]-frontend
    ports:
      - "[前端端口]:80"
    depends_on:
      - backend
    networks:
      - [项目名]-network

  # MySQL 数据库
  db:
    image: mysql:8.0
    container_name: [项目名]-db
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=[root密码]
      - MYSQL_DATABASE=[数据库名]
      - MYSQL_USER=[数据库用户名]
      - MYSQL_PASSWORD=[数据库密码]
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - [项目名]-network

networks:
  [项目名]-network:
    driver: bridge

volumes:
  mysql-data:
```

---

## 纯后端项目模板

### Python/Django 后端 + MySQL

```yaml
version: '3.8'

services:
  # 后端服务
  backend:
    build: ./[后端目录名]
    container_name: [项目名]-backend
    ports:
      - "[后端端口]:8000"
    volumes:
      - ./[后端目录名]:/app
    environment:
      - DEBUG=1
      - DATABASE_URL=mysql://[数据库用户名]:[数据库密码]@db:3306/[数据库名]
    depends_on:
      - db
    networks:
      - [项目名]-network

  # MySQL 数据库
  db:
    image: mysql:8.0
    container_name: [项目名]-db
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=[root密码]
      - MYSQL_DATABASE=[数据库名]
      - MYSQL_USER=[数据库用户名]
      - MYSQL_PASSWORD=[数据库密码]
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - [项目名]-network

networks:
  [项目名]-network:
    driver: bridge

volumes:
  mysql-data:
```

### Java/Spring Boot 后端 + PostgreSQL

```yaml
version: '3.8'

services:
  # Java 后端服务
  backend:
    build: ./[后端目录名]
    container_name: [项目名]-backend
    ports:
      - "[后端端口]:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=dev
      - SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/[数据库名]
      - SPRING_DATASOURCE_USERNAME=[数据库用户名]
      - SPRING_DATASOURCE_PASSWORD=[数据库密码]
    depends_on:
      - db
    networks:
      - [项目名]-network

  # PostgreSQL 数据库
  db:
    image: postgres:15
    container_name: [项目名]-db
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_DB=[数据库名]
      - POSTGRES_USER=[数据库用户名]
      - POSTGRES_PASSWORD=[数据库密码]
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - [项目名]-network

networks:
  [项目名]-network:
    driver: bridge

volumes:
  postgres-data:
```

---

## 配置说明

### 需要替换的参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `[项目名]` | 项目名称（用于容器命名） | `my-shop`, `blog-system` |
| `[后端目录名]` | 后端代码目录 | `backend`, `server`, `api` |
| `[前端目录名]` | 前端代码目录 | `frontend`, `web`, `client` |
| `[后端端口]` | 后端服务端口 | `8000`, `8080`, `3000` |
| `[前端端口]` | 前端服务端口 | `8080`, `3000`, `80` |
| `[数据库名]` | 数据库名称 | `mydb`, `shop_db` |
| `[数据库用户名]` | 数据库用户名 | `root`, `admin` |
| `[数据库密码]` | 数据库密码 | `password123` |
| `[root密码]` | MySQL root 密码 | `rootpass123` |

### 常用数据库镜像

| 数据库 | 镜像 | 默认端口 |
|--------|------|----------|
| MySQL | `mysql:8.0` | 3306 |
| PostgreSQL | `postgres:15` | 5432 |
| MongoDB | `mongo:6.0` | 27017 |
| Redis | `redis:7.0` | 6379 |

---

## 使用步骤

### 1. 复制模板

根据你的项目类型，复制对应的模板到项目根目录，命名为 `docker-compose.yml`

### 2. 替换参数

将模板中所有 `[参数]` 替换为实际值。

### 3. 确保 Dockerfile 存在

每个服务目录下需要有 `Dockerfile`：

```
your-project/
├── docker-compose.yml
├── backend/
│   └── Dockerfile
└── frontend/
    └── Dockerfile
```

### 4. 启动服务

```bash
# 进入项目根目录
cd your-project

# 启动所有服务
docker-compose up -d

# 查看运行状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 5. 访问服务

根据配置的端口访问：
- 后端：`http://localhost:[后端端口]`
- 前端：`http://localhost:[前端端口]`

---

## 常用命令

```bash
# 启动所有服务（后台运行）
docker-compose up -d

# 启动所有服务（前台运行，可看日志）
docker-compose up

# 停止所有服务
docker-compose down

# 停止并删除所有数据
docker-compose down -v

# 重启服务
docker-compose restart

# 查看运行状态
docker-compose ps

# 查看日志
docker-compose logs

# 查看特定服务日志
docker-compose logs backend

# 进入容器
docker-compose exec backend bash

# 重新构建镜像
docker-compose build

# 重新构建并启动
docker-compose up -d --build
```

---

## 实际示例

### 示例 1: Django + Vue3 电商项目

```yaml
version: '3.8'

services:
  backend:
    build: ./pyzkds
    container_name: shop-backend
    ports:
      - "8000:8000"
    volumes:
      - ./pyzkds:/app
    environment:
      - DEBUG=1
    networks:
      - shop-network

  admin:
    build: ./admin/admin
    container_name: shop-admin
    ports:
      - "8080:80"
    depends_on:
      - backend
    networks:
      - shop-network

  front:
    build: ./front/front
    container_name: shop-front
    ports:
      - "8081:80"
    depends_on:
      - backend
    networks:
      - shop-network

networks:
  shop-network:
    driver: bridge
```

### 示例 2: Spring Boot + React 博客系统

```yaml
version: '3.8'

services:
  backend:
    build: ./blog-backend
    container_name: blog-backend
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=dev
      - SPRING_DATASOURCE_URL=jdbc:mysql://db:3306/blog_db
      - SPRING_DATASOURCE_USERNAME=blog_user
      - SPRING_DATASOURCE_PASSWORD=blog_pass123
    depends_on:
      - db
    networks:
      - blog-network

  frontend:
    build: ./blog-frontend
    container_name: blog-frontend
    ports:
      - "3000:80"
    depends_on:
      - backend
    networks:
      - blog-network

  db:
    image: mysql:8.0
    container_name: blog-db
    ports:
      - "3306:3306"
    environment:
      - MYSQL_ROOT_PASSWORD=root123
      - MYSQL_DATABASE=blog_db
      - MYSQL_USER=blog_user
      - MYSQL_PASSWORD=blog_pass123
    volumes:
      - mysql-data:/var/lib/mysql
    networks:
      - blog-network

networks:
  blog-network:
    driver: bridge

volumes:
  mysql-data:
```

---

## 常见问题

### Q1: 端口被占用怎么办？

修改 `ports` 配置：

```yaml
ports:
  - "8001:8000"  # 将本地端口改为 8001
```

### Q2: 如何添加 Redis 缓存？

添加 Redis 服务：

```yaml
services:
  redis:
    image: redis:7.0
    container_name: [项目名]-redis
    ports:
      - "6379:6379"
    networks:
      - [项目名]-network
```

### Q3: 如何持久化数据？

使用 volumes：

```yaml
volumes:
  - ./data:/app/data  # 映射到本地目录
```

### Q4: 如何查看容器内部？

```bash
# 进入容器
docker-compose exec backend bash

# 查看文件
ls -la

# 退出
exit
```

---

## 优势

使用 docker-compose 的好处：

✅ **一键启动**：不需要分别启动多个服务
✅ **环境隔离**：不污染本地环境
✅ **团队协作**：团队成员环境一致
✅ **快速部署**：可以快速在任何机器上运行
✅ **易于调试**：可以方便地查看日志和进入容器

---

**创建时间**: 2026-02-04
**适用版本**: Docker Compose v3.8+
