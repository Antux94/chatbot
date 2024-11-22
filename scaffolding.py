import os
import shutil
import leerRaml
import plantillaCopy
import compilador
import leerApiRaml
import generatorTest


#TODO: AJUSTAR TODO EL PROYECTO PARA QUE SEA UN PROYECTO MAVEN Y PARA QUE COMPILE
#TODO: AJUSTAR LA INTERFACE DEL FACADE PARA QUE SE PUEDA TOMAR POR MAPSTRUCS
#TODO: DESCARGAR MAPSTRUCS PARA COMPILAR EL PROYECTO Y GENERAR EL MAPPER


#Copia de plantilla original
#plantillaCopy.copia_plantilla()


def crear_carpetas(rutas):
    """Crea una lista de carpetas si no existen."""
    for ruta in rutas:
        os.makedirs(ruta, exist_ok=True)

def eliminar_si_existe(carpeta):
    """Elimina la carpeta si ya existe."""
    if os.path.exists(carpeta):
        shutil.rmtree(carpeta)
        print(f"La carpeta '{carpeta}' ha sido eliminada.")
    else:
        print(f"La carpeta '{carpeta}' no existe.")

def gen_scaffolding():
    # Definir nombre base y versión
    ruta = 'riskadmissionscalculateincomesv0/src/main/java/com/bbva/ccol/'
    rutaNueva = 'riskadmissionscalculateincomesv0Nuevo/src/main/java/com/bbva/ccol/'
    carpeta_nombre = 'ccol_calculate-incomes'
    carpeta_nombreNuevo = 'riskadmissionscalculateincomes'
    carpeta_tx = 'cmlct001_1' #TODO: Reemplaza con el nombre de la carpeta para la transaccion
    version_mayor = 'v0'

    # Definir las rutas principales
    rutas_facade = [
        f'{ruta}{carpeta_nombre}/facade/{version_mayor}/impl',
        f'{ruta}{carpeta_nombre}/facade/{version_mayor}/dto',
        f'{ruta}{carpeta_nombre}/facade/{version_mayor}/mapper'
    ]

    rutas_business = [
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/impl',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/dao',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/dao/impl',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/dao/models',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/mapper',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/mapper/impl',
        f'{ruta}{carpeta_nombre}/business/{version_mayor}/dto'
    ]

    # Eliminar carpeta si ya existe
    eliminar_si_existe(carpeta_nombre)

    # Crear carpetas base
    crear_carpetas([carpeta_nombre] + rutas_facade + rutas_business)

    # Definir rutas específicas para generar DTOs
    nueva_carpeta = f'{rutaNueva}{carpeta_nombreNuevo}/facade/{version_mayor}/dto'
    int_carpeta = f'{rutaNueva}{carpeta_nombreNuevo}/business/{version_mayor}/dto'
    formatos_carpeta = f'{rutaNueva}{carpeta_nombreNuevo}/business/{version_mayor}/dao/model/{carpeta_tx}/in' #TODO: Reemplaza con la ruta de los formatos, se debe dejar parametrico

    # Llamada a la función genDtos para generar los DTOs
    rutaApi = 'C:/Users/SURAMERICANA/PycharmProjects/asoAsistantMaster/asoasistantv1/motor_laboral/api.raml'
    mainDto = leerApiRaml.leerApiRamml(rutaApi)
    print("MAIN DTO: " + mainDto)
    leerRaml.leerRaml(nueva_carpeta, int_carpeta, formatos_carpeta, carpeta_tx, mainDto)

    # Opcional: Comprimir la carpeta en un archivo zip
    archivo_zip = f"{carpeta_nombre}.zip"
    shutil.make_archive(carpeta_nombre, 'zip', carpeta_nombre)
    print(f"Archivo comprimido: {archivo_zip}")

    #Rectificar nonbre de clases
    leerRaml.rectificarDtos(nueva_carpeta, int_carpeta, mainDto)

# Llamar a la función principal
#gen_scaffolding()


#compilador.compilar()


#mappper = "C:/Users/SURAMERICANA/PycharmProjects/asoAsistantMaster/asoasistantv1/riskadmissionscalculateincomesv0Nuevo/target/generated-sources/annotations/com/bbva/ccol/riskadmissionscalculateincomes/facade/v0/mapper/IPostRiskAdmissionsCalculateIncomesMapperImpl.java"
#
## Leer el contenido del archivo RAML
#with open(mappper, 'r') as archivo:
#    contenido = archivo.read()
#
#generatorTest.generatorTest(contenido)




