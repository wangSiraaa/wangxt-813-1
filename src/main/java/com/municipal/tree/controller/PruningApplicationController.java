package com.municipal.tree.controller;

import com.municipal.tree.dto.ApiResponse;
import com.municipal.tree.dto.AuditRequest;
import com.municipal.tree.dto.CompletionPhotoRequest;
import com.municipal.tree.dto.PruningApplicationRequest;
import com.municipal.tree.entity.*;
import com.municipal.tree.service.PruningApplicationService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/pruning")
public class PruningApplicationController {

    private final PruningApplicationService pruningApplicationService;

    public PruningApplicationController(PruningApplicationService pruningApplicationService) {
        this.pruningApplicationService = pruningApplicationService;
    }

    @PostMapping("/applications")
    public ApiResponse<PruningApplication> submitApplication(@RequestBody PruningApplicationRequest request) {
        PruningApplication application = pruningApplicationService.submitApplication(request);
        return ApiResponse.success(application);
    }

    @GetMapping("/applications")
    public ApiResponse<List<PruningApplication>> getAllApplications() {
        List<PruningApplication> applications = pruningApplicationService.getAllApplications();
        return ApiResponse.success(applications);
    }

    @GetMapping("/applications/{id}")
    public ApiResponse<PruningApplication> getApplicationById(@PathVariable Long id) {
        PruningApplication application = pruningApplicationService.getApplicationById(id);
        return ApiResponse.success(application);
    }

    @GetMapping("/applications/no/{applicationNo}")
    public ApiResponse<PruningApplication> getApplicationByNo(@PathVariable String applicationNo) {
        PruningApplication application = pruningApplicationService.getApplicationByNo(applicationNo);
        return ApiResponse.success(application);
    }

    @GetMapping("/applications/expert/pending")
    public ApiResponse<List<PruningApplication>> getExpertPendingApplications() {
        List<PruningApplication> applications = pruningApplicationService.getExpertPendingApplications();
        return ApiResponse.success(applications);
    }

    @PostMapping("/applications/{id}/street-audit")
    public ApiResponse<PruningApplication> streetAudit(@PathVariable Long id, @RequestBody AuditRequest request) {
        PruningApplication application = pruningApplicationService.streetAudit(id, request);
        return ApiResponse.success(application);
    }

    @PostMapping("/applications/{id}/expert-audit")
    public ApiResponse<PruningApplication> expertAudit(@PathVariable Long id, @RequestBody AuditRequest request) {
        PruningApplication application = pruningApplicationService.expertAudit(id, request);
        return ApiResponse.success(application);
    }

    @PostMapping("/applications/{id}/start-construction")
    public ApiResponse<PruningApplication> startConstruction(@PathVariable Long id) {
        PruningApplication application = pruningApplicationService.startConstruction(id);
        return ApiResponse.success(application);
    }

    @PostMapping("/applications/{id}/complete-construction")
    public ApiResponse<PruningApplication> completeConstruction(@@PathVariable Long id) {
        PruningApplication application = pruningApplicationService.completeConstruction(id);
        return ApiResponse.success(application);
    }

    @PostMapping("/applications/{id}/photos")
    public ApiResponse<CompletionPhoto> uploadCompletionPhoto(@PathVariable Long id, @RequestBody CompletionPhotoRequest request) {
        CompletionPhoto photo = pruningApplicationService.uploadCompletionPhoto(id, request);
        return ApiResponse.success(photo);
    }

    @GetMapping("/applications/{id}/photos")
    public ApiResponse<List<CompletionPhoto>> getCompletionPhotos(@PathVariable Long id) {
        List<CompletionPhoto> photos = pruningApplicationService.getCompletionPhotos(id);
        return ApiResponse.success(photos);
    }

    @PostMapping("/applications/{id}/close")
    public ApiResponse<PruningApplication> closeApplication(@PathVariable Long id) {
        PruningApplication application = pruningApplicationService.closeApplication(id);
        return ApiResponse.success(application);
    }

    @GetMapping("/applications/{id}/audit-records")
    public ApiResponse<List<AuditRecord>> getAuditRecords(@PathVariable Long id) {
        List<AuditRecord> records = pruningApplicationService.getAuditRecords(id);
        return ApiResponse.success(records);
    }

    @GetMapping("/trees")
    public ApiResponse<List<Tree>> getAllTrees() {
        List<Tree> trees = pruningApplicationService.getAllTrees();
        return ApiResponse.success(trees);
    }

    @GetMapping("/trees/{id}")
    public ApiResponse<Tree> getTreeById(@PathVariable Long id) {
        Tree tree = pruningApplicationService.getTreeById(id);
        return ApiResponse.success(tree);
    }

    @GetMapping("/construction-sections")
    public ApiResponse<List<ConstructionSection>> getAllConstructionSections() {
        List<ConstructionSection> sections = pruningApplicationService.getAllConstructionSections();
        return ApiResponse.success(sections);
    }
}
