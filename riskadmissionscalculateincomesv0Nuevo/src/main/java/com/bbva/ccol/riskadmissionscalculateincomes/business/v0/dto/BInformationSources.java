
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BInformationSources {
    private String id;
    private boolean isConsulted;
    
    public BInformationSources() {
    }
    
    public BInformationSources(String id, boolean isConsulted) {
        this.id = id;
        this.isConsulted = isConsulted;
    }
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    public boolean isConsulted() {
        return isConsulted;
    }
    
    public void setConsulted(boolean consulted) {
        isConsulted = consulted;
    }
}