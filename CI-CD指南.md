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