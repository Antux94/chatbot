
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BIdentityDocument {
    private String documentType;
    private String documentNumber;
    
    public BIdentityDocument() {
    }
    
    public BIdentityDocument(String documentType, String documentNumber) {
        this.documentType = documentType;
        this.documentNumber = documentNumber;
    }
    
    public String getDocumentType() {
        return documentType;
    }
    
    public void setDocumentType(String documentType) {
        this.documentType = documentType;
    }
    
    public String getDocumentNumber() {
        return documentNumber;
    }
    
    public void setDocumentNumber(String documentNumber) {
        this.documentNumber = documentNumber;
    }
}