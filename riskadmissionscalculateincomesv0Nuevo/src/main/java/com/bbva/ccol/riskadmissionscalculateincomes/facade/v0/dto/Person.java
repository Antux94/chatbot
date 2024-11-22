
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class Person {
    
    private IdentityDocument identityDocument;
    private String firstName;
    private String middleName;
    private String lastName;
    private LaboralInformation laboralInformation;
    
    public IdentityDocument getIdentityDocument() {
        return identityDocument;
    }
    
    public void setIdentityDocument(IdentityDocument identityDocument) {
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
    
    public LaboralInformation getLaboralInformation() {
        return laboralInformation;
    }
    
    public void setLaboralInformation(LaboralInformation laboralInformation) {
        this.laboralInformation = laboralInformation;
    }
}