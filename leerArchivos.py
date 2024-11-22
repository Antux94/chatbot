import os
import generador


def leerArchivos(carpeta, nueva_carpeta, int_carpeta, form_carpeta, accion, archivos, carpeta_tx, mainDto):
  # Iterar sobre cada archivo en la carpeta

  numeroIteracion = 0
  isFirstCall = True

  for archivo in archivos:
      ruta_completa = os.path.join(carpeta, archivo)


      # Asegúrate de que es un archivo y no una subcarpeta
      if os.path.isfile(ruta_completa):
          # Abre y lee el archivo

          if (accion == "GENERAR_JSON_SCHEMA"):
            if (numeroIteracion != 0):
               isFirstCall = False
               
            generador.generar_dtos(carpeta, nueva_carpeta, int_carpeta, form_carpeta, archivo, ruta_completa, carpeta_tx, isFirstCall)



            #TODO: cambiar ruta interface para que se tome de forma automatica
            ruta_interface = "C:/Users/SURAMERICANA/PycharmProjects/asoAsistantv2/ccol_calculate - incomes/facade/v0/mapper"


          with open(ruta_completa, 'r') as archivo_abierto:
              contenido = archivo_abierto.read()

      numeroIteracion = numeroIteracion + 1

  generador.generar_interfaces(carpeta, nueva_carpeta, int_carpeta, form_carpeta, archivo, ruta_completa, mainDto)

  #generador.generar_interfaces_out_trx(carpeta, nueva_carpeta, int_carpeta)