
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BPerson {
    private BIdentityDocument identityDocument;
    private String firstName;
    private String middleName;
    private String lastName;
    private BLaboralInformation laboralInformation;
    
    public BIdentityDocument getIdentityDocument() {
        return identityDocument;
    }
    
    public void setIdentityDocument(BIdentityDocument identityDocument) {
        this.identityDocument = identityDocument;
    }
    
    public String getFirstName() {
        return firstName;
    }
    
    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }
    
    public String getMiddleName() {
        return middleName;
    }
    
    public void setMiddleName(String middleName) {
        this.middleName = middleName;
    }
    
    public String getLastName() {
        return lastName;
    }
    
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
    
    public BLaboralInformation getLaboralInformation() {
        return laboralInformation;
    }
    
    public void setLaboralInformation(BLaboralInformation laboralInformation) {
        this.laboralInformation = laboralInformation;
    }
}