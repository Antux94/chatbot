
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto;

import java.util.List;

public class BBody {
    
    private BPerson person;
    private List<BInformationSources> informationSources;
    private BProduct product;
    
    public BPerson getPerson() {
        return person;
    }
    
    public void setPerson(BPerson person) {
        this.person = person;
    }
    
    public List<BInformationSources> getInformationSources() {
        return informationSources;
    }
    
    public void setInformationSources(List<BInformationSources> informationSources) {
        this.informationSources = informationSources;
    }
    
    public BProduct getProduct() {
        return product;
    }
    
    public void setProduct(BProduct product) {
        this.product = product;
    }
}