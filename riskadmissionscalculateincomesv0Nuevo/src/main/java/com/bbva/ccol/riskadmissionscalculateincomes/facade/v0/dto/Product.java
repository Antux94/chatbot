
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class Product {
    
    private String id;
    private String name;
    
    public Product() {
    }
    
    public Product(String id, String name) {
        this.id = id;
        this.name = name;
    }
    
    public String getId() {
        return this.id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    public Product id(String id) {
        this.id = id;
        return this;
    }
    
    public String getName() {
        return this.name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public Product name(String name) {
        this.name = name;
        return this;
    }
}