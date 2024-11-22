
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BProduct {
    
    private String id;
    private String name;
    
    public BProduct() {
    }
    
    public BProduct(String id, String name) {
        this.id = id;
        this.name = name;
    }
    
    public String getId() {
        return this.id;
    }
    
    public BProduct setId(String id) {
        this.id = id;
        return this;
    }
    
    public String getName() {
        return this.name;
    }
    
    public BProduct setName(String name) {
        this.name = name;
        return this;
    }
}