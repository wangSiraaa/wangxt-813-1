package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.time.LocalDate;

public class PruningApplicationRequest {
    @NotBlank
    private String treeCode;
    @NotBlank
    private String applicant;
    @NotBlank
    private String maintenanceUnit;
    @NotBlank
    private String pruningReason;
    private String pruningScheme;
    @NotNull
    private LocalDate plannedStartDate;
    @NotNull
    private LocalDate plannedEndDate;
    private Boolean occupyRoad;
    private String roadSection;

    public String getTreeCode() { return treeCode; }
    public void setTreeCode(String treeCode) { this.treeCode = treeCode; }
    public String getApplicant() { return applicant; }
    public void setApplicant(String applicant) { this.applicant = applicant; }
    public String getMaintenanceUnit() { return maintenanceUnit; }
    public void setMaintenanceUnit(String maintenanceUnit) { this.maintenanceUnit = maintenanceUnit; }
    public String getPruningReason() { return pruningReason; }
    public void setPruningReason(String pruningReason) { this.pruningReason = pruningReason; }
    public String getPruningScheme() { return pruningScheme; }
    public void setPruningScheme(String pruningScheme) { this.pruningScheme = pruningScheme; }
    public LocalDate getPlannedStartDate() { return plannedStartDate; }
    public void setPlannedStartDate(LocalDate plannedStartDate) { this.plannedStartDate = plannedStartDate; }
    public LocalDate getPlannedEndDate() { return plannedEndDate; }
    public void setPlannedEndDate(LocalDate plannedEndDate) { this.plannedEndDate = plannedEndDate; }
    public Boolean getOccupyRoad() { return occupyRoad; }
    public void setOccupyRoad(Boolean occupyRoad) { this.occupyRoad = occupyRoad; }
    public String getRoadSection() { return roadSection; }
    public void setRoadSection(String roadSection) { this.roadSection = roadSection; }
}
