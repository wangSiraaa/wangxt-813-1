package com.municipal.tree.validator;

import com.municipal.tree.entity.PruningApplication;
import com.municipal.tree.entity.Tree;
import com.municipal.tree.enums.TreeCategory;
import com.municipal.tree.exception.BusinessException;
import com.municipal.tree.repository.CompletionPhotoRepository;
import com.municipal.tree.repository.PruningApplicationRepository;
import org.springframework.stereotype.Component;

import java.time.LocalDate;

@Component
public class BusinessRuleValidator {

    private final PruningApplicationRepository pruningApplicationRepository;
    private final CompletionPhotoRepository completionPhotoRepository;

    public BusinessRuleValidator(PruningApplicationRepository pruningApplicationRepository,
                                  CompletionPhotoRepository completionPhotoRepository) {
        this.pruningApplicationRepository = pruningApplicationRepository;
        this.completionPhotoRepository = completionPhotoRepository;
    }

    public void validateRoadOccupationConflict(String roadSection, LocalDate startDate, LocalDate endDate, Long excludeApplicationId) {
        var conflicting = pruningApplicationRepository.findConflictingRoadOccupations(roadSection, startDate, endDate, excludeApplicationId);
        for (var app : conflicting) {
            if (!app.getId().equals(excludeApplicationId)) {
                throw new BusinessException(400, "占道施工时间冲突");
            }
        }
    }

    public boolean requiresExpertApproval(Tree tree) {
        return tree.getCategory() == TreeCategory.ANCIENT_AND_FAMOUS;
    }

    public void validateClosePermission(PruningApplication application) {
        var photos = completionPhotoRepository.findByApplicationId(application.getId());
        if (photos.isEmpty()) {
            throw new BusinessException(400, "未上传完工照片，不能关闭许可");
        }
    }
}
