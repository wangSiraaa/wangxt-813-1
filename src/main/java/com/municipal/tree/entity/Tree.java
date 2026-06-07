package com.municipal.tree.entity;
import com.municipal.tree.enums.TreeCategory;
import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "tree_archive")
public class Tree {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(nullable = false, unique = true)
    private String treeCode;
    @Column(nullable = false)
    private String species;
    @Column(nullable = false)
    private String location;
    private String street;
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private TreeCategory category;
    private Integer age;
    private Double diameter;
    private String healthStatus;
    private LocalDate plantDate;
    private String maintenanceUnit;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTreeCode() {
        return treeCode;
    }

    public void setTreeCode(String treeCode) {
        this.treeCode = treeCode;
    }

    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public TreeCategory getCategory() {
        return category;
    }

    public void setCategory(TreeCategory category) {
        this.category = category;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Double getDiameter() {
        return diameter;
    }

    public void setDiameter(Double diameter) {
        this.diameter = diameter;
    }

    public String getHealthStatus() {
        return healthStatus;
    }

    public void setHealthStatus(String healthStatus) {
        this.healthStatus = healthStatus;
    }

    public LocalDate getPlantDate() {
        return plantDate;
    }

    public void setPlantDate(LocalDate plantDate) {
        this.plantDate = plantDate;
    }

    public String getMaintenanceUnit() {
        return maintenanceUnit;
    }

    public void setMaintenanceUnit(String maintenanceUnit) {
        this.maintenanceUnit = maintenanceUnit;
    }
}
