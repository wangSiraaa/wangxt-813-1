package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;

public class CompletionPhotoRequest {
    @NotBlank
    private String photoUrl;
    private String description;
    @NotBlank
    private String uploader;

    public String getPhotoUrl() { return photoUrl; }
    public void setPhotoUrl(String photoUrl) { this.photoUrl = photoUrl; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getUploader() { return uploader; }
    public void setUploader(String uploader) { this.uploader = uploader; }
}
