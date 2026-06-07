# 市政行道树修剪许可管理系统

## 项目概述

本系统是一套市政行道树修剪许可审批管理平台，实现树木修剪申请的提交、审批、施工、验收全流程管理。系统支持普通树木和古树名木的差异化审批流程，占道施工冲突检测，以及完工照片上传验证等核心业务功能。

## 核心业务规则

### 1. 古树专家审批规则
- 古树名木（category = ANCIENT_AND_FAMOUS）的修剪申请，提交后自动进入**专家审批（EXPERT_APPROVAL）**状态
- 普通树木（category = ORDINARY）的修剪申请，提交后进入**部门审批（DEPT_APPROVAL）**状态

### 2. 占道冲突拒绝规则
- 申请占道施工时，系统自动校验指定路段是否已被占用
- 若路段已被占用（is_occupied = TRUE），申请将被拒绝并提示冲突

### 3. 完工照片验证规则
- 修剪作业完成后，必须上传完工照片
- 未上传完工照片的申请，无法执行关闭操作

## 技术栈

- **后端框架**: Spring Boot 2.x
- **数据库**: H2（内存数据库，开发环境）
- **ORM**: Spring Data JPA + Hibernate
- **构建工具**: Maven
- **接口测试**: REST Client / HTTP Client

## 快速开始

### 启动方式

1. 确保已安装 JDK 8+ 和 Maven
2. 进入项目根目录执行：
```bash
mvn spring-boot:run
```
3. 服务启动后访问：
   - API 基础路径: `http://localhost:8080/api/pruning`
   - H2 控制台: `http://localhost:8080/h2-console`

### H2 控制台配置
- JDBC URL: `jdbc:h2:mem:treepermit`
- 用户名: `sa`
- 密码: （空）

## 验收路径说明

### 验收场景：提交古树修剪申请并验证进入专家审批

**操作步骤：**

1. 启动应用服务
2. 提交古树（TR003）修剪申请：
   - 调用 `POST /api/pruning/applications`
   - 请求体包含 `treeCode: "TR003"`（该树为古树名木）
3. **预期结果**：
   - 返回状态码 200
   - 响应数据中 `status` 字段值为 `EXPERT_APPROVAL`
4. 查询待专家审批列表：
   - 调用 `GET /api/pruning/applications/expert/pending`
   - 验证刚才提交的申请出现在列表中

## API 接口列表

| 接口路径 | 方法 | 说明 |
|---------|------|------|
| `/api/pruning/trees` | GET | 查询所有树木档案 |
| `/api/pruning/trees/{code}` | GET | 根据编码查询单株树木 |
| `/api/pruning/applications` | POST | 提交修剪申请 |
| `/api/pruning/applications` | GET | 查询所有申请 |
| `/api/pruning/applications/{id}` | GET | 根据ID查询申请详情 |
| `/api/pruning/applications/expert/pending` | GET | 查询待专家审批列表 |
| `/api/pruning/applications/{id}/expert/audit` | POST | 专家审批 |
| `/api/pruning/applications/{id}/dept/audit` | POST | 部门审批 |
| `/api/pruning/applications/{id}/construct` | POST | 开始施工 |
| `/api/pruning/applications/{id}/photo` | POST | 上传完工照片 |
| `/api/pruning/applications/{id}/close` | POST | 关闭申请 |

## 初始化数据说明

系统启动时自动初始化以下测试数据：

### 树木档案（tree_archive）

| 编码 | 树种 | 位置 | 类别 | 树龄 | 养护单位 |
|------|------|------|------|------|----------|
| TR001 | 悬铃木 | 中山路1号 | 普通树木 | 15年 | 市政养护 |
| TR002 | 香樟 | 中山路2号 | 普通树木 | 12年 | 市政养护 |
| TR003 | 国槐 | 人民路1号 | 古树名木 | 120年 | 古树中心 |
| TR004 | 银杏 | 人民路2号 | 古树名木 | 300年 | 古树中心 |
| TR005 | 杨树 | 建设路1号 | 普通树木 | 8年 | 绿源公司 |

### 施工路段（construction_section）

| 路段名称 | 位置 | 占用状态 |
|----------|------|----------|
| Zhongshan-E | 中山路东段 | 未占用 |
| Renmin-N | 人民路北段 | 未占用 |
| Jianshe-M | 建设路中段 | 未占用 |
