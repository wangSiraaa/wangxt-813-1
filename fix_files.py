#!/usr/bin/env python3
import os

base_dir = "/Users/mingyuan/workspace/sihuo/wangxtw3/813/src/main/java/com/municipal/tree"

# 修复 PruningApplication.java
pruning_app_content = '''package com.municipal.tree.entity;

import com.municipal.tree.enums.ApplicationStatus;
import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "pruning_application")
public class PruningApplication {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String applicationNo;

    private Long treeId;

    private String applicant;

    private String maintenanceUnit;

    private String pruningReason;

    private String pruningScheme;

    private LocalDate plannedStartDate;

    private LocalDate plannedEndDate;

    private Boolean occupyRoad;

    private String roadSection;

    @Enumerated(EnumType.STRING)
    private ApplicationStatus status;

    private String streetAuditor;

    private String expert;

    private String streetAuditOpinion;

    private String expertOpinion;

    private String rejectReason;

    private LocalDateTime submitTime;

    private LocalDateTime streetAuditTime;

    private LocalDateTime expertAuditTime;

    private LocalDateTime constructionStartTime;

    private LocalDateTime constructionEndTime;

    private LocalDateTime closeTime;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getApplicationNo() { return applicationNo; }
    public void setApplicationNo(String applicationNo) { this.applicationNo = applicationNo; }
    public Long getTreeId() { return treeId; }
    public void setTreeId(Long treeId) { this.treeId = treeId; }
    public String getApplicant() { return applicant; }
    public void setApplicant(String applicant) { this.applicant = applicant; }
    public String getMaintenanceUnit() { return maintenanceUnit; }
    public void setMaintenanceUnit(String maintenanceUnit) { this.maintenanceUnit = maintenanceUnit; }
    public String getPruningReason() { return pruningReason; }
    public void setPruningReason(String pruningReason) { this.pruningReason = pruningReason; }
    public String getPruningScheme() { return pruningScheme; }
    public void setPruningScheme(String pruningScheme) { this.pruningScheme = pruningScheme; }
    public LocalDate getPlannedStartDate() { return plannedStartDate; }
    public void setPlannedStartDate(LocalDate plannedStartDate) { this.plannedStartDate = plannedStartDate; }
    public LocalDate getPlannedEndDate() { return plannedEndDate; }
    public void setPlannedEndDate(LocalDate plannedEndDate) { this.plannedEndDate = plannedEndDate; }
    public Boolean getOccupyRoad() { return occupyRoad; }
    public void setOccupyRoad(Boolean occupyRoad) { this.occupyRoad = occupyRoad; }
    public String getRoadSection() { return roadSection; }
    public void setRoadSection(String roadSection) { this.roadSection = roadSection; }
    public ApplicationStatus getStatus() { return status; }
    public void setStatus(ApplicationStatus status) { this.status = status; }
    public String getStreetAuditor() { return streetAuditor; }
    public void setStreetAuditor(String streetAuditor) { this.streetAuditor = streetAuditor; }
    public String getExpert() { return expert; }
    public void setExpert(String expert) { this.expert = expert; }
    public String getStreetAuditOpinion() { return streetAuditOpinion; }
    public void setStreetAuditOpinion(String streetAuditOpinion) { this.streetAuditOpinion = streetAuditOpinion; }
    public String getExpertOpinion() { return expertOpinion; }
    public void setExpertOpinion(String expertOpinion) { this.expertOpinion = expertOpinion; }
    public String getRejectReason() { return rejectReason; }
    public void setRejectReason(String rejectReason) { this.rejectReason = rejectReason; }
    public LocalDateTime getSubmitTime() { return submitTime; }
    public void setSubmitTime(LocalDateTime submitTime) { this.submitTime = submitTime; }
    public LocalDateTime getStreetAuditTime() { return streetAuditTime; }
    public void setStreetAuditTime(LocalDateTime streetAuditTime) { this.streetAuditTime = streetAuditTime; }
    public LocalDateTime getExpertAuditTime() { return expertAuditTime; }
    public void setExpertAuditTime(LocalDateTime expertAuditTime) { this.expertAuditTime = expertAuditTime; }
    public LocalDateTime getConstructionStartTime() { return constructionStartTime; }
    public void setConstructionStartTime(LocalDateTime constructionStartTime) { this.constructionStartTime = constructionStartTime; }
    public LocalDateTime getConstructionEndTime() { return constructionEndTime; }
    public void setConstructionEndTime(LocalDateTime constructionEndTime) { this.constructionEndTime = constructionEndTime; }
    public LocalDateTime getCloseTime() { return closeTime; }
    public void setCloseTime(LocalDateTime closeTime) { this.closeTime = closeTime; }
}
'''

with open(os.path.join(base_dir, "entity/PruningApplication.java"), "w") as f:
    f.write(pruning_app_content)

# 修复 AuditRecord.java
audit_record_content = '''package com.municipal.tree.entity;

import com.municipal.tree.enums.RoleType;
import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "audit_record")
public class AuditRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long applicationId;

    private String auditor;

    @Enumerated(EnumType.STRING)
    private RoleType auditorRole;

    private Boolean approved;

    private String opinion;

    private LocalDateTime auditTime;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getApplicationId() { return applicationId; }
    public void setApplicationId(Long applicationId) { this.applicationId = applicationId; }
    public String getAuditor() { return auditor; }
    public void setAuditor(String auditor) { this.auditor = auditor; }
    public RoleType getAuditorRole() { return auditorRole; }
    public void setAuditorRole(RoleType auditorRole) { this.auditorRole = auditorRole; }
    public Boolean getApproved() { return approved; }
    public void setApproved(Boolean approved) { this.approved = approved; }
    public String getOpinion() { return opinion; }
    public void setOpinion(String opinion) { this.opinion = opinion; }
    public LocalDateTime getAuditTime() { return auditTime; }
    public void setAuditTime(LocalDateTime auditTime) { this.auditTime = auditTime; }
}
'''

with open(os.path.join(base_dir, "entity/AuditRecord.java"), "w") as f:
    f.write(audit_record_content)

# 修复 ConstructionSection.java
construction_section_content = '''package com.municipal.tree.entity;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "construction_section")
public class ConstructionSection {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String sectionName;

    private String location;

    private LocalDate occupyStartDate;

    private LocalDate occupyEndDate;

    private String currentApplicationNo;

    private Boolean isOccupied;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getSectionName() { return sectionName; }
    public void setSectionName(String sectionName) { this.sectionName = sectionName; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public LocalDate getOccupyStartDate() { return occupyStartDate; }
    public void setOccupyStartDate(LocalDate occupyStartDate) { this.occupyStartDate = occupyStartDate; }
    public LocalDate getOccupyEndDate() { return occupyEndDate; }
    public void setOccupyEndDate(LocalDate occupyEndDate) { this.occupyEndDate = occupyEndDate; }
    public String getCurrentApplicationNo() { return currentApplicationNo; }
    public void setCurrentApplicationNo(String currentApplicationNo) { this.currentApplicationNo = currentApplicationNo; }
    public Boolean getIsOccupied() { return isOccupied; }
    public void setIsOccupied(Boolean isOccupied) { this.isOccupied = isOccupied; }
}
'''

with open(os.path.join(base_dir, "entity/ConstructionSection.java"), "w") as f:
    f.write(construction_section_content)

# 修复 CompletionPhoto.java
completion_photo_content = '''package com.municipal.tree.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "completion_photo")
public class CompletionPhoto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long applicationId;

    private String photoUrl;

    private String description;

    private String uploader;

    private LocalDateTime uploadTime;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getApplicationId() { return applicationId; }
    public void setApplicationId(Long applicationId) { this.applicationId = applicationId; }
    public String getPhotoUrl() { return photoUrl; }
    public void setPhotoUrl(String photoUrl) { this.photoUrl = photoUrl; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getUploader() { return uploader; }
    public void setUploader(String uploader) { this.uploader = uploader; }
    public LocalDateTime getUploadTime() { return uploadTime; }
    public void setUploadTime(LocalDateTime uploadTime) { this.uploadTime = uploadTime; }
}
'''

with open(os.path.join(base_dir, "entity/CompletionPhoto.java"), "w") as f:
    f.write(completion_photo_content)

# 修复 DTO 类
# ApiResponse.java
api_response_content = '''package com.municipal.tree.dto;

public class ApiResponse<T> {

    private int code;
    private String message;
    private T data;

    public ApiResponse() {}

    public ApiResponse(int code, String message, T data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(200, "success", data);
    }

    public static <T> ApiResponse<T> success(String message, T data) {
        return new ApiResponse<>(200, message, data);
    }

    public static <T> ApiResponse<T> error(int code, String message) {
        return new ApiResponse<>(code, message, null);
    }

    public static <T> ApiResponse<T> error(String message) {
        return new ApiResponse<>(500, message, null);
    }

    public int getCode() { return code; }
    public void setCode(int code) { this.code = code; }
    public String getMessage() { return message; }
    public void setMessage(String message) { this.message = message; }
    public T getData() { return data; }
    public void setData(T data) { this.data = data; }
}
'''

with open(os.path.join(base_dir, "dto/ApiResponse.java"), "w") as f:
    f.write(api_response_content)

# PruningApplicationRequest.java
pruning_app_request_content = '''package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.time.LocalDate;

public class PruningApplicationRequest {
    @NotBlank
    private String treeCode;
    @NotBlank
    private String applicant;
    @NotBlank
    private String maintenanceUnit;
    @NotBlank
    private String pruningReason;
    private String pruningScheme;
    @NotNull
    private LocalDate plannedStartDate;
    @NotNull
    private LocalDate plannedEndDate;
    private Boolean occupyRoad;
    private String roadSection;

    public String getTreeCode() { return treeCode; }
    public void setTreeCode(String treeCode) { this.treeCode = treeCode; }
    public String getApplicant() { return applicant; }
    public void setApplicant(String applicant) { this.applicant = applicant; }
    public String getMaintenanceUnit() { return maintenanceUnit; }
    public void setMaintenanceUnit(String maintenanceUnit) { this.maintenanceUnit = maintenanceUnit; }
    public String getPruningReason() { return pruningReason; }
    public void setPruningReason(String pruningReason) { this.pruningReason = pruningReason; }
    public String getPruningScheme() { return pruningScheme; }
    public void setPruningScheme(String pruningScheme) { this.pruningScheme = pruningScheme; }
    public LocalDate getPlannedStartDate() { return plannedStartDate; }
    public void setPlannedStartDate(LocalDate plannedStartDate) { this.plannedStartDate = plannedStartDate; }
    public LocalDate getPlannedEndDate() { return plannedEndDate; }
    public void setPlannedEndDate(LocalDate plannedEndDate) { this.plannedEndDate = plannedEndDate; }
    public Boolean getOccupyRoad() { return occupyRoad; }
    public void setOccupyRoad(Boolean occupyRoad) { this.occupyRoad = occupyRoad; }
    public String getRoadSection() { return roadSection; }
    public void setRoadSection(String roadSection) { this.roadSection = roadSection; }
}
'''

with open(os.path.join(base_dir, "dto/PruningApplicationRequest.java"), "w") as f:
    f.write(pruning_app_request_content)

# AuditRequest.java
audit_request_content = '''package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class AuditRequest {
    @NotBlank
    private String auditor;
    @NotNull
    private Boolean approved;
    private String opinion;

    public String getAuditor() { return auditor; }
    public void setAuditor(String auditor) { this.auditor = auditor; }
    public Boolean getApproved() { return approved; }
    public void setApproved(Boolean approved) { this.approved = approved; }
    public String getOpinion() { return opinion; }
    public void setOpinion(String opinion) { this.opinion = opinion; }
}
'''

with open(os.path.join(base_dir, "dto/AuditRequest.java"), "w") as f:
    f.write(audit_request_content)

# CompletionPhotoRequest.java
completion_photo_request_content = '''package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;

public class CompletionPhotoRequest {
    @NotBlank
    private String photoUrl;
    private String description;
    @NotBlank
    private String uploader;

    public String getPhotoUrl() { return photoUrl; }
    public void setPhotoUrl(String photoUrl) { this.photoUrl = photoUrl; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getUploader() { return uploader; }
    public void setUploader(String uploader) { this.uploader = uploader; }
}
'''

with open(os.path.join(base_dir, "dto/CompletionPhotoRequest.java"), "w") as f:
    f.write(completion_photo_request_content)

print("所有实体类和DTO类已修复完成！")

# 修复 PruningApplicationService.java
service_content = '''package com.municipal.tree.service;

import com.municipal.tree.dto.AuditRequest;
import com.municipal.tree.dto.CompletionPhotoRequest;
import com.municipal.tree.dto.PruningApplicationRequest;
import com.municipal.tree.entity.*;
import com.municipal.tree.enums.ApplicationStatus;
import com.municipal.tree.enums.TreeCategory;
import com.municipal.tree.exception.BusinessException;
import com.municipal.tree.repository.*;
import com.municipal.tree.validator.BusinessRuleValidator;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

@Service
@Transactional
public class PruningApplicationService {

    private final PruningApplicationRepository pruningApplicationRepository;
    private final TreeRepository treeRepository;
    private final AuditRecordRepository auditRecordRepository;
    private final CompletionPhotoRepository completionPhotoRepository;
    private final ConstructionSectionRepository constructionSectionRepository;
    private final BusinessRuleValidator businessRuleValidator;

    public PruningApplicationService(PruningApplicationRepository pruningApplicationRepository,
                                      TreeRepository treeRepository,
                                      AuditRecordRepository auditRecordRepository,
                                      CompletionPhotoRepository completionPhotoRepository,
                                      ConstructionSectionRepository constructionSectionRepository,
                                      BusinessRuleValidator businessRuleValidator) {
        this.pruningApplicationRepository = pruningApplicationRepository;
        this.treeRepository = treeRepository;
        this.auditRecordRepository = auditRecordRepository;
        this.completionPhotoRepository = completionPhotoRepository;
        this.constructionSectionRepository = constructionSectionRepository;
        this.businessRuleValidator = businessRuleValidator;
    }

    public PruningApplication submitApplication(PruningApplicationRequest request) {
        Tree tree = treeRepository.findByTreeCode(request.getTreeCode())
                .orElseThrow(() -> new BusinessException(404, "树木不存在"));

        if (request.getOccupyRoad()) {
            businessRuleValidator.validateRoadOccupationConflict(
                    request.getRoadSection(),
                    request.getPlannedStartDate(),
                    request.getPlannedEndDate(),
                    null
            );
        }

        PruningApplication application = new PruningApplication();
        application.setTreeId(tree.getId());
        application.setApplicant(request.getApplicant());
        application.setMaintenanceUnit(request.getMaintenanceUnit());
        application.setPruningReason(request.getPruningReason());
        application.setPruningScheme(request.getPruningScheme());
        application.setOccupyRoad(request.getOccupyRoad());
        application.setRoadSection(request.getRoadSection());
        application.setPlannedStartDate(request.getPlannedStartDate());
        application.setPlannedEndDate(request.getPlannedEndDate());

        String applicationNo = "PRU" + UUID.randomUUID().toString().replace("-", "").substring(0, 12).toUpperCase();
        application.setApplicationNo(applicationNo);
        application.setSubmitTime(LocalDateTime.now());

        boolean needsExpertApproval = businessRuleValidator.requiresExpertApproval(tree);
        if (needsExpertApproval) {
            application.setStatus(ApplicationStatus.EXPERT_APPROVAL);
        } else {
            application.setStatus(ApplicationStatus.STREET_REVIEW);
        }

        application = pruningApplicationRepository.save(application);

        if (request.getOccupyRoad()) {
            ConstructionSection section = new ConstructionSection();
            section.setSectionName(request.getRoadSection());
            section.setOccupyStartDate(request.getPlannedStartDate());
            section.setOccupyEndDate(request.getPlannedEndDate());
            section.setCurrentApplicationNo(application.getApplicationNo());
            section.setIsOccupied(true);
            constructionSectionRepository.save(section);
        }

        return application;
    }

    public PruningApplication streetAudit(Long applicationId, AuditRequest request) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        if (application.getStatus() != ApplicationStatus.STREET_REVIEW) {
            throw new BusinessException(400, "当前状态不允许街道审核");
        }

        Tree tree = treeRepository.findById(application.getTreeId())
                .orElseThrow(() -> new BusinessException(404, "树木不存在"));

        if (tree.getCategory() == TreeCategory.ANCIENT_AND_FAMOUS) {
            throw new BusinessException(400, "古树名木不能由街道审核");
        }

        AuditRecord auditRecord = new AuditRecord();
        auditRecord.setApplicationId(applicationId);
        auditRecord.setAuditor(request.getAuditor());
        auditRecord.setApproved(request.getApproved());
        auditRecord.setOpinion(request.getOpinion());
        auditRecord.setAuditTime(LocalDateTime.now());
        auditRecordRepository.save(auditRecord);

        if (request.getApproved()) {
            application.setStatus(ApplicationStatus.APPROVED);
        } else {
            application.setStatus(ApplicationStatus.REJECTED);
        }

        return pruningApplicationRepository.save(application);
    }

    public PruningApplication expertAudit(Long applicationId, AuditRequest request) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        if (application.getStatus() != ApplicationStatus.EXPERT_APPROVAL) {
            throw new BusinessException(400, "当前状态不允许专家审批");
        }

        AuditRecord auditRecord = new AuditRecord();
        auditRecord.setApplicationId(applicationId);
        auditRecord.setAuditor(request.getAuditor());
        auditRecord.setApproved(request.getApproved());
        auditRecord.setOpinion(request.getOpinion());
        auditRecord.setAuditTime(LocalDateTime.now());
        auditRecordRepository.save(auditRecord);

        if (request.getApproved()) {
            application.setStatus(ApplicationStatus.APPROVED);
        } else {
            application.setStatus(ApplicationStatus.REJECTED);
        }

        return pruningApplicationRepository.save(application);
    }

    public PruningApplication startConstruction(Long applicationId) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        if (application.getStatus() != ApplicationStatus.APPROVED) {
            throw new BusinessException(400, "当前状态不允许开始施工");
        }

        application.setStatus(ApplicationStatus.IN_CONSTRUCTION);
        application.setConstructionStartTime(LocalDateTime.now());
        return pruningApplicationRepository.save(application);
    }

    public PruningApplication completeConstruction(Long applicationId) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        if (application.getStatus() != ApplicationStatus.IN_CONSTRUCTION) {
            throw new BusinessException(400, "当前状态不允许完成施工");
        }

        application.setStatus(ApplicationStatus.COMPLETED);
        application.setConstructionEndTime(LocalDateTime.now());
        return pruningApplicationRepository.save(application);
    }

    public CompletionPhoto uploadCompletionPhoto(Long applicationId, CompletionPhotoRequest request) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        CompletionPhoto photo = new CompletionPhoto();
        photo.setApplicationId(applicationId);
        photo.setPhotoUrl(request.getPhotoUrl());
        photo.setDescription(request.getDescription());
        photo.setUploader(request.getUploader());
        photo.setUploadTime(LocalDateTime.now());
        return completionPhotoRepository.save(photo);
    }

    public PruningApplication closeApplication(Long applicationId) {
        PruningApplication application = pruningApplicationRepository.findById(applicationId)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));

        if (application.getStatus() != ApplicationStatus.COMPLETED) {
            throw new BusinessException(400, "当前状态不允许关闭许可");
        }

        businessRuleValidator.validateClosePermission(application);

        application.setStatus(ApplicationStatus.CLOSED);
        application.setCloseTime(LocalDateTime.now());

        if (application.getOccupyRoad()) {
            List<ConstructionSection> sections = constructionSectionRepository.findAll();
            for (ConstructionSection section : sections) {
                if (application.getApplicationNo().equals(section.getCurrentApplicationNo())) {
                    section.setIsOccupied(false);
                    constructionSectionRepository.save(section);
                }
            }
        }

        return pruningApplicationRepository.save(application);
    }

    public PruningApplication getApplicationById(Long id) {
        return pruningApplicationRepository.findById(id)
                .orElseThrow(() -> new BusinessException(404, "申请不存在"));
    }

    public PruningApplication getApplicationByNo(String applicationNo) {
        return pruningApplicationRepository.findByApplicationNo(applicationNo);
    }

    public List<PruningApplication> getAllApplications() {
        return pruningApplicationRepository.findAll();
    }

    public List<PruningApplication> getExpertPendingApplications() {
        return pruningApplicationRepository.findByStatus(ApplicationStatus.EXPERT_APPROVAL);
    }

    public List<AuditRecord> getAuditRecords(Long applicationId) {
        return auditRecordRepository.findByApplicationIdOrderByAuditTimeDesc(applicationId);
    }

    public List<CompletionPhoto> getCompletionPhotos(Long applicationId) {
        return completionPhotoRepository.findByApplicationId(applicationId);
    }

    public List<ConstructionSection> getAllConstructionSections() {
        return constructionSectionRepository.findAll();
    }

    public List<Tree> getAllTrees() {
        return treeRepository.findAll();
    }

    public Tree getTreeById(Long id) {
        return treeRepository.findById(id)
                .orElseThrow(() -> new BusinessException(404, "树木不存在"));
    }
}
'''

with open(os.path.join(base_dir, "service/PruningApplicationService.java"), "w") as f:
    f.write(service_content)

print("PruningApplicationService.java 修复完成！")

# 修复 Repository 接口
# TreeRepository - 添加 findByTreeCode 方法
tree_repo_content = '''package com.municipal.tree.repository;

import com.municipal.tree.entity.Tree;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface TreeRepository extends JpaRepository<Tree, Long> {
    Optional<Tree> findByTreeCode(String treeCode);
}
'''

with open(os.path.join(base_dir, "repository/TreeRepository.java"), "w") as f:
    f.write(tree_repo_content)

print("TreeRepository.java 修复完成！")

# PruningApplicationRepository - 修复返回类型并添加必要方法
pruning_repo_content = '''package com.municipal.tree.repository;

import com.municipal.tree.entity.PruningApplication;
import com.municipal.tree.enums.ApplicationStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;

@Repository
public interface PruningApplicationRepository extends JpaRepository<PruningApplication, Long> {
    PruningApplication findByApplicationNo(String applicationNo);
    
    List<PruningApplication> findByStatus(ApplicationStatus status);
    
    @Query("SELECT p FROM PruningApplication p WHERE p.roadSection = :roadSection " +
           "AND p.status IN ('STREET_REVIEW', 'EXPERT_APPROVAL', 'APPROVED', 'IN_CONSTRUCTION') " +
           "AND p.id != :excludeId " +
           "AND ((p.plannedStartDate <= :endDate AND p.plannedEndDate >= :startDate))")
    List<PruningApplication> findConflictingRoadOccupations(
            @Param("roadSection") String roadSection,
            @Param("startDate") LocalDate startDate,
            @Param("endDate") LocalDate endDate,
            @Param("excludeId") Long excludeId);
}
'''

with open(os.path.join(base_dir, "repository/PruningApplicationRepository.java"), "w") as f:
    f.write(pruning_repo_content)

print("PruningApplicationRepository.java 修复完成！")

# ConstructionSectionRepository - 添加 findByApplicationId 方法
section_repo_content = '''package com.municipal.tree.repository;

import com.municipal.tree.entity.ConstructionSection;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ConstructionSectionRepository extends JpaRepository<ConstructionSection, Long> {
    List<ConstructionSection> findByCurrentApplicationNo(String applicationNo);
}
'''

with open(os.path.join(base_dir, "repository/ConstructionSectionRepository.java"), "w") as f:
    f.write(section_repo_content)

print("ConstructionSectionRepository.java 修复完成！")

# AuditRecordRepository - 确保方法存在
audit_repo_content = '''package com.municipal.tree.repository;

import com.municipal.tree.entity.AuditRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AuditRecordRepository extends JpaRepository<AuditRecord, Long> {
    List<AuditRecord> findByApplicationIdOrderByAuditTimeDesc(Long applicationId);
}
'''

with open(os.path.join(base_dir, "repository/AuditRecordRepository.java"), "w") as f:
    f.write(audit_repo_content)

print("AuditRecordRepository.java 修复完成！")

# CompletionPhotoRepository - 确保方法存在
photo_repo_content = '''package com.municipal.tree.repository;

import com.municipal.tree.entity.CompletionPhoto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CompletionPhotoRepository extends JpaRepository<CompletionPhoto, Long> {
    List<CompletionPhoto> findByApplicationId(Long applicationId);
}
'''

with open(os.path.join(base_dir, "repository/CompletionPhotoRepository.java"), "w") as f:
    f.write(photo_repo_content)

print("CompletionPhotoRepository.java 修复完成！")

# 修复 BusinessRuleValidator.java
validator_content = '''package com.municipal.tree.validator;

import com.municipal.tree.entity.PruningApplication;
import com.municipal.tree.entity.Tree;
import com.municipal.tree.enums.ApplicationStatus;
import com.municipal.tree.enums.TreeCategory;
import com.municipal.tree.exception.BusinessException;
import com.municipal.tree.repository.PruningApplicationRepository;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.List;

@Component
public class BusinessRuleValidator {

    private final PruningApplicationRepository pruningApplicationRepository;

    public BusinessRuleValidator(PruningApplicationRepository pruningApplicationRepository) {
        this.pruningApplicationRepository = pruningApplicationRepository;
    }

    public boolean requiresExpertApproval(Tree tree) {
        return tree.getCategory() == TreeCategory.ANCIENT_AND_FAMOUS;
    }

    public void validateRoadOccupationConflict(String roadSection, LocalDate startDate, LocalDate endDate, Long excludeId) {
        List<PruningApplication> conflicts = pruningApplicationRepository.findConflictingRoadOccupations(
                roadSection, startDate, endDate, excludeId
        );
        if (!conflicts.isEmpty()) {
            throw new BusinessException(400, "该路段在申请时间段内已被占用");
        }
    }

    public void validateClosePermission(PruningApplication application) {
        if (application.getStatus() != ApplicationStatus.COMPLETED) {
            throw new BusinessException(400, "只有已完成状态的申请才能关闭");
        }
    }
}
'''

with open(os.path.join(base_dir, "validator/BusinessRuleValidator.java"), "w") as f:
    f.write(validator_content)

print("BusinessRuleValidator.java 修复完成！")

print("\\n所有文件修复完成！现在可以运行 mvn compile 验证了。")

