
package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper;

import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.Body;
import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BBody;

import org.mapstruct.Mapper;

@Mapper(componentModel = "spring")
public interface IPostRiskAdmissionsCalculateIncomesMapper {

    BBody mapInData(Body dto);

    Body mapOutData(BBody dtoInt);
}