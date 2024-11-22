

ruta_archivo = ""

def guardar_test(json):
    # TODO: cambiar ruta
    ruta_archivo = "C:/Users/SURAMERICANA/PycharmProjects/asoAsistantMaster/asoasistantv1/riskadmissionscalculateincomesv0_example/src/test/java/com/bbva/ccol/riskadmissionscalculateincomes/facade/v0/mapper/impl/CalculateMapperTest.java"

    # Crear y guardar un archivo en la carpeta
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(json)

    # with open(ruta_archivo_temp, 'w') as archivo:
    #
    #    #TODO: seguir limpiando los DTOS
    #
    #    json = json.replace("import com.bbva.jee.arq.spring.core.host.Campo;", "")
    #    json = json.replace("import com.bbva.jee.arq.spring.core.host.FilaCampoTabular;", "")
    #    json = json.replace("import com.bbva.jee.arq.spring.core.host.TipoCampo;", "")
    #    json = json.replace("import javax.validation.constraints.NotNull;", "")
    #    json = json.replace("@NotNull", "")
    #
    #
    #    archivo.write(eliminar_lineas_campo(json))

    print(f'Archivo guardado en: {ruta_archivo}')