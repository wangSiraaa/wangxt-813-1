package com.municipal.tree.repository;

import com.municipal.tree.entity.CompletionPhoto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CompletionPhotoRepository extends JpaRepository<CompletionPhoto, Long> {
    List<CompletionPhoto> findByApplicationId(Long applicationId);
}
