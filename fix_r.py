import os
base = "src/main/java/com/municipal/tree/repository"

with open(os.path.join(base, "AuditRecordRepository.java"), "w") as f:
    f.write("package com.municipal.tree.repository;\n\nimport com.municipal.tree.entity.AuditRecord;\nimport org.springframework.data.jpa.repository.JpaRepository;\nimport org.springframework.stereotype.Repository;\n\nimport java.util.List;\n\n@Repository\npublic interface AuditRecordRepository extends JpaRepository<AuditRecord, Long> {\n    List<AuditRecord> findByApplicationIdOrderByAuditTimeDesc(Long applicationId);\n}\n")
print("1")

with open(os.path.join(base, "ConstructionSectionRepository.java"), "w") as f:
    f.write("package com.municipal.tree.repository;\n\nimport com.municipal.tree.entity.ConstructionSection;\nimport org.springframework.data.jpa.repository.JpaRepository;\nimport org.springframework.stereotype.Repository;\n\nimport java.util.List;\n\n@Repository\npublic interface ConstructionSectionRepository extends JpaRepository<ConstructionSection, Long> {\n    List<ConstructionSection> findByCurrentApplicationNo(String applicationNo);\n}\n")
print("2")

with open(os.path.join(base, "CompletionPhotoRepository.java"), "w") as f:
    f.write("package com.municipal.tree.repository;\n\nimport com.municipal.tree.entity.CompletionPhoto;\nimport org.springframework.data.jpa.repository.JpaRepository;\nimport org.springframework.stereotype.Repository;\n\nimport java.util.List;\n\n@Repository\npublic interface CompletionPhotoRepository extends JpaRepository<CompletionPhoto, Long> {\n    List<CompletionPhoto> findByApplicationId(Long applicationId);\n}\n")
print("3")

with open(os.path.join(base, "PruningApplicationRepository.java"), "w") as f:
    f.write("package com.municipal.tree.repository;\n\nimport com.municipal.tree.entity.PruningApplication;\nimport com.municipal.tree.enums.ApplicationStatus;\nimport org.springframework.data.jpa.repository.JpaRepository;\nimport org.springframework.data.jpa.repository.Query;\nimport org.springframework.data.repository.query.Param;\nimport org.springframework.stereotype.Repository;\n\nimport java.time.LocalDate;\nimport java.util.List;\n\n@Repository\npublic interface PruningApplicationRepository extends JpaRepository<PruningApplication, Long> {\n    PruningApplication findByApplicationNo(String applicationNo);\n    List<PruningApplication> findByStatus(ApplicationStatus status);\n}\n")
print("4")
print("Done!")
