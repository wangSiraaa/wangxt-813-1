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
echo "【业务规则3验证】未上传完工照片不能关闭许可（含签收流程）"
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

echo "9. 施工单位提交签收确认..."
echo "   预期：status = SIGN_OFF_SUBMITTED，signOffPerson = 张施工"
RESPONSE_SIGNOFF=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/submit-signoff" \
  -H "Content-Type: application/json" \
  -d '{
    "signOffPerson": "张施工",
    "rejectReason": ""
  }')
echo "$RESPONSE_SIGNOFF" | python3 -m json.tool
STATUS_SIGNOFF=$(echo "$RESPONSE_SIGNOFF" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
SIGN_OFF_PERSON=$(echo "$RESPONSE_SIGNOFF" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['signOffPerson'])")

if [ "$STATUS_SIGNOFF" = "SIGN_OFF_SUBMITTED" ] && [ "$SIGN_OFF_PERSON" = "张施工" ]; then
  echo "   ✅ 验证通过：签收提交成功，状态正确更新"
else
  echo "   ❌ 验证失败：签收提交失败或状态不正确"
fi
echo ""

echo "10. 尝试关闭许可（已签收但未上传照片）..."
echo "    预期：返回错误，提示未上传完工照片不能关闭许可"
RESPONSE4=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/close")
echo "$RESPONSE4" | python3 -m json.tool
SUCCESS4=$(echo "$RESPONSE4" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")

if [ "$SUCCESS4" = "False" ]; then
  echo "   ✅ 验证通过：已签收但未上传照片不能关闭许可"
else
  echo "   ❌ 验证失败：已签收但未上传照片时应该拒绝关闭许可"
fi
echo ""

echo "11. 街道审核员记录到场时间..."
echo "    预期：status = ARRIVAL_RECORDED"
RESPONSE_ARRIVAL=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/record-arrival")
echo "$RESPONSE_ARRIVAL" | python3 -m json.tool
STATUS_ARRIVAL=$(echo "$RESPONSE_ARRIVAL" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")

if [ "$STATUS_ARRIVAL" = "ARRIVAL_RECORDED" ]; then
  echo "   ✅ 验证通过：到场时间记录成功"
else
  echo "   ❌ 验证失败：到场时间记录失败"
fi
echo ""

echo "12. 再次尝试关闭许可（已记录到场但仍未上传照片）..."
echo "    预期：返回错误，提示未上传完工照片不能关闭许可"
RESPONSE5=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/close")
echo "$RESPONSE5" | python3 -m json.tool
SUCCESS5=$(echo "$RESPONSE5" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")

if [ "$SUCCESS5" = "False" ]; then
  echo "   ✅ 验证通过：已记录到场但未上传照片仍不能关闭许可"
else
  echo "   ❌ 验证失败：已记录到场但未上传照片时应该拒绝关闭许可"
fi
echo ""

echo "13. 园林专家要求补充完工照片..."
echo "    预期：status = PHOTO_SUPPLEMENT_REQUESTED"
RESPONSE_SUPPLEMENT=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/request-photo-supplement" \
  -H "Content-Type: application/json" \
  -d '{
    "signOffPerson": "",
    "rejectReason": "完工照片不清晰，请重新上传修剪后整体效果照片"
  }')
echo "$RESPONSE_SUPPLEMENT" | python3 -m json.tool
STATUS_SUPPLEMENT=$(echo "$RESPONSE_SUPPLEMENT" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
REJECT_REASON=$(echo "$RESPONSE_SUPPLEMENT" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['signOffRejectReason'])")

if [ "$STATUS_SUPPLEMENT" = "PHOTO_SUPPLEMENT_REQUESTED" ] && [ -n "$REJECT_REASON" ]; then
  echo "   ✅ 验证通过：专家要求补充照片成功"
else
  echo "   ❌ 验证失败：专家要求补充照片失败"
fi
echo ""

echo "14. 上传完工照片..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/photos" \
  -H "Content-Type: application/json" \
  -d '{
    "photoUrl": "https://example.com/photos/completion_001.jpg",
    "description": "修剪后整体效果",
    "uploader": "张工"
  }' | python3 -m json.tool
echo ""

echo "15. 施工单位重新提交签收（补充照片后）..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/submit-signoff" \
  -H "Content-Type: application/json" \
  -d '{
    "signOffPerson": "张施工",
    "rejectReason": ""
  }' | python3 -m json.tool
echo ""

echo "16. 街道审核员再次记录到场时间..."
curl -s -X POST "$BASE_URL/applications/$APP_ID2/record-arrival" | python3 -m json.tool
echo ""

echo "17. 关闭许可（已上传照片）..."
echo "    预期：关闭成功，status = CLOSED"
RESPONSE6=$(curl -s -X POST "$BASE_URL/applications/$APP_ID2/close")
echo "$RESPONSE6" | python3 -m json.tool
SUCCESS6=$(echo "$RESPONSE6" | python3 -c "import sys, json; print(json.load(sys.stdin)['success'])")
STATUS6=$(echo "$RESPONSE6" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")

if [ "$SUCCESS6" = "True" ] && [ "$STATUS6" = "CLOSED" ]; then
  echo "   ✅ 验证通过：已上传完工照片，可以关闭许可"
else
  echo "   ❌ 验证失败：上传照片后应该可以关闭许可"
fi
echo ""

echo "18. 查询申请详情，验证返回状态、签收人和拒绝原因..."
echo "    预期：status = CLOSED，signOffPerson = 张施工"
RESPONSE_DETAIL=$(curl -s "$BASE_URL/applications/$APP_ID2")
echo "$RESPONSE_DETAIL" | python3 -m json.tool
STATUS_DETAIL=$(echo "$RESPONSE_DETAIL" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['status'])")
SIGN_OFF_PERSON_DETAIL=$(echo "$RESPONSE_DETAIL" | python3 -c "import sys, json; print(json.load(sys.stdin)['data']['signOffPerson'])")

if [ "$STATUS_DETAIL" = "CLOSED" ] && [ "$SIGN_OFF_PERSON_DETAIL" = "张施工" ]; then
  echo "   ✅ 验证通过：查询详情正确返回状态和签收人信息"
else
  echo "   ❌ 验证失败：查询详情未正确返回状态或签收人信息"
fi
echo ""

echo "=========================================="
echo "验证完成！"
echo "=========================================="
