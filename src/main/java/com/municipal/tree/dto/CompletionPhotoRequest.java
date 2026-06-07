package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;

@Data
public class CompletionPhotoRequest {
    @NotBlank(message = "照片URL不能为空")
    private String photoUrl;

    private String description;

    @NotBlank(message = "上传人不能为空")
    private String uploader;
}
