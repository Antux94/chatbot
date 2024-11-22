
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper;

import org.mapstruct.Mapper;

import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.RequestTransactionCmlct001_1;
import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BBody;

@Mapper(componentModel = "spring")
public interface ICalculateV0MapperTx 
{            
    RequestTransactionCmlct001_1 mapInApxData(BBody dtoInt);
}