package com.municipal.tree.validator;

import com.municipal.tree.entity.CompletionPhoto;
import com.municipal.tree.entity.PruningApplication;
import com.municipal.tree.entity.Tree;
import com.municipal.tree.enums.ApplicationStatus;
import com.municipal.tree.enums.TreeCategory;
import com.municipal.tree.exception.BusinessException;
import com.municipal.tree.repository.CompletionPhotoRepository;
import com.municipal.tree.repository.PruningApplicationRepository;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

@Component
public class BusinessRuleValidator {

    private final PruningApplicationRepository pruningApplicationRepository;
    private final CompletionPhotoRepository completionPhotoRepository;

    public BusinessRuleValidator(PruningApplicationRepository pruningApplicationRepository, CompletionPhotoRepository completionPhotoRepository) {
        this.pruningApplicationRepository = pruningApplicationRepository;
        this.completionPhotoRepository = completionPhotoRepository;
    }

    public boolean requiresExpertApproval(Tree tree) {
        return tree.getCategory() == TreeCategory.ANCIENT_AND_FAMOUS;
    }

    public void validateRoadOccupationConflict(String roadSection, LocalDate startDate, LocalDate endDate, Long excludeId) {
        List<ApplicationStatus> activeStatuses = Arrays.asList(
            ApplicationStatus.STREET_REVIEW,
            ApplicationStatus.EXPERT_APPROVAL,
            ApplicationStatus.APPROVED,
            ApplicationStatus.IN_CONSTRUCTION
        );
        List<PruningApplication> conflicts = pruningApplicationRepository.findConflictingRoadOccupations(
                roadSection, startDate, endDate, excludeId, activeStatuses
        );
        if (!conflicts.isEmpty()) {
            throw new BusinessException(400, "该路段在申请时间段内已被占用");
        }
    }

    public void validateClosePermission(PruningApplication application) {
        if (application.getStatus() != ApplicationStatus.COMPLETED &&
            application.getStatus() != ApplicationStatus.ARRIVAL_RECORDED) {
            throw new BusinessException(400, "只有已完成或已记录到场的申请才能关闭");
        }
        List<CompletionPhoto> photos = completionPhotoRepository.findByApplicationId(application.getId());
        if (photos == null || photos.isEmpty()) {
            throw new BusinessException(400, "未上传完工照片，不能关闭许可");
        }
    }
}
