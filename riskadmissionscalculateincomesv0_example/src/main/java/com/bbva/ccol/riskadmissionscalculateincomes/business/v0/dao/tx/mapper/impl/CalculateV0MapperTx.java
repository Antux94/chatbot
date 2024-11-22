//package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper.impl;
//
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.IdentityDocument;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.InformationSources;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.LaboralInformation;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.Person;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.Product;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.RequestTransactionCmlct001_1;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.Employers;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.Incomes;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.ResponseTransactionCmlct001_1;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper.ICalculateV0MapperTx;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BCalculate;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BData;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BDeduction;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BEconomicActivity;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BEmployerInfo;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BEmployers;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BEmploymentHistory;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BEmploymentSituation;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIdentifierTimeEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIdentityDocument;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIdentityDocumentTypeEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIncomeAmount;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIncomes;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIncomesFrecuencyEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BIncomesIdEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BInformationSources;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BInformationSourcesIdEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BLaboralInformation;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BParticipantInformation;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BPeriod;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BPeriodIdEnum;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BPerson;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BSeniority;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BTotalDeductions;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BTotalIncomes;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BTstatus;
//import org.springframework.stereotype.Service;
//
//import java.util.ArrayList;
//import java.util.List;
//
//@Service(value = "calculateV0MapperTx")
//public class CalculateV0MapperTx implements ICalculateV0MapperTx {
//    @Override
//    public RequestTransactionCmlct001_1 mapInApxData(BCalculate bCalculate) {
//        RequestTransactionCmlct001_1 request = new RequestTransactionCmlct001_1();
//
//        if(bCalculate != null){
//            if(bCalculate.getPerson() != null){
//                request.setPerson(new Person());
//                IdentityDocument txIdentityDocument = new IdentityDocument();
//                txIdentityDocument.setDocumentType(bCalculate.getPerson().getIdentityDocument().getDocumentType().getId());
//                txIdentityDocument.setDocumentNumber(bCalculate.getPerson().getIdentityDocument().getDocumentNumber());
//                request.getPerson().setIdentityDocument(txIdentityDocument);
//                request.getPerson().setFirstName(bCalculate.getPerson().getFirstName());
//                request.getPerson().setMiddleName(bCalculate.getPerson().getMiddleName());
//                request.getPerson().setLastName(bCalculate.getPerson().getLastName());
//
//                if(bCalculate.getPerson().getLaboralInformation() != null){
//                    LaboralInformation laboralInformation = new LaboralInformation();
//                    laboralInformation.setCompanyId(bCalculate.getPerson().getLaboralInformation().getCompanyId());
//                    laboralInformation.setDeclaratedIncome(bCalculate.getPerson().getLaboralInformation().getDeclaratedIncome());
//                    request.getPerson().setLaboralInformation(laboralInformation);
//                }
//            }
//
//            mapInApxData2(bCalculate,request);
//
//        }
//        return request;
//    }
//
//    private void mapInApxData2(BCalculate bCalculate, RequestTransactionCmlct001_1 request){
//        if(bCalculate.getInformationSources() != null){
//            request.setInformationSources(new ArrayList<>());
//            for(BInformationSources data : bCalculate.getInformationSources()){
//                InformationSources txInformationSourcesClass = new InformationSources();
//                String information = String.valueOf(BInformationSourcesIdEnum.valueOf(data.getId().getId()));
//                txInformationSourcesClass.setId(information);
//
//                boolean isConsultedBoolean = false;
//
//                if (data.getIsConsulted() != null) {
//                    isConsultedBoolean = data.getIsConsulted();
//                }
//
//                String isConsulted = Boolean.toString(isConsultedBoolean);
//
//                txInformationSourcesClass.setIsConsulted(isConsulted);
//                request.getInformationSources().add(txInformationSourcesClass);
//            }
//        }
//
//        if(bCalculate.getProduct() != null){
//            request.setProduct(new Product());
//            request.getProduct().setId(bCalculate.getProduct().getId());
//            request.getProduct().setName(bCalculate.getProduct().getName());
//        }
//    }
//
//    @Override
//    public BData mapOutData(ResponseTransactionCmlct001_1 transaccionCmlct001) {
//        BData bData = new BData();
//        bData.setAppId(transaccionCmlct001.getAppId());
//        if(transaccionCmlct001.getData() != null){
//            bData.setPerson(new BPerson());
//            if(transaccionCmlct001.getData().getPerson() != null) {
//                bData.getPerson().setFirstName(transaccionCmlct001.getData().getPerson().getFirstName());
//                bData.getPerson().setMiddleName(transaccionCmlct001.getData().getPerson().getMiddleName());
//                bData.getPerson().setLastName(transaccionCmlct001.getData().getPerson().getLastName());
//                bData.getPerson().setIdentityDocument(new BIdentityDocument());
//                bData.getPerson().getIdentityDocument().setDocumentType(BIdentityDocumentTypeEnum.valueOf(transaccionCmlct001.getData().getPerson().getIdentityDocument().getDocumentType()));
//                bData.getPerson().getIdentityDocument().setDocumentNumber(transaccionCmlct001.getData().getPerson().getIdentityDocument().getDocumentNumber());
//
//                if(transaccionCmlct001.getData().getPerson().getLaboralInformation() != null){
//                    bData.getPerson().setLaboralInformation(new BLaboralInformation());
//                    bData.getPerson().getLaboralInformation().setCompanyId(transaccionCmlct001.getData().getPerson().getLaboralInformation().getCompanyId());
//                    bData.getPerson().getLaboralInformation().setDeclaratedIncome(transaccionCmlct001.getData().getPerson().getLaboralInformation().getDeclaratedIncome());
//                }
//            }
//            mapOutData2(transaccionCmlct001, bData);
//        }
//        return bData;
//    }
//
//    private void mapOutData2(ResponseTransactionCmlct001_1 transaccionCmlct001, BData bData){
//        if(transaccionCmlct001.getData().getInformationSources() != null){
//            bData.setInformationSources(this.getInformationSources(transaccionCmlct001.getData().getInformationSources()));
//        }
//
//        if(transaccionCmlct001.getData().getTotalIncomes() != null ){
//            bData.setTotalIncomes(new BTotalIncomes());
//            bData.getTotalIncomes().setAmount(transaccionCmlct001.getData().getTotalIncomes().getAmount());
//            bData.getTotalIncomes().setCurrency(transaccionCmlct001.getData().getTotalIncomes().getCurrency());
//        }
//
//        if(transaccionCmlct001.getData().getTotalDeductions() != null){
//            bData.setTotalDeductions(new BTotalDeductions());
//            bData.getTotalDeductions().setAmount(transaccionCmlct001.getData().getTotalDeductions().getAmount());
//            bData.getTotalDeductions().setCurrency(transaccionCmlct001.getData().getTotalDeductions().getCurrency());
//        }
//        if(transaccionCmlct001.getData().getEmployers() != null){
//            bData.setEmployers(this.getBEmployers(transaccionCmlct001.getData().getEmployers()));
//        }
//
//        if(transaccionCmlct001.getData().getEmploymentHistory() != null){
//            bData.setEmploymentHistory(new BEmploymentHistory());
//            bData.getEmploymentHistory().setId(BIdentifierTimeEnum.valueOf(transaccionCmlct001.getData().getEmploymentHistory().getId()));
//            bData.getEmploymentHistory().setTimeContinuity(transaccionCmlct001.getData().getEmploymentHistory().getTimeContinuity());
//            bData.getEmploymentHistory().setDateContinuity(transaccionCmlct001.getData().getEmploymentHistory().getDateContinuity());
//        }
//
//        if(transaccionCmlct001.getData().getStatus() != null){
//            bData.setStatus(new BTstatus());
//            bData.getStatus().setId(transaccionCmlct001.getData().getStatus().getId());
//            bData.getStatus().setDescription(transaccionCmlct001.getData().getStatus().getDescription());
//        }
//    }
//
//    private  List<BInformationSources> getInformationSources(List<com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.InformationSources> informationSources){
//        ArrayList<BInformationSources> listInformationSources = new ArrayList<>();
//        for(com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.InformationSources data : informationSources){
//            BInformationSources informationSourcesClass = new BInformationSources();
//            informationSourcesClass.setId(BInformationSourcesIdEnum.valueOf(data.getId()));
//            informationSourcesClass.setIsConsulted(data.getIsConsulted());
//            listInformationSources.add(informationSourcesClass);
//        }
//        return listInformationSources;
//    }
//
//    private ArrayList<BEmployers> getBEmployers(List<Employers> employers){
//        ArrayList<BEmployers> listBEmployers = new ArrayList<>();
//        for(Employers data : employers){
//         BEmployers bEmployersClass = new BEmployers();
//            bEmployersClass.setEmployerInfo(new BEmployerInfo());
//            bEmployersClass.getEmployerInfo().setCompanyName(data.getEmployerInfo().getCompanyName());
//            bEmployersClass.getEmployerInfo().setIdentityDocument(new BIdentityDocument());
//            bEmployersClass.getEmployerInfo().getIdentityDocument().setDocumentType(BIdentityDocumentTypeEnum.valueOf(data.getEmployerInfo().getIdentityDocument().getDocumentType()));
//            bEmployersClass.getEmployerInfo().getIdentityDocument().setDocumentNumber(data.getEmployerInfo().getIdentityDocument().getDocumentNumber());
//
//            bEmployersClass.getEmployerInfo().setEconomicActivity(new BEconomicActivity());
//            bEmployersClass.getEmployerInfo().getEconomicActivity().setId(data.getEmployerInfo().getEconomicActivity().getId());
//            bEmployersClass.getEmployerInfo().getEconomicActivity().setName(data.getEmployerInfo().getEconomicActivity().getName());
//            bEmployersClass.getEmployerInfo().getEconomicActivity().setInternationalClassification(data.getEmployerInfo().getEconomicActivity().getInternationalClassification());
//
//            bEmployersClass.setParticipantInformation(new BParticipantInformation());
//            bEmployersClass.getParticipantInformation().setSeniority(new BSeniority());
//            bEmployersClass.getParticipantInformation().getSeniority().setNumber(data.getParticipantInformation().getSeniority().getNumber());
//            bEmployersClass.getParticipantInformation().getSeniority().setPeriod(new BPeriod());
//            bEmployersClass.getParticipantInformation().getSeniority().getPeriod().setId(BPeriodIdEnum.valueOf(data.getParticipantInformation().getSeniority().getPeriod().getId()));
//            bEmployersClass.getParticipantInformation().getSeniority().getPeriod().setName(data.getParticipantInformation().getSeniority().getPeriod().getName());
//
//            bEmployersClass.getParticipantInformation().setIncomes(this.getBIncomes(data.getParticipantInformation().getIncomes()));
//
//            bEmployersClass.getParticipantInformation().setDeduction(new BDeduction());
//            bEmployersClass.getParticipantInformation().getDeduction().setAmount(data.getParticipantInformation().getDeduction().getAmount());
//            bEmployersClass.getParticipantInformation().getDeduction().setCurrency(data.getParticipantInformation().getDeduction().getCurrency());
//
//            bEmployersClass.getParticipantInformation().setEmploymentSituation(new BEmploymentSituation());
//            bEmployersClass.getParticipantInformation().getEmploymentSituation().setId(data.getParticipantInformation().getEmploymentSituation().getId());
//            bEmployersClass.getParticipantInformation().getEmploymentSituation().setName(data.getParticipantInformation().getEmploymentSituation().getName());
//
//            bEmployersClass.getParticipantInformation().setDateRelationship(data.getParticipantInformation().getDateRelationship());
//            listBEmployers.add(bEmployersClass);
//        }
//        return listBEmployers;
//    }
//
//    private ArrayList<BIncomes> getBIncomes(List<Incomes> incomes){
//        ArrayList<BIncomes> listBIncomes = new ArrayList<>();
//        for(Incomes data : incomes){
//            BIncomes bIncomesClass = new BIncomes();
//            bIncomesClass.setId(BIncomesIdEnum.valueOf(data.getId()));
//            bIncomesClass.setName(data.getName());
//            bIncomesClass.setIncomeAmount(new BIncomeAmount());
//            bIncomesClass.getIncomeAmount().setAmount(data.getIncomeAmount().getAmount());
//            bIncomesClass.getIncomeAmount().setCurrency(data.getIncomeAmount().getCurrency());
//            bIncomesClass.setFrecuency(BIncomesFrecuencyEnum.valueOf(data.getFrecuency()));
//            listBIncomes.add(bIncomesClass);
//        }
//
//        return listBIncomes;
//    }
//}
