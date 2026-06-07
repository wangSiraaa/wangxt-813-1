package com.municipal.tree.repository;

import com.municipal.tree.entity.Tree;
import com.municipal.tree.enums.TreeCategory;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface TreeRepository extends JpaRepository<Tree, Long> {
    Optional<Tree> findByTreeCode(String treeCode);
    List<Tree> findByCategory(TreeCategory category);
    List<Tree> findByStreet(String street);
}
