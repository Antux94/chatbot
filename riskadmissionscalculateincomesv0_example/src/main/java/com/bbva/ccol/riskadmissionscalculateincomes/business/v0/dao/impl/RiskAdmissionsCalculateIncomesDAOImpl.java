//package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.impl;
//
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.IRiskAdmissionsCalculateIncomesDAO;
//
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.TransaccionCmlct001;
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.RequestTransactionCmlct001_1;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.ResponseTransactionCmlct001_1;
//
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper.ICalculateV0MapperTx;
//import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.*;
//import org.springframework.stereotype.Component;
//
//import javax.annotation.Resource;
//
//@Component(value = "riskAdmissionsCalculateIncomesDAOImpl")
//public class RiskAdmissionsCalculateIncomesDAOImpl implements IRiskAdmissionsCalculateIncomesDAO {
//    //@Resource(name = "transaccionCmlct001")
//    //private TransaccionCmlct001 transaccionCmlct001;
//
//    @Resource(name = "calculateV0MapperTx")
//    private ICalculateV0MapperTx calculateV0MapperTx;
//
//    @Override
//    public void createData(BBody source) {
//        RequestTransactionCmlct001_1 request = calculateV0MapperTx.INSTANCE.toTargetDTO(source);
//        //ResponseTransactionCmlct001_1 cmlct001 = transaccionCmlct001.invocar(request);
//        //return calculateV0MapperTx.mapOutData(cmlct001);
//        //return null;
//    }
//}



//import org.springframework.web.bind.annotation.*;
//
//@RestController
//@RequestMapping("/api")
//public class MyController {
//
//    @PostMapping("/convert")
//    public TargetDTO convert(@RequestBody SourceDTO source) {
//        // Aquí es donde haces la llamada al método de mapeo
//        return MyMapper.INSTANCE.toTargetDTO(source);
//    }
//}
