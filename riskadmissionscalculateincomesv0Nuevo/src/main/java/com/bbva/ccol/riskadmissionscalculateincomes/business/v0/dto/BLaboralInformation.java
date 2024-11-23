
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BLaboralInformation {
    private String companyId;
    private Integer declaratedIncome;
    
    public BLaboralInformation() {
    }
    
    public BLaboralInformation(String companyId, Integer declaratedIncome) {
        this.companyId = companyId;
        this.declaratedIncome = declaratedIncome;
    }
    
    public String getCompanyId() {
        return this.companyId;
    }
    
    public void setCompanyId(String companyId) {
        this.companyId = companyId;
    }
    
    public Integer getDeclaratedIncome() {
        return this.declaratedIncome;
    }
    
    public void setDeclaratedIncome(Integer declaratedIncome) {
        this.declaratedIncome = declaratedIncome;
    }
}