//package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper;
//
//import com.bbva.jee.arq.spring.core.catalog.gabi.ServiceResponseNoBody;
//import org.springframework.http.HttpMethod;
//
//public class ServiceResponseAcceptedNoBody extends ServiceResponseNoBody {
//    private ServiceResponseAcceptedNoBody() {
//    }
//
//    public int getHttpStatus(HttpMethod httpMethod) {
//        return 202;
//    }
//
//    public static class ServiceResponseAcceptedNoBodyBuilder {
//        ServiceResponseAcceptedNoBodyBuilder() {
//            //Do nothing
//        }
//
//        public static ServiceResponseAcceptedNoBody build() {
//            return new ServiceResponseAcceptedNoBody();
//        }
//    }
//}