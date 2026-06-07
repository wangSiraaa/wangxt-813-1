package com.municipal.tree.service;

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
