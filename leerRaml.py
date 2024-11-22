import leerArchivos
import os

def leerRaml(nueva_carpeta, int_carpeta, formatos_carpeta, carpeta_tx, mainDto):

  # Ruta de la carpeta que contiene los archivos
  carpeta_raml = 'motor_laboral/types/calculate-incomes/post/request'  #TODO: Reemplaza con la ruta a tu carpeta

  # Listar todos los archivos en la carpeta
  archivos_raml = os.listdir(carpeta_raml)

  leerArchivos.leerArchivos(carpeta_raml, nueva_carpeta, int_carpeta, formatos_carpeta, "GENERAR_JSON_SCHEMA" , archivos_raml, carpeta_tx, mainDto)


def rectificarDtos(nueva_carpeta, int_carpeta, mainDto):

  # Ruta de la carpeta que contiene los archivos
  #carpeta_raml = 'motor_laboral/types/calculate-incomes/post/request'  #TODO: Reemplaza con la ruta a tu carpeta

  # Listar todos los archivos en la carpeta
  archivos_dtos = os.listdir(nueva_carpeta)
  print(archivos_dtos)










