
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class IdentityDocument {
    
    private String documentType;
    private String documentNumber;
    
    public IdentityDocument() {
    }
    
    public IdentityDocument(String documentType, String documentNumber) {
        this.documentType = documentType;
        this.documentNumber = documentNumber;
    }
    
    public String getDocumentType() {
        return this.documentType;
    }
    
    public void setDocumentType(String documentType) {
        this.documentType = documentType;
    }
    
    public String getDocumentNumber() {
        return this.documentNumber;
    }
    
    public void setDocumentNumber(String documentNumber) {
        this.documentNumber = documentNumber;
    }
}