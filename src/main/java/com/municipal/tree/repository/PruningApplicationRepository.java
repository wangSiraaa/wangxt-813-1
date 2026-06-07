package com.municipal.tree.repository;

import com.municipal.tree.entity.PruningApplication;
import com.municipal.tree.enums.ApplicationStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Repository
public interface PruningApplicationRepository extends JpaRepository<PruningApplication, Long> {
    Optional<PruningApplication> findByApplicationNo(String applicationNo);
    List<PruningApplication> findByStatus(ApplicationStatus status);
    
    @Query("SELECT p FROM PruningApplication p WHERE p.roadSection = :roadSection AND p.status IN ('STREET_REVIEW', 'EXPERT_APPROVAL', 'APPROVED', 'IN_CONSTRUCTION') AND p.id != :excludeId AND ((p.plannedStartDate <= :endDate AND p.plannedEndDate >= :startDate))")
    List<PruningApplication> findConflictingRoadOccupations(@Param("roadSection") String roadSection, @Param("startDate") LocalDate startDate, @Param("endDate") LocalDate endDate, @Param("excludeId") Long excludeId);
}
