//package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.impl;
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.*;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.Calculate;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.InformationSources;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.ICalculateMapper;
//import org.springframework.stereotype.Service;
//
//import java.util.ArrayList;
//
//@Service(value = "calculateMapper")
//public class CalculateMapper implements ICalculateMapper {
//
//    @Override
//    public BCalculate mapInCalculate(Calculate calculate) {
//        BCalculate response = new BCalculate();
//        if(calculate.getPerson() != null){
//            BPerson bPerson = new BPerson();
//            bPerson.setFirstName(calculate.getPerson().getFirstName());
//            bPerson.setMiddleName(calculate.getPerson().getMiddleName());
//            bPerson.setLastName(calculate.getPerson().getLastName());
//            response.setPerson(bPerson);
//
//            BIdentityDocument bIdentityDocument = new BIdentityDocument();
//            bIdentityDocument.setDocumentType(BIdentityDocumentTypeEnum.valueOf(calculate.getPerson().getIdentityDocument().getDocumentType().getId()));
//            bIdentityDocument.setDocumentNumber(calculate.getPerson().getIdentityDocument().getDocumentNumber());
//            response.getPerson().setIdentityDocument(bIdentityDocument);
//
//            if(calculate.getPerson().getLaboralInformation() != null){
//                BLaboralInformation bLaboralInformation = new BLaboralInformation();
//                bLaboralInformation.setCompanyId(calculate.getPerson().getLaboralInformation().getCompanyId());
//                bLaboralInformation.setDeclaratedIncome(calculate.getPerson().getLaboralInformation().getDeclaratedIncome());
//                response.getPerson().setLaboralInformation(bLaboralInformation);
//            }
//        }
//        if(calculate.getInformationSources() != null){
//            response.setInformationSources(new ArrayList<>());
//            for(InformationSources data : calculate.getInformationSources()){
//                BInformationSources informationSourcesClass = new BInformationSources();
//                informationSourcesClass.setId(BInformationSourcesIdEnum.valueOf(data.getId().getId()));
//                informationSourcesClass.setIsConsulted(data.getIsConsulted());
//                response.getInformationSources().add(informationSourcesClass);
//            }
//        }
//        if(calculate.getProduct() != null){
//           BProduct bProduct = new BProduct();
//           bProduct.setId(calculate.getProduct().getId());
//           bProduct.setName(calculate.getProduct().getName());
//           response.setProduct(bProduct);
//        }
//        return response;
//    }
//}
