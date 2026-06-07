package com.municipal.tree.repository;

import com.municipal.tree.entity.ConstructionSection;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ConstructionSectionRepository extends JpaRepository<ConstructionSection, Long> {
    Optional<ConstructionSection> findBySectionName(String sectionName);
}
