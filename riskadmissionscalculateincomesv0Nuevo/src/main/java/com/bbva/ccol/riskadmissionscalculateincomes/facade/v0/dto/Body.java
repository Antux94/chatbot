
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto;

import java.util.List;

public class Body {
    
    private Person person;
    private List<InformationSources> informationSources;
    private Product product;
    
    public Person getPerson() {
        return person;
    }
    
    public void setPerson(Person person) {
        this.person = person;
    }
    
    public List<InformationSources> getInformationSources() {
        return informationSources;
    }
    
    public void setInformationSources(List<InformationSources> informationSources) {
        this.informationSources = informationSources;
    }
    
    public Product getProduct() {
        return product;
    }
    
    public void setProduct(Product product) {
        this.product = product;
    }
}