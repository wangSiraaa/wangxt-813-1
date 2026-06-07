# 市政行道树修剪许可管理系统

## 项目概述

本系统是一套市政行道树修剪许可审批管理平台，实现树木修剪申请的提交、审批、施工、验收全流程管理。系统支持普通树木和古树名木的差异化审批流程，占道施工冲突检测，完工照片上传验证，以及签收确认流程。

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
- 即使完成签收流程，未上传完工照片仍不能关闭许可

### 4. 签收确认规则
- 施工单位完成作业后提交签收确认（SIGN_OFF_SUBMITTED）
- 街道审核员现场核查并记录到场时间（ARRIVAL_RECORDED）
- 园林专家可要求补充完工照片（PHOTO_SUPPLEMENT_REQUESTED）
- 补充照片后需重新提交签收并记录到场时间
- 所有签收流程状态下，未上传完工照片均不能关闭许可

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

## API 接口列表

### 树木档案管理
| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /trees | 查询所有树木档案 |
| GET | /trees/{id} | 查询单棵树木详情 |

### 修剪申请管理
| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /applications | 提交修剪申请 |
| GET | /applications | 查询申请列表 |
| GET | /applications/{id} | 查询申请详情 |
| POST | /applications/{id}/street-audit | 街道审核 |
| POST | /applications/{id}/expert-audit | 专家审批 |
| POST | /applications/{id}/start-construction | 开始施工 |
| POST | /applications/{id}/complete-construction | 完成施工 |
| POST | /applications/{id}/submit-signoff | 提交签收确认 |
| POST | /applications/{id}/record-arrival | 记录到场时间 |
| POST | /applications/{id}/request-photo-supplement | 要求补充照片 |
| POST | /applications/{id}/photos | 上传完工照片 |
| POST | /applications/{id}/close | 关闭许可 |

## API 请求示例

### 1. 提交修剪申请
```bash
curl -X POST http://localhost:8080/api/pruning/applications \
  -H "Content-Type: application/json" \
  -d '{
    "treeCode": "TR001",
    "applicant": "李工",
    "maintenanceUnit": "城维养护公司",
    "pruningReason": "树冠过密影响采光",
    "pruningScheme": "疏剪过密枝条",
    "plannedStartDate": "2026-06-12",
    "plannedEndDate": "2026-06-14",
    "occupyRoad": true,
    "roadSection": "中山路-东段"
  }'
```

### 2. 街道审核
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/street-audit \
  -H "Content-Type: application/json" \
  -d '{
    "auditor": "王审核",
    "approved": true,
    "opinion": "情况属实，同意修剪"
  }'
```

### 3. 提交签收确认（施工单位）
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/submit-signoff \
  -H "Content-Type: application/json" \
  -d '{
    "signOffPerson": "张施工",
    "rejectReason": ""
  }'
```

**响应示例：**
```json
{
  "success": true,
  "message": "签收提交成功",
  "data": {
    "id": 1,
    "applicationNo": "PR2026060001",
    "status": "SIGN_OFF_SUBMITTED",
    "signOffPerson": "张施工",
    "signOffTime": "2026-06-15T10:30:00",
    "arrivalTime": null,
    "signOffRejectReason": null
  }
}
```

### 4. 记录到场时间（街道审核员）
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/record-arrival
```

**响应示例：**
```json
{
  "success": true,
  "message": "到场时间记录成功",
  "data": {
    "id": 1,
    "status": "ARRIVAL_RECORDED",
    "signOffPerson": "张施工",
    "arrivalTime": "2026-06-15T11:00:00",
    "signOffRejectReason": null
  }
}
```

### 5. 要求补充完工照片（园林专家）
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/request-photo-supplement \
  -H "Content-Type: application/json" \
  -d '{
    "signOffPerson": "",
    "rejectReason": "完工照片不清晰，请重新上传修剪后整体效果照片"
  }'
```

**响应示例：**
```json
{
  "success": true,
  "message": "已要求补充照片",
  "data": {
    "id": 1,
    "status": "PHOTO_SUPPLEMENT_REQUESTED",
    "signOffPerson": "张施工",
    "signOffRejectReason": "完工照片不清晰，请重新上传修剪后整体效果照片"
  }
}
```

### 6. 上传完工照片
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/photos \
  -H "Content-Type: application/json" \
  -d '{
    "photoUrl": "https://example.com/photos/completion_001.jpg",
    "description": "修剪后整体效果",
    "uploader": "张工"
  }'
```

### 7. 查询申请详情（含状态、签收人、拒绝原因）
```bash
curl http://localhost:8080/api/pruning/applications/1
```

**响应示例：**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "applicationNo": "PR2026060001",
    "status": "ARRIVAL_RECORDED",
    "applicant": "李工",
    "treeCode": "TR001",
    "signOffPerson": "张施工",
    "signOffTime": "2026-06-15T10:30:00",
    "arrivalTime": "2026-06-15T11:00:00",
    "signOffRejectReason": null,
    "hasCompletionPhoto": true
  }
}
```

### 8. 关闭许可（需已上传完工照片）
```bash
curl -X POST http://localhost:8080/api/pruning/applications/1/close
```

**未上传照片时的错误响应：**
```json
{
  "success": false,
  "message": "未上传完工照片，不能关闭许可"
}
```

## 验收路径说明

### 验收场景：提交古树修剪申请并验证进入专家审批

1. 查询树木档案，获取古树编号（如 TR003）
2. 提交该古树的修剪申请
3. 验证申请状态自动变为 EXPERT_APPROVAL（专家审批）
4. 查询待专家审批的申请列表，验证包含该申请

### 验收场景：签收确认流程验证

1. 提交普通树木修剪申请并通过街道审核
2. 开始施工、完成施工
3. 施工单位提交签收确认，状态变为 SIGN_OFF_SUBMITTED
4. **验证关键：此时尝试关闭许可，因未上传完工照片应被拒绝**
5. 街道审核员记录到场时间，状态变为 ARRIVAL_RECORDED
6. **验证关键：此时再次尝试关闭许可，仍因未上传照片被拒绝**
7. 园林专家要求补充照片，状态变为 PHOTO_SUPPLEMENT_REQUESTED
8. 上传完工照片
9. 重新提交签收并记录到场时间
10. 关闭许可成功，状态变为 CLOSED
11. 查询申请详情，验证返回状态、签收人和拒绝原因

## 验证脚本

项目提供了自动化验证脚本 `verify.sh`，可一次性验证所有核心业务规则：

```bash
chmod +x verify.sh
./verify.sh
```

脚本将依次验证：
- 古树自动进入专家审批
- 普通树木进入街道审核
- 占道施工时间冲突拒绝
- 未上传完工照片不能关闭许可（含签收流程各阶段验证）
- 签收确认全流程
- 查询详情返回状态、签收人和拒绝原因

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
