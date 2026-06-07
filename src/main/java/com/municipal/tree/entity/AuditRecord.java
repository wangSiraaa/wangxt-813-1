package com.municipal.tree.entity;

import com.municipal.tree.enums.RoleType;
import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@Entity
@Table(name = "audit_record")
public class AuditRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private Long applicationId;

    @Column(nullable = false)
    private String auditor;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private RoleType auditorRole;

    @Column(nullable = false)
    private Boolean approved;

    private String opinion;

    private LocalDateTime auditTime;
}
