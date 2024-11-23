
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class LaboralInformation {
    
    private String companyId;
    private Integer declaratedIncome;
    
    public LaboralInformation() {
    }
    
    public LaboralInformation(String companyId, Integer declaratedIncome) {
        this.companyId = companyId;
        this.declaratedIncome = declaratedIncome;
    }
    
    public String getCompanyId() {
        return companyId;
    }
    
    public void setCompanyId(String companyId) {
        this.companyId = companyId;
    }
    
    public Integer getDeclaratedIncome() {
        return declaratedIncome;
    }
    
    public void setDeclaratedIncome(Integer declaratedIncome) {
        this.declaratedIncome = declaratedIncome;
    }
}
