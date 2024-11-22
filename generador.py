import guardar
import langchain
import os
from langchain_core.prompts import PromptTemplate  # Actualizado a langchain_core.prompts
from langchain_openai import OpenAI


#langchain.llm_cache.clear()



llm = OpenAI(
    #TODO: AJUSTAR CLAVE DE API
    openai_api_key= os.getenv("OPENAI_API_KEY"),
    temperature=0.0,
    max_tokens=3000,
    model="gpt-3.5-turbo-instruct"  #TODO: Actualización del modelo
)

# noinspection SpellCheckingInspection
def generar_dtos(carpeta, nueva_carpeta, int_carpeta, form_carpeta, origen_archivo, ruta_completa, carpeta_tx, isFirstCall):
    # Instancia la clase OpenAI con la clave de la API

    # Definir plantillas de prompts
    #Coloca los imports de la clausula (uses:) al inicio.
    #Si hay un ENUM, agrega un comentario //ENUM: (valores), sobre el atributo.

    #TODO: Se debe tomar del api.raml.
    carpeta = "riskadmissionscalculateincomes"

    print("isFirstCall: ", isFirstCall)

    #TODO: Se debe cambiar el nombre body y tomarlo del api.raml




 #   if isFirstCall:
 #       nombre_padre = "If the name of the first object in the RAML is 'Body', so the class name should be: (RequestTransactionCmlct001_1)."
 #   else:
 #       nombre_padre = "The class name should be the name of the first object in the RAML with the first letter capitalized."
#

    prompts_dtos = {
        # TODO: this should be sent as parameters in a DB.
        # TODO: IMPORTANTE -- getters y setters siempre con getName y setName porque no se mapea en mapstructs.
        "dto": """
            Generate a Java DTO class from the following RAML specification: {input_raml}.
            - The class name should be the name of the first object in the RAML with the first letter capitalized.
            - For each attribute, use the elements within ("properties:") to construct the fields.
            - For each data type of the attribute, use the elements within ("type:") to construct the data types of fields exactly with te SAME data type.
            - Ensure that any array types are converted to Java List types.
            - Include setters and getters for all attributes. 
            - Add the package declaration at the beginning: (package com.bbva.ccol.{carpeta}.facade.v0.dto;).
            - Ensure the class is clean and can compile in Java.
            - Add next to package this imports: 
                -(import java.util.List;).
            - Verify that each data type of the fields is the SAME data type within ("type:") of the RAML.  
            - Adjust the indentation properly.
        """,
        "dtoInt": """
            Generate a Java DTO class from the following RAML specification: {input_raml}.
            - The class name should be the name of the first object in the RAML with the first letter capitalized.
            - For each attribute, use the elements within ("properties:") to construct the fields.
            - For each data type of the attribute, use the elements within ("type:") to construct the data types of fields exactly with te SAME data type.
            - Ensure that any array types are converted to Java List types.
            - Include setters and getters for all attributes.
            - Add the package declaration at the beginning: (package com.bbva.ccol.{carpeta}.business.v0.dto;).
            - Ensure the class is clean and can compile in Java.
            - Add next to package this imports: 
                -(import java.util.List;).
            - Prefix 'B' to the class. For example the class Person becomes BPerson.
            - Verify that each data type of the fields is the SAME data type within ("type:") of the RAML.  
            - Adjust the indentation properly.
        """,
        "dtoIntOLD2": """
            Generate a Java DTO class from the following RAML specification: {input_raml}.
            - The class name should be the name of the first object in the RAML with the first letter capitalized.
            - Prefix 'B' to the class. For example the class Person becomes BPerson.
            - For each attribute, use the elements within ("properties:") to construct the fields.
            - For each data type of the attribute, use the elements within ("type:") to construct the data types of fields exactly with te SAME data type.
            - Ensure that any array types are converted to Java List types.
            - Include setters and getters for all attributes.
            - Add the package declaration at the beginning: (package com.bbva.ccol.{carpeta}.business.v0.dto;).
            - Ensure the class is clean and can compile in Java.
            - Add next to package this imports: 
                -(import java.util.List;).
            - Adjust the indentation properly.
        """,
        "dtoIntOLD": """
            Generate a Java DTOInt class from the following RAML specification: {input_raml}.
            - The class name should be the name of the first object in the RAML with the first letter capitalized.
            - Prefix 'B' to the class and 'b' to the attribute names. For example, Person becomes BPerson, name becomes bName, etc.
            - Use the elements within ("properties":) to construct the fields.
            - Add the package declaration at the beginning: (package com.bbva.ccol.{carpeta}.business.v0.dto;).
            - Add the @NotNull annotation to fields where required = true.
            - Add next to package this imports: 
                -(import javax.validation.constraints.NotNull;).
                -(import java.util.List;).
            - Ensure the class is clean and can compile in Java.
            - Adjust the indentation properly.
        """,
        "dtoFormato": """
            Generate a Java DTO class from the following RAML specification: {input_raml}.
            - The class name should be the name of the first object in the RAML with the first letter capitalized.
            - Add the annotation @Campo(indice = [1,2,3...], nombre = "fieldName", tipo = TipoCampo.[ALFANUMERICO, ENTERO, DECIMAL, FECHA, VARCHAR, TABULAR, ATTACHMENTS, BOOLEAN, LIST, TIMESTAMP, DTO]) to each field. 
                - If the field is a String, set tipo as ALFANUMERICO.
                - If the field is an Integer, set tipo as ENTERO.
                - If the field is a List, set tipo as TABULAR.
                - For other types, use the model's discretion.
            - Include setters and getters for all attributes.
            - Add the package declaration at the beginning: (package com.bbva.ccol.{carpeta}.business.v0.dao.model.cmlct001_1.in;).
            - Add next to package this imports: 
                -(import com.bbva.jee.arq.spring.core.host.Campo;).
                -(import com.bbva.jee.arq.spring.core.host.FilaCampoTabular;).
                -(import com.bbva.jee.arq.spring.core.host.TipoCampo;).
                -(import java.util.List;).
            - Ensure the class is clean and can compile in Java.
            - Adjust the indentation properly.
            - Ensure that any array types are converted to Java List types.
        """
    }




    # Crear los prompt templates
    prompt_template2 = PromptTemplate(template=prompts_dtos["dto"], input_variables=["input_raml", "carpeta"])
    prompt_template3 = PromptTemplate(template=prompts_dtos["dtoInt"], input_variables=["input_raml", "carpeta"])
    prompt_template4 = PromptTemplate(template=prompts_dtos["dtoFormato"], input_variables=["input_raml", "carpeta"])
    #prompt_template5 = PromptTemplate(template=prompts["mapper"], input_variables=["dto1", "dto2"])

    # Leer el contenido del archivo RAML
    with open(ruta_completa, 'r') as archivo:
        contenido = archivo.read()

    # Generar DTOs
    message2 = prompt_template2.format(input_raml=contenido, carpeta=carpeta)
    message3 = prompt_template3.format(input_raml=contenido, carpeta=carpeta)
    message4 = prompt_template4.format(input_raml=contenido, carpeta=carpeta)

    dtos = llm.invoke(message2).replace("*/", "")
    dtos_int = llm.invoke(message3).replace("*/", "")
    #formats = llm.invoke(message4).replace("*/", "")



    def ajustar_indentacion(codigo):
        # Ajustar la indentación del código Java generado
        lineas = codigo.split('\n')
        indentado = []
        nivel_indentacion = 0
        for linea in lineas:
            linea = linea.strip()
            if linea.endswith('}') and nivel_indentacion > 0:
                nivel_indentacion -= 1
            indentado.append('    ' * nivel_indentacion + linea)
            if linea.endswith('{'):
                nivel_indentacion += 1
        return '\n'.join(indentado)

    # Ajustar la indentación de los DTOs y formatos generados
    dtos = ajustar_indentacion(dtos)
    dtos_int = ajustar_indentacion(dtos_int)
    #formats = ajustar_indentacion(formats)

    # Generar el mapper
    #message5 = prompt_template5.format(dto1=dtos, dto2=dtos_int)
    #mapper = llm.invoke(message5)

    # Guardar los resultados en los archivos correspondientes
    guardar.guardar_dtos(carpeta, nueva_carpeta, origen_archivo, dtos)
    guardar.guardar_dtos(carpeta, int_carpeta, origen_archivo, dtos_int)

    #guardar.guardar_dtos(carpeta, form_carpeta, origen_archivo, formats)
    #guardarJsonSchema.guardar_json_schema(carpeta, form_carpeta, origen_archivo, mapper)






def generar_interfaces(carpeta, nueva_carpeta, int_carpeta, form_carpeta, origen_archivo, ruta_completa, mainDto):


    # Definir plantillas de prompts
    prompts_mappers = {
        "firma_interface": """
            Genera una clase de tipo interface en java con la firma del método para mapear los siguientes DTOs: {dto_externo} al {dto_interno}.
            Usa como guia la siguiente estructura: {estructura_interface}.
            Limpia la clase para que pueda compilar en java.
            Ajusta la identacion.
        """,
        "estructura_interface": """
            package com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.mapper;
            
            import com.bbva.ccol.riskadmissionscalculateincomes.facade.v0.dto.Body;
            import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BBody;
            
            import org.mapstruct.Mapper;
            
            @Mapper(componentModel = "spring")
            public interface IPostRiskAdmissionsCalculateIncomesMapper
            {
                {dto_interno} mapInData({dto_externo} dto);
                {dto_externo} mapOutData({dto_interno} dtoInt);
            }
        """
    }

    # Definir plantillas de prompts
    prompts_mappers_trx = {
        "firma_interface": """
            Genera una clase de tipo interface en java con la firma del método para mapear los siguientes DTOs: {dto_interno} al {dto_formato_apx}.
            Usa como guia la siguiente estructura: {estructura_interface}, reemplaza los valores de dto_formato_apx y dto_interno.
            Limpia la clase para que pueda compilar en java.
            Ajusta la identacion.
        """,
        "estructura_interface": """
            package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper;
            
            
            import org.mapstruct.Mapper;
            
            import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.in.RequestTransactionCmlct001_1;
            import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BBody;
            
            @Mapper(componentModel = "spring")
            public interface ICalculateV0MapperTx 
            {            
                {dto_formato_apx} mapInApxData({dto_interno} dtoInt);
            }

        """
    }

    # Crear los prompt templates
    prompt_template= PromptTemplate(template=prompts_mappers["firma_interface"], input_variables=["dto_externo", "dto_interno", "estructura_interface"])
    prompt_template_trx= PromptTemplate(template=prompts_mappers_trx["firma_interface"], input_variables=["dto_interno", "dto_formato_apx", "estructura_interface"])


    # lectura de dtos en arbol para generar mapper completo
    #contenido_dto = ruta_completa.split('\\')

    contenido_dto = mainDto
    contenido_dto = contenido_dto[0].upper() + contenido_dto[1:]

    contenido_dto_int = "B" + contenido_dto
    contenido_dto_trx = "RequestTransactionCmlct001_1" #TODO: CAMBIAR

    #TODO: CAMBIAR
    #ruta_dto = "C:/Users/SURAMERICANA/PycharmProjects/asoAsistantv2/ccol_calculate-incomes/facade/v0/dto/InformationSources.java"
    #with open(ruta_dto, 'r') as archivo:
    #    contenido_dto = archivo.read()
#
    ##TODO: CAMBIAR
    #ruta_dto_int = "C:/Users/SURAMERICANA/PycharmProjects/asoAsistantv2/ccol_calculate-incomes/business/v0/dto/InformationSources.java"
    #with open(ruta_dto_int, 'r') as archivo:
    #    contenido_dto_int = archivo.read()

    # Generar Mapper
    message = prompt_template.format(dto_externo=contenido_dto, dto_interno=contenido_dto_int, estructura_interface=prompts_mappers["estructura_interface"])
    message_trx = prompt_template_trx.format(dto_interno=contenido_dto_int, dto_formato_apx=contenido_dto_trx, estructura_interface=prompts_mappers_trx["estructura_interface"])



    interface = llm.invoke(message)
    interface_trx = llm.invoke(message_trx)



    # Guardar los resultados en los archivos correspondientes
    guardar.guardar_interface(carpeta, nueva_carpeta, origen_archivo, interface, True, False)
    guardar.guardar_interface(carpeta, nueva_carpeta, origen_archivo, interface_trx, False, False)


def generar_interfaces_out_trx(carpeta, nueva_carpeta, origen_archivo):

    #TODO: CAMBIAR
    rutaDto = "riskadmissionscalculateincomesv0Nuevo/src/main/java/com/bbva/ccol/riskadmissionscalculateincomes/facade/v0/dto/Body.java"

    mappings_var = ""

    with open(rutaDto, "r") as archivo:
        contenido = archivo.readlines()


    lineas_private = [linea for linea in contenido if "private" in linea]

    for linea in lineas_private:
        print("lineas_private: " + linea)
        nombre_campo = linea.strip().split(" ")[-1].replace(";","")
        mapping = f"@Mapping(source = \"data.{nombre_campo}\", target = \"{nombre_campo}\"),\n"
        mappings_var = mappings_var + mapping
        print("mappings_var: " + mappings_var)

    # Definir plantillas de prompts
    interface_concatenated = f"""  
package com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.tx.mapper;


import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.Mappings;

import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dao.model.cmlct001_1.out.ResponseTransactionCmlct001_1;
import com.bbva.ccol.riskadmissionscalculateincomes.business.v0.dto.BBody;

@Mapper(componentModel = "spring")
public interface ICalculateV0MapperTxOut {{

                
    @Mappings({{
    {mappings_var}
    }})
    BBody mapOutData(ResponseTransactionCmlct001_1 responseTransactionCmlct0011);


}}
        """

    guardar.guardar_interface(carpeta, nueva_carpeta, origen_archivo, interface_concatenated, False, True)

#generar_interfaces_out_trx()


def generar_mappers(carpeta, nueva_carpeta, int_carpeta, form_carpeta, origen_archivo, ruta_completa):

    # Definir plantillas de prompts
    prompts_mappers = {
        "mapper_facade": """
            Genera un mapper campo a campo desde: {dto_externo} al {dto_interno}.
        """,
        "mapper_business": """
            Genera un mapper campo a campo desde: {dto_interno} al {dto_externo}.
        """
    }

    # Crear los prompt templates
    prompt_template_mapper_facade = PromptTemplate(template=prompts_mappers["mapper_facade"], input_variables=["dto_externo", "dto_interno"])
    prompt_template_mapper_business = PromptTemplate(template=prompts_mappers["mapper_business"], input_variables=["dto_externo", "dto_interno"])


    # lectura de dtos en arbol para generar mapper completo
    with open(ruta_completa, 'r') as archivo:
        contenido = archivo.read()

    # Generar Mapper
    message_mapper_facade = prompt_template_mapper_facade.format(input_raml=contenido)
    message_mapper_business = prompt_template_mapper_business.format(input_raml=contenido)


    mapper_facade = llm.invoke(message_mapper_facade)
    mapper_business = llm.invoke(message_mapper_business)


    # Guardar los resultados en los archivos correspondientes
    guardar.guardar_dtos(carpeta, nueva_carpeta, origen_archivo, mapper_facade)
    guardar.guardar_dtos(carpeta, int_carpeta, origen_archivo, mapper_business)


