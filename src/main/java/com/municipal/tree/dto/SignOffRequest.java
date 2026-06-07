package com.municipal.tree.dto;

import jakarta.validation.constraints.NotBlank;

public class SignOffRequest {
    @NotBlank
    private String signOffPerson;
    private String rejectReason;

    public String getSignOffPerson() { return signOffPerson; }
    public void setSignOffPerson(String signOffPerson) { this.signOffPerson = signOffPerson; }
    public String getRejectReason() { return rejectReason; }
    public void setRejectReason(String rejectReason) { this.rejectReason = rejectReason; }
}
