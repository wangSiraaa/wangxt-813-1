package com.municipal.tree.entity;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "construction_section")
public class ConstructionSection {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String sectionName;

    private String location;

    private LocalDate occupyStartDate;

    private LocalDate occupyEndDate;

    private String currentApplicationNo;

    private Boolean isOccupied;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getSectionName() { return sectionName; }
    public void setSectionName(String sectionName) { this.sectionName = sectionName; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public LocalDate getOccupyStartDate() { return occupyStartDate; }
    public void setOccupyStartDate(LocalDate occupyStartDate) { this.occupyStartDate = occupyStartDate; }
    public LocalDate getOccupyEndDate() { return occupyEndDate; }
    public void setOccupyEndDate(LocalDate occupyEndDate) { this.occupyEndDate = occupyEndDate; }
    public String getCurrentApplicationNo() { return currentApplicationNo; }
    public void setCurrentApplicationNo(String currentApplicationNo) { this.currentApplicationNo = currentApplicationNo; }
    public Boolean getIsOccupied() { return isOccupied; }
    public void setIsOccupied(Boolean isOccupied) { this.isOccupied = isOccupied; }
}
