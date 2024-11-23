#import streamlit as st
import math
import time
import os


import os
import streamlit as st





ruta_archivo = ""

def guardar_dtos(ubicacion, carpeta, nombre_archivo, json):
  


  # Ruta de la carpeta donde quieres almacenar el archivo
  carpeta_destino = carpeta
  #carpeta_destino_temp = carpeta + "/temp"

  # Crear la carpeta si no existe
  if not os.path.exists(carpeta_destino):
      os.makedirs(carpeta_destino)

  #if not os.path.exists(carpeta_destino_temp):
  #    os.makedirs(carpeta_destino_temp)

  # Ruta del archivo que deseas guardar
  
  print("CARPETAS.......................")
  print(carpeta_destino)
  print(nombre_archivo)
  print("CARPETAS.......................")

  ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
  #ruta_archivo_temp = os.path.join(carpeta_destino, nombre_archivo)

  pos = ruta_archivo.rfind('/')
  print("POS.......................")
  print(pos)

  # Dividir la cadena
  parte1 = ruta_archivo[:pos]
  parte2 = ruta_archivo[pos+1:]

  ruta_split = parte2.split('.')
  nombre_componente = ruta_split[-2]
  nombre_componente = nombre_componente[0].capitalize() + nombre_componente[1:]

  print (nombre_componente)

  if ("business" in parte1 and "model" not in parte1):
    ruta_archivo =(parte1 + '/B' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")

    #ruta_archivo_temp =(parte1 + '/temp/B' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")

  elif ("business" in parte1 and "model" in parte1):

    print("parte 1: " + parte1)

    if nombre_componente == "Body":
        nombre_componente = "RequestTransactionCmlct001_1"

        #TODO: REEMPLAZAR POR PARAMETRIA PARA EL NOMBRE DE LA TRANSACCION
        json = json.replace("public class Body",
        """
@Transaccion(
    nombre = "CMLCT001",
    tipo = 1, 
    subtipo = 1,	
    version = 1,
    configuracion = "default_apx",
    respuesta = ResponseTransactionCmlct001_1.class,
    atributos = {@Atributo(nombre = "country", valor = "CO")}
)
public class RequestTransactionCmlct001_1""")

    ruta_archivo =(parte1 + '/' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")

    #ruta_archivo_temp =(parte1 + '/temp/' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")

  else:
    ruta_archivo =(parte1 + '/' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")




  # Crear y guardar un archivo en la carpeta
  with open(ruta_archivo, 'w') as archivo:
      archivo.write(json)

  #with open(ruta_archivo_temp, 'w') as archivo:
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


  #TODO: se deja en stand by hasta tenerlo como un proyecto maven y compilarlo completo
  #if ("business" in ruta_archivo and "model" not in ruta_archivo):
  #  compilador.compilar(ruta_archivo_temp)
  #elif ("business" in ruta_archivo and "model" in ruta_archivo):
  #  compilador.compilar(ruta_archivo_temp)
  #else:
  #  compilador.compilar(ruta_archivo)




def eliminar_lineas_campo(texto):
    lineas = texto.split("\n")
    lineas_filtradas = [linea for linea in lineas if not linea.lstrip().startswith("@Campo")]
    return "\n".join(lineas_filtradas)




  #st.info(f'Archivo guardado en: {ruta_archivo}')
  #st.session_state['cantidad_componentes'] += 6.6

  # Título de la aplicación
  #st.title('Generador de Código Java con Efecto de Escritura')

  # Inputs del usuario para el nombre de la clase y metodo (esto podría ajustarse según cómo quieras manejarlo con el archivo)
  #class_name = st.text_input('Nombre de la Clase', 'MiClase')
  #method_name = st.text_input('Nombre del Metodo', 'miMetodo')
  #method_return_type = st.selectbox('Tipo de Retorno del Metodo', ['void', 'int', 'String', 'double'])

  # Botón para generar el código
  #if False:
def read_java_file(file_path):
    """Lee el contenido de un archivo Java y lo devuelve como una cadena."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


file_path = ruta_archivo

# Intenta leer el contenido del archivo Java
try:
    code = read_java_file(file_path)
except FileNotFoundError:
    #st.error(f'El archivo {file_path} no se encontró.')
    code = ""

# Contenedor vacío
if code:  # Solo procede si se encontró el archivo y se leyó el contenido
    code_container = st.empty()

    # Crear un contenedor para ejecutar el script de scroll
    #scroll_script_container = st.empty()

    # Efecto de escritura
    displayed_code = ""
    for char in code:
        displayed_code += char
        code_container.code(displayed_code, language='java')
        time.sleep(0.01)





def guardar_interface(ubicacion, carpeta, nombre_archivo, json, isFacade, isTrxOut):

  # Ruta de la carpeta donde quieres almacenar el archivo

  #TODO: CAMBIAR
  if (isFacade):
    carpeta = "riskadmissionscalculateincomesv0Nuevo/src/main/java/com/bbva/ccol/riskadmissionscalculateincomes/facade/v0/mapper"
  else:
    carpeta = "riskadmissionscalculateincomesv0Nuevo/src/main/java/com/bbva/ccol/riskadmissionscalculateincomes/business/v0/dao/tx/mapper"

  carpeta_destino = carpeta

  # Crear la carpeta si no existe
  if not os.path.exists(carpeta_destino):
      os.makedirs(carpeta_destino)

  # Ruta del archivo que deseas guardar
  #ruta_archivo = os.path.join(carpeta_destino, "I" + "postMapper")

  if (isFacade):
    ruta_archivo = carpeta + "/I" + "PostRiskAdmissionsCalculateIncomesMapper.java"
  elif (isTrxOut):
    ruta_archivo = carpeta + "/I" + "CalculateV0MapperTxOut.java"
  else:
    ruta_archivo = carpeta + "/I" + "CalculateV0MapperTx.java"


  #pos = ruta_archivo.rfind('\\')
#
  ## Dividir la cadena
  #parte1 = ruta_archivo[:pos]
  #parte2 = ruta_archivo[pos+1:]
#
  #ruta_split = parte2.split('.')
  #nombre_componente = ruta_split[-2]
  #nombre_componente = nombre_componente[0].capitalize() + nombre_componente[1:]
  #ruta_archivo =(parte1 + '/' + nombre_componente + '.' + ruta_split[-1]).replace(".raml", ".java")





  # Crear y guardar un archivo en la carpeta
  with open(ruta_archivo, 'w') as archivo:
      archivo.write(json)

  print(f'Archivo guardado en: {ruta_archivo}')

  #TODO: se deja en stand by hasta tenerlo como un proyecto maven y compilarlo completo
  #compilador.compilar(ruta_archivo)

  #st.info(f'Archivo guardado en: {ruta_archivo}')
  #st.session_state['cantidad_componentes'] += 6.6

  # Título de la aplicación
  #st.title('Generador de Código Java con Efecto de Escritura')

  # Inputs del usuario para el nombre de la clase y metodo (esto podría ajustarse según cómo quieras manejarlo con el archivo)
  #class_name = st.text_input('Nombre de la Clase', 'MiClase')
  #method_name = st.text_input('Nombre del Metodo', 'miMetodo')
  #method_return_type = st.selectbox('Tipo de Retorno del Metodo', ['void', 'int', 'String', 'double'])

  # Botón para generar el código
  #if False:
  def read_java_file(file_path):
      """Lee el contenido de un archivo Java y lo devuelve como una cadena."""
      with open(file_path, 'r', encoding='utf-8') as file:
          return file.read()


  file_path = ruta_archivo

  # Intenta leer el contenido del archivo Java
  try:
      code = read_java_file(file_path)
  except FileNotFoundError:
      #st.error(f'El archivo {file_path} no se encontró.')
      code = ""

  # Contenedor vacío
  if code:  # Solo procede si se encontró el archivo y se leyó el contenido
      #code_container = st.empty()

      # Crear un contenedor para ejecutar el script de scroll
      #scroll_script_container = st.empty()

      # Efecto de escritura
      displayed_code = ""
      for char in code:
          displayed_code += char
          #code_container.code(displayed_code, language='java')
          time.sleep(0.01)


