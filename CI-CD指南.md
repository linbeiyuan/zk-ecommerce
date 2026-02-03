# 基于 CI/CD 的电商管理平台 - 部署指南

> 本项目实现了完整的 CI/CD 自动化流程，包括代码检查、自动构建和部署。

## 目录

1. [项目概述](#项目概述)
2. [CI/CD 架构说明](#cicd-架构说明)
3. [环境准备](#环境准备)
4. [本地开发](#本地开发)
5. [Docker 部署](#docker-部署)
6. [GitHub Actions 配置](#github-actions-配置)
7. [常见问题](#常见问题)

---

## 项目概述

本项目是一个基于 CI/CD 的电商管理平台，采用前后端分离架构：

| 模块 | 技术栈 | 端口 |
|------|--------|------|
| 后端 API | Django + DRF | 8000 |
| 管理后台 | Vue3 + TypeScript | 8080 |
| 用户前台 | Vue3 + TypeScript | 8081 |

---

## CI/CD 架构说明

### 什么是 CI/CD？

- **CI (持续集成)**: 代码提交后自动运行测试和构建
- **CD (持续部署)**: 测试通过后自动部署到服务器

### 本项目 CI/CD 流程

```
代码提交 → GitHub → 触发 CI → 代码检查 → 构建测试 → 构建镜像 → 推送镜像 → 部署
```

### 工作流文件说明

| 文件 | 作用 | 触发条件 |
|------|------|----------|
| `.github/workflows/ci.yml` | 持续集成 | push/PR 到 main/develop |
| `.github/workflows/cd.yml` | 持续部署 | push 到 main 或创建 tag |

---

## 环境准备

### 必需软件

1. **Git** - 版本控制
2. **Docker Desktop** - 容器化部署
3. **Node.js 18+** - 前端开发
4. **Python 3.9+** - 后端开发

### 安装 Docker (Windows)

1. 下载 Docker Desktop: https://www.docker.com/products/docker-desktop
2. 安装并重启电脑
3. 验证安装: `docker --version`

---

## 本地开发

### 后端启动

```bash
cd pyzkds
pip install -r requirements.txt
python manage.py runserver
```

### 前端 Admin 启动

```bash
cd admin/admin
npm install
npm run dev
```

### 前端 Front 启动

```bash
cd front/front
npm install
npm run dev
```

---

## Docker 部署

### 一键启动所有服务

```bash
# 在项目根目录执行
docker-compose up -d
```

### 查看运行状态

```bash
docker-compose ps
```

### 停止服务

```bash
docker-compose down
```

### 访问地址

| 服务 | 地址 |
|------|------|
| 后端 API | http://localhost:8000 |
| 管理后台 | http://localhost:8080 |
| 用户前台 | http://localhost:8081 |

---

## GitHub Actions 配置

### 步骤 1: 创建 GitHub 仓库

1. 登录 GitHub
2. 点击 "New repository"
3. 输入仓库名称，如 `zk-ecommerce`
4. 选择 Public（公开）
5. 点击 "Create repository"

### 步骤 2: 推送代码到 GitHub

```bash
git add .
git commit -m "初始化项目"
git branch -M main
git remote add origin https://github.com/你的用户名/zk-ecommerce.git
git push -u origin main
```

### 步骤 3: 配置 Secrets（可选，用于 CD）

1. 进入仓库 Settings → Secrets and variables → Actions
2. 添加以下 Secrets:
   - `DOCKER_USERNAME`: Docker Hub 用户名
   - `DOCKER_PASSWORD`: Docker Hub 密码

### 步骤 4: 查看 CI/CD 运行结果

1. 进入仓库的 "Actions" 标签页
2. 可以看到每次提交触发的工作流
3. 点击查看详细日志

---

## 常见问题

### Q1: Docker 构建失败？

检查 Dockerfile 路径和依赖文件是否正确。

### Q2: GitHub Actions 运行失败？

查看 Actions 日志，通常是依赖安装或构建命令问题。

### Q3: 端口被占用？

修改 docker-compose.yml 中的端口映射。

---

## 项目结构

```
zk电商平台/
├── .github/
│   └── workflows/
│       ├── ci.yml          # CI 持续集成配置
│       └── cd.yml          # CD 持续部署配置
├── pyzkds/                  # Django 后端
│   ├── Dockerfile
│   └── ...
├── admin/admin/             # Vue3 管理后台
│   ├── Dockerfile
│   ├── nginx.conf
│   └── ...
├── front/front/             # Vue3 用户前台
│   ├── Dockerfile
│   ├── nginx.conf
│   └── ...
├── docker-compose.yml       # Docker 编排文件
├── .gitignore
└── CI-CD指南.md
```



~~~
传统方式的问题：

每次修改代码后，需要手动测试
手动构建项目
手动部署到服务器
容易出错，效率低
使用 CI/CD 后：

代码提交到 GitHub 后，自动运行测试
自动构建前后端项目
自动检查代码质量
测试通过后，自动部署到服务器
节省时间，减少人为错误

"这正好展示了 CI/CD 的核心价值！如果没有 CI/CD，这些错误会在部署到生产环境后才被发现，造成系统崩溃。但现在，GitHub Actions 在代码提交后立即自动检测到了问题，并给出了详细的错误位置和原因，让我们可以在开发阶段就修复这些问题，避免了生产事故。"
~~~

![image-20260203234016117](C:\Users\李圣杰\AppData\Roaming\Typora\typora-user-images\image-20260203234016117.png)

~~~
git push 的作用
✅ 是的，每次执行 git push，会把本地的新提交推送到 GitHub 仓库

不是推送整个项目，而是推送增量更新（只推送新的改动）
第一次推送是完整项目，之后只推送修改的部分
2. CI 自动触发
✅ 是的，每次 git push 到 main 分支，会自动触发 CI 持续集成

GitHub Actions 检测到新提交
自动运行 .github/workflows/ci.yml 中定义的测试
自动构建前后端项目
检查代码是否有错误

下载 ZIP
点击 "下载ZIP" 按钮
下载压缩包，解压后使用

"每次我修改代码并 push 到 GitHub，GitHub Actions 会自动检测到新提交，然后自动运行我配置的 CI 工作流。它会自动测试后端代码、构建前后端项目，如果有错误会立即反馈给我。这样可以在开发阶段就发现问题，避免部署到生产环境后才发现错误。"
~~~

