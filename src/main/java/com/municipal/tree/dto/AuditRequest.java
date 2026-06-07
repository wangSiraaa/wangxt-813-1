package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.Data;

@Data
public class AuditRequest {
    @NotBlank(message = "审核人不能为空")
    private String auditor;

    @NotNull(message = "审核结果不能为空")
    private Boolean approved;

    private String opinion;
}
