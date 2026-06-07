package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Data;
import java.time.LocalDate;

@Data
public class PruningApplicationRequest {
    @NotBlank(message = "树木编号不能为空")
    private String treeCode;

    @NotBlank(message = "申请人不能为空")
    private String applicant;

    @NotBlank(message = "养护单位不能为空")
    private String maintenanceUnit;

    @NotBlank(message = "修剪原因不能为空")
    private String pruningReason;

    private String pruningScheme;

    @NotNull(message = "计划开始日期不能为空")
    private LocalDate plannedStartDate;

    @NotNull(message = "计划结束日期不能为空")
    private LocalDate plannedEndDate;

    private Boolean occupyRoad;

    private String roadSection;
}
