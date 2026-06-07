package com.municipal.tree.entity;

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
