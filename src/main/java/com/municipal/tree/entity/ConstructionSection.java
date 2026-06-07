package com.municipal.tree.entity;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Data
@Entity
@Table(name = "construction_section")
public class ConstructionSection {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String sectionName;

    @Column(nullable = false)
    private String location;

    private LocalDate occupyStartDate;

    private LocalDate occupyEndDate;

    private String currentApplicationNo;

    private Boolean isOccupied;
}
