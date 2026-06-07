#!/usr/bin/env python3
# 最终修复脚本

# 1. 修复 PruningApplicationService.java - 添加完工照片检查
service_file = "src/main/java/com/municipal/tree/service/PruningApplicationService.java"

with open(service_file, 'r') as f:
    content = f.read()

# 查找并替换 closeApplication 方法
old_part = """        if (application.getStatus() != ApplicationStatus.COMPLETED) {
            throw new BusinessException(400, "当前状态不允许关闭许可");
        }

        businessRuleValidator.validateClosePermission(application);"""

new_part = """        if (application.getStatus() != ApplicationStatus.COMPLETED) {
            throw new BusinessException(400, "当前状态不允许关闭许可");
        }

        var photos = completionPhotoRepository.findByApplicationId(applicationId);
        if (photos == null || photos.isEmpty()) {
            throw new BusinessException(400, "未上传完工照片，不能关闭许可");
        }

        businessRuleValidator.validateClosePermission(application);"""

content = content.replace(old_part, new_part)

with open(service_file, 'w') as f:
    f.write(content)

print("✓ 完工照片检查已添加到 PruningApplicationService.java")

# 2. 检查占道冲突检测 - 修复 Repository 的查询
repo_file = "src/main/java/com/municipal/tree/repository/PruningApplicationRepository.java"

with open(repo_file, 'r') as f:
    repo_content = f.read()

# 修复 JPQL 查询，使用正确的枚举引用
old_query = """    @Query("SELECT p FROM PruningApplication p WHERE p.roadSection = :roadSection " +
           "AND p.status IN ('STREET_REVIEW', 'EXPERT_APPROVAL', 'APPROVED', 'IN_CONSTRUCTION') " +
           "AND p.id != :excludeId " +
           "AND ((p.plannedStartDate <= :endDate AND p.plannedEndDate >= :startDate))")"""

new_query = """    @Query("SELECT p FROM PruningApplication p WHERE p.roadSection = :roadSection " +
           "AND p.status IN (com.municipal.tree.enums.ApplicationStatus.STREET_REVIEW, " +
           "com.municipal.tree.enums.ApplicationStatus.EXPERT_APPROVAL, " +
           "com.municipal.tree.enums.ApplicationStatus.APPROVED, " +
           "com.municipal.tree.enums.ApplicationStatus.IN_CONSTRUCTION) " +
           "AND (p.id IS NULL OR p.id != :excludeId) " +
           "AND ((p.plannedStartDate <= :endDate AND p.plannedEndDate >= :startDate))")"""

repo_content = repo_content.replace(old_query, new_query)

with open(repo_file, 'w') as f:
    f.write(repo_content)

print("✓ 占道冲突查询已修复")
print("\n所有修复完成！现在请重新编译运行。")
