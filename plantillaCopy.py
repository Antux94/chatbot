from pathlib import Path
import shutil

def copia_plantilla():
    # Obtener la ruta del directorio actual
    ruta = Path.cwd()

    # Ruta del directorio original
    directorio_origen = ruta / 'riskadmissionscalculateincomesv0_example'

    # TODO: CAMBIAR POR EL NOMBRE DE LA CARPETA SEGÚN EL API.RAML
    nombre_carpeta = 'riskadmissionscalculateincomesv0Nuevo'

    # Ruta del directorio de destino
    directorio_destino = ruta / nombre_carpeta

    # Copiar el directorio completo
    shutil.copytree(directorio_origen, directorio_destino)

