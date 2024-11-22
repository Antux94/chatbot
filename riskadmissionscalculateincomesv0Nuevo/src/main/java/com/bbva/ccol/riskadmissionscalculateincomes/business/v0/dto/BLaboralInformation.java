
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BLaboralInformation {
    private String companyId;
    private Integer declaratedIncome;
    
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