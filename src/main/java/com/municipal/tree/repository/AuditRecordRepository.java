package com.municipal.tree.repository;

import com.municipal.tree.entity.AuditRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AuditRecordRepository extends JpaRepository<AuditRecord, Long> {
    List<AuditRecord> findByApplicationIdOrderByAuditTimeDesc(Long applicationId);
}
