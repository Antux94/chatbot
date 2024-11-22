//package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.impl;
//
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.IBSrvRiskAdmissionsCalculateIncomesv0;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BCalculate;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BData;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.ISrvRiskAdmissionsCalculateIncomesv0;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.Calculate;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.Data;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.ServiceResponseAcceptedNoBody;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.ICalculateMapper;
//import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper.IDataMapper;
//import com.bbva.jee.arq.spring.core.catalog.gabi.*;
//import com.bbva.jee.arq.spring.core.managers.OutputHeaderManager;
//import com.bbva.jee.arq.spring.core.servicing.annotations.SMC;
//import com.bbva.jee.arq.spring.core.servicing.annotations.SN;
//import com.bbva.jee.arq.spring.core.servicing.annotations.VN;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.stereotype.Service;
//import javax.annotation.Resource;
//import javax.ws.rs.*;
//import javax.ws.rs.core.MediaType;
//
//
//@Path("/v0")
//@SN(registryID = "SNCO1810037", logicalID = "risk-admissions")
//@VN(vnn = "v0")
//@Consumes({MediaType.APPLICATION_JSON})
//@Produces({MediaType.APPLICATION_JSON})
//@Service(value = "srvRiskAdmissionsCalculateIncomesv0")
//public class SrvRiskAdmissionsCalculateIncomesv0 implements ISrvRiskAdmissionsCalculateIncomesv0 {
//    @Resource(name = "bSrvRiskAdmissionsCalculateIncomesv0")
//    private IBSrvRiskAdmissionsCalculateIncomesv0 bSrvRiskAdmissionsCalculateIncomesv0;
//
//    @Resource(name="calculateMapper")
//    private ICalculateMapper calculateMapper;
//
//    @Resource(name="dataMapper")
//    private IDataMapper dataMapper;
//
//    @Autowired
//    private OutputHeaderManager outputHeaderManager;
//
//    /**
//     * Fecha: 18/05/2022
//     * Version: 0.30.0
//     * Autor: Meraki Software Technologies SAS
//     * Proyecto:
//     **/
//
//    @Override
//    @POST
//    @Path("/calculate-incomes")
//    @SMC(registryID = "SMGG20220523", logicalID = "postIdentificationDataPerson", forcedCatalog = "gabiCatalog")
//    public ServiceResponseInterface postIdentificationDataPerson(Calculate calculate) {
//
//
//        BCalculate bCalculate = calculateMapper.mapInCalculate(calculate);
//        BData bData = bSrvRiskAdmissionsCalculateIncomesv0.postCalculateIncomes(bCalculate);
//        if(bData.getPerson() != null){
//            Data data = dataMapper.mapOutData(bData);
//            return ServiceResponseOK.data(data).build();
//        }else{
//            String location = String.valueOf(bData.getAppId());
//            outputHeaderManager.setLocationHeader(location);
//
//            return ServiceResponseAcceptedNoBody.ServiceResponseAcceptedNoBodyBuilder.build();
//        }
//    }
//
//}
