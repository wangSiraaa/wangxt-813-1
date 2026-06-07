package com.municipal.tree.entity;

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
