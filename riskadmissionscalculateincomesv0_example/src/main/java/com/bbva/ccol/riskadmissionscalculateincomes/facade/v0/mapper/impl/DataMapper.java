//package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.impl;
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.*;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.*;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.IDataMapper;
//import org.springframework.stereotype.Service;
//
//import java.util.ArrayList;
//import java.util.List;
//
//@Service(value = "dataMapper")
//public class DataMapper implements IDataMapper {
//
//    @Override
//    public Data mapOutData(BData bData) {
//        Data response = new Data();
//        if(bData.getPerson() != null){
//            response.setPerson(new Person());
//            response.getPerson().setFirstName(bData.getPerson().getFirstName());
//            response.getPerson().setMiddleName(bData.getPerson().getMiddleName());
//            response.getPerson().setLastName(bData.getPerson().getLastName());
//
//            response.getPerson().setIdentityDocument(new IdentityDocument());
//            String documentType = bData.getPerson().getIdentityDocument().getDocumentType().getId();
//            IdentityDocumentTypeEnum identityDocumentTypeEnum = IdentityDocumentTypeEnum.valueOf(documentType);
//            response.getPerson().getIdentityDocument().setDocumentType(identityDocumentTypeEnum);
//            response.getPerson().getIdentityDocument().setDocumentNumber(bData.getPerson().getIdentityDocument().getDocumentNumber());
//
//            if(bData.getPerson().getLaboralInformation() != null){
//                LaboralInformation laboralInformation = new LaboralInformation();
//                laboralInformation.setCompanyId(bData.getPerson().getLaboralInformation().getCompanyId());
//                laboralInformation.setDeclaratedIncome(bData.getPerson().getLaboralInformation().getDeclaratedIncome());
//                response.getPerson().setLaboralInformation(laboralInformation);
//            }
//        }
//        if(bData.getInformationSources() != null){
//            response.setInformationSources(this.getInformationSourcesData(bData.getInformationSources()));
//        }
//        if(bData.getTotalIncomes() != null){
//            response.setTotalIncomes(new TotalIncomes());
//            response.getTotalIncomes().setAmount(bData.getTotalIncomes().getAmount());
//            response.getTotalIncomes().setCurrency(bData.getTotalIncomes().getCurrency());
//        }
//        if(bData.getTotalDeductions() != null){
//            response.setTotalDeductions(new TotalDeductions());
//            response.getTotalDeductions().setAmount(bData.getTotalDeductions().getAmount());
//            response.getTotalDeductions().setCurrency(bData.getTotalDeductions().getCurrency());
//        }
//        if(bData.getEmployers() != null){
//            response.setEmployers(new ArrayList<>());
//            for(BEmployers employersData : bData.getEmployers()) {
//                Employers employers = new Employers();
//                if (employersData.getEmployerInfo() != null) {
//                    EmployerInfo employerInfo = new EmployerInfo();
//                    employerInfo.setCompanyName(employersData.getEmployerInfo().getCompanyName());
//
//                    IdentityDocument identityDocument = new IdentityDocument();
//                    identityDocument.setDocumentType(IdentityDocumentTypeEnum.valueOf(employersData.getEmployerInfo().getIdentityDocument().getDocumentType().getId()));
//                    identityDocument.setDocumentNumber(employersData.getEmployerInfo().getIdentityDocument().getDocumentNumber());
//                    employerInfo.setIdentityDocument(identityDocument);
//
//                    EconomicActivity economicActivity = new EconomicActivity();
//                    economicActivity.setId(employersData.getEmployerInfo().getEconomicActivity().getId());
//                    economicActivity.setName(employersData.getEmployerInfo().getEconomicActivity().getName());
//                    economicActivity.setInternationalClassification(employersData.getEmployerInfo().getEconomicActivity().getInternationalClassification());
//                    employerInfo.setEconomicActivity(economicActivity);
//                    employers.setEmployerInfo(employerInfo);
//                }
//                if (employersData.getParticipantInformation() != null) {
//                    ParticipantInformation participantInformation = new ParticipantInformation();
//
//                    Seniority seniority = new Seniority();
//                    seniority.setNumber(employersData.getParticipantInformation().getSeniority().getNumber());
//                    seniority.setPeriod(new Period());
//                    seniority.getPeriod().setId(PeriodIdEnum.valueOf(employersData.getParticipantInformation().getSeniority().getPeriod().getId().getId()));
//                    seniority.getPeriod().setName(employersData.getParticipantInformation().getSeniority().getPeriod().getName());
//                    participantInformation.setSeniority(seniority);
//
//                    participantInformation.setIncomes(this.getIncomesData(employersData.getParticipantInformation().getIncomes()));
//
//                    Deduction deduction = new Deduction();
//                    deduction.setAmount(employersData.getParticipantInformation().getDeduction().getAmount());
//                    deduction.setCurrency(employersData.getParticipantInformation().getDeduction().getCurrency());
//                    participantInformation.setDeduction(deduction);
//
//                    EmploymentSituation employmentSituation = new EmploymentSituation();
//                    employmentSituation.setId(employersData.getParticipantInformation().getEmploymentSituation().getId());
//                    employmentSituation.setName(employersData.getParticipantInformation().getEmploymentSituation().getName());
//                    participantInformation.setEmploymentSituation(employmentSituation);
//
//                    participantInformation.setDateRelationship(employersData.getParticipantInformation().getDateRelationship());
//                    employers.setParticipantInformation(participantInformation);
//                }
//                response.getEmployers().add(employers);
//            }
//        }
//        if(bData.getEmploymentHistory() != null){
//            response.setEmploymentHistory(new EmploymentHistory());
//            response.getEmploymentHistory().setId(IdentifierTimeEnum.valueOf(bData.getEmploymentHistory().getId().getId()));
//            response.getEmploymentHistory().setTimeContinuity(bData.getEmploymentHistory().getTimeContinuity());
//            response.getEmploymentHistory().setDateContinuity(bData.getEmploymentHistory().getDateContinuity());
//        }
//
//        if(bData.getStatus() != null){
//            response.setStatus(new Status());
//            response.getStatus().setId(bData.getStatus().getId());
//            response.getStatus().setDescription(bData.getStatus().getDescription());
//        }
//
//        return response;
//    }
//
//    private ArrayList<Incomes> getIncomesData(List<BIncomes> bIncomes){
//        ArrayList<Incomes> listIncomes = new ArrayList<>();
//        for (BIncomes incomesData : bIncomes) {
//            Incomes incomes = new Incomes();
//            incomes.setId(IncomesIdEnum.valueOf(incomesData.getId().getId()));
//            incomes.setName(incomesData.getName());
//            IncomeAmount incomeAmount = new IncomeAmount();
//            incomeAmount.setAmount(incomesData.getIncomeAmount().getAmount());
//            incomeAmount.setCurrency(incomesData.getIncomeAmount().getCurrency());
//            incomes.setIncomeAmount(incomeAmount);
//            incomes.setFrecuency(IncomesFrecuencyEnum.valueOf(incomesData.getFrecuency().getId()));
//            listIncomes.add(incomes);
//        }
//        return listIncomes;
//    }
//
//    private ArrayList<InformationSources> getInformationSourcesData(List<BInformationSources> bInformationSources){
//        ArrayList<InformationSources> listInformationSources = new ArrayList<>();
//        for(BInformationSources data : bInformationSources){
//            InformationSources informationSourcesClass = new InformationSources();
//            informationSourcesClass.setId(InformationSourcesIdEnum.valueOf(data.getId().getId()));
//            informationSourcesClass.setIsConsulted(data.getIsConsulted());
//            listInformationSources.add(informationSourcesClass);
//        }
//        return listInformationSources;
//    }
//}
