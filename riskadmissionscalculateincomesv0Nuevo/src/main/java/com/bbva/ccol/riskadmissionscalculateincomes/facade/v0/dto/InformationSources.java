
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class InformationSources {
    
    private String id;
    private boolean isConsulted;
    
    public InformationSources() {
    }
    
    public InformationSources(String id, boolean isConsulted) {
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