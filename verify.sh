#!/bin/bash

BASE_URL="http://localhost:8080/api/pruning"

echo "=========================================="
echo "市政行道树修剪许可 API 验证脚本"
echo "=========================================="
echo ""

echo "请确保服务已启动（mvn spring-boot:run）"
echo ""
read -p "按 Enter 键开始验证..."

echo ""
echo "=========================================="
echo "【验收路径】提交古树修剪申请并验证进入专家审批"
echo "=========================================="
echo ""

echo "1. 查询树木档案..."
curl -s "$BASE_URL/trees" | python3 -m json.tool
echo ""

echo "2. 提交古树名木（TR003 - 国槐，120年树龄）的修剪申请..."
echo "   预期：status = EXPERT_APPROVAL"
RESPONSE=$(curl -s -X POST "$BASE_URL/applications" \
  -H "Content-Type: application/json" \
  -d '{
    "treeCode": "TR003",
    "applicant": "张工",
    "maintenanceUnit": "古树名木保护中心",
    "pruningReason": "枯枝存在安全隐患，需要修剪",
    "pruningScheme": "保留主枝，剪除枯死枝条",
    "plannedStartDate": "2026-06-10",
    "plannedEndDate": "2026-06-15",
    "occupyRoad": false
  }')

echo "$RESPONSE" | python3 -m json.tool

STATUS=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
APP_ID=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['id'])")
APP_NO=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['applicationNo'])")

echo ""
echo "   申请ID: $APP_ID"
echo "   申请编号: $APP_NO"
echo "   当前状态: $STATUS"

if [ "$STATUS" = "EXPERT_APPROVAL" ]; then
  echo "   ✅ 验证通过：古树名木自动进入专家审批状态"
else
  echo "   ❌ 验证失败：预期状态为 EXPERT_APPROVAL，实际为 $STATUS"
fi
echo ""

echo "3. 查询待专家审批的申请列表..."
echo "   预期：包含刚才提交的申请"
curl -s "$BASE_URL/applications/expert/pending" | python3 -m json.tool
echo ""

echo "=========================================="
echo "【业务规则1验证】普通树木进入街道审核"
echo "=========================================="
echo ""

echo "4. 提交普通树木（TR001 - 悬铃木）的修剪申请..."
echo "   预期：status = STREET_REVIEW"
RESPONSE2=$(curl -s -X POST "$BASE_URL/applications" \
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
  }')

echo "$RESPONSE2" | python3 -m json.tool
STATUS2=$(echo "$RESPONSE2" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
APP_ID2=$(echo "$RESPONSE2" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['id'])")

if [ "$STATUS2" = "STREET_REVIEW" ]; then
  echo "   ✅ 验证通过：普通树木进入街道审核状态"
else
  echo "   ❌ 验证失败：预期状态为 STREET_REVIEW，实际为 $STATUS2"
fi
echo ""

echo "=========================================="
echo "【业务规则2验证】占道施工时间冲突拒绝"
echo "=========================================="
echo ""

echo "5. 尝试提交另一个占道申请，时间与上一个重叠..."
echo "   预期：返回错误，提示占道施工时间冲突"
RESPONSE3=$(curl -s -X POST "$BASE_URL/applications" \
  -H "Content-Type: application/json" \
  -d '{
    "treeCode": "TR002",
    "applicant": "赵工",
    "maintenanceUnit": "城维养护公司",
    "pruningReason": "树枝遮挡交通标志",
    "pruningScheme": "修剪遮挡枝条",
    "plannedStartDate": "2026-06-13",
    "plannedEndDate": "2026-06-16",
    "occupyRoad": true,
    "roadSection": "中山路-东段"
  }')

echo "$RESPONSE3" | python3 -m json.tool
SUCCESS3=$(echo "$RESPONSE3" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")

if [ "$SUCCESS3" = "False" ]; then
  echo "   ✅ 验证通过：占道施工时间冲突被正确拒绝"
else
  echo "   ❌ 验证失败：应该拒绝时间冲突的申请"
fi
echo ""

echo "=========================================="
echo "【业务规则3验证】未上传完工照片不能关闭许可"
echo "=========================================="
echo ""

echo "6. 街道审核通过申请 #$APP_ID2..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/street-audit" \
  -H "Content-Type: application/json" \
  -d '{
    "auditor": "王审核",
    "approved": true,
    "opinion": "情况属实，同意修剪"
  }' | python3 -m json.tool
echo ""

echo "7. 开始施工..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/start-construction" | python3 -m json.tool
echo ""

echo "8. 完成施工..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/complete-construction" | python3 -m json.tool
echo ""

echo "9. 尝试关闭许可（未上传照片）..."
echo "   预期：返回错误，提示未上传完工照片不能关闭许可"
RESPONSE4=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/close")
echo "$RESPONSE4" | python3 -m json.tool
SUCCESS4=$(echo "$RESPONSE4" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")

if [ "$SUCCESS4" = "False" ]; then
  echo "   ✅ 验证通过：未上传完工照片不能关闭许可"
else
  echo "   ❌ 验证失败：未上传照片时应该拒绝关闭许可"
fi
echo ""

echo "10. 上传完工照片..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/photos" \
  -H "Content-Type: application/json" \
  -d '{
    "photoUrl": "https://example.com/photos/completion_001.jpg",
    "description": "修剪后整体效果",
    "uploader": "张工"
  }' | python3 -m json.tool
echo ""

echo "11. 再次关闭许可（已上传照片）..."
echo "    预期：关闭成功，status = CLOSED"
RESPONSE5=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/close")
echo "$RESPONSE5" | python3 -m json.tool
SUCCESS5=$(echo "$RESPONSE5" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")
STATUS5=$(echo "$RESPONSE5" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")

if [ "$SUCCESS5" = "True" ] && [ "$STATUS5" = "CLOSED" ]; then
  echo "   ✅ 验证通过：已上传完工照片，可以关闭许可"
else
  echo "   ❌ 验证失败：上传照片后应该可以关闭许可"
fi
echo ""

echo "=========================================="
echo "验证完成！"
echo "=========================================="
