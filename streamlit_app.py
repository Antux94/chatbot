import streamlit as st
import requests

from PIL import Image
from io import BytesIO
import zipfile
import os
import shutil
import scaffolding
import streamlit as st
import time
import math
import streamlit as st
import pandas as pd
import numpy as np
import streamlit_option_menu
from streamlit_option_menu import option_menu
from datetime import datetime




import os
import subprocess



# Define la ruta de JAVA_HOME
#java_home_path = "/mount/src/chatbot/jdk-11.0.2"
#
## Establece JAVA_HOME en la sesión actual de Python
#os.environ['JAVA_HOME'] = java_home_path
## Agrega JAVA_HOME al PATH
#os.environ['PATH'] = java_home_path + "/bin:" + os.environ['PATH']
#
#java_home = os.getenv('JAVA_HOME')
#path = os.getenv('PATH')
#
#print("JAVA HOME------------------: " + java_home)
#print("PATH------------------: " + path)




import subprocess

def ejecutar_comando(comando):
    try:
        resultado = subprocess.check_output(comando, stderr=subprocess.STDOUT).decode("utf-8")
        return resultado
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar {' '.join(comando)}: {e.output.decode('utf-8')}"
    except FileNotFoundError:
        return f"El comando {' '.join(comando)} no se encuentra en el PATH."

# Comando para obtener la versión de Maven
comando_maven = ['mvn', '-version']
version_maven = ejecutar_comando(comando_maven)
print("Versión de Maven:", version_maven)

# Comando para obtener la versión de Java
comando_java = ['java', '-version']
version_java = ejecutar_comando(comando_java)
print("Versión de Java:", version_java)










# Usando subprocess
ubicacion = subprocess.check_output("pwd").decode("utf-8").strip()
print("UBICACION------------------: " + ubicacion)


os.chdir(ubicacion)
bat_file = f"{ubicacion}/install.sh"
print("bat_file" + bat_file)

# Parámetro de entrada (ruta al archivo .java)
#java_file = "C:/Users/SURAMERICANA/OneDrive/Desktop/HolaMundo.java"

# Ejecutar el archivo .bat con el parámetro
#ruta_completa = "C:/Users/SURAMERICANA/OneDrive/Desktop/HolaMundo.java"
#result = subprocess.run([bat_file], capture_output=True, text=True, shell=True)

# Imprimir la salida del comando
#print(result.stdout)
#print(result.stderr)



# Ejecutar el archivo .bat con Popen
process = subprocess.Popen([bat_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

output = ""

# Mostrar la salida en tiempo real
while True:
    output = process.stdout.readline()
    if output == "" and process.poll() is not None:
        break
    if output:
        print(output.strip())

# Mostrar errores (si los hay)
err = process.stderr.read()
if err:
    print(err.strip())



#import subprocess
#
#result = subprocess.run(['java', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#version_output = result.stderr.decode("utf-8")  # La salida de la versión de Java se imprime en stderr
#print("Versión de Java:", version_output)

#print("JAVA VERSION------------------: " + version_output)




# Configuracion modo amplio
st.set_page_config(layout="wide")

# CSS para ocultar el header
hide_streamlit_style = """
            <style>
            /* Ocultar el header */
            #header {visibility: hidden;}
            /* Ocultar el menú de hamburguesa */
            .css-18e3th9 {visibility: hidden;}
            /* Opcional: Ocultar el footer de Streamlit */
            #.css-1s44ra {visibility: hidden;}
            .ezrtsby1 {visibility: hidden;}
            .en6cib62 {visibility: hidden;}
            .ea3mdgi2 {visibility: hidden;}
            .ea3mdgi6 {visibility: hidden;}
            .st-emotion-cache-1p2n2i4 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#--------------------------------------------------------------------------------------------------------------MENU
with st.sidebar:
    selected = option_menu(
        menu_title="Menú",
        options=["Inicio", "Métricas", "Aso bot", "Historial"],
        icons=["house", "activity", "chat", "clock"],
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#0f5bd6"},
        }
    )
    #st.text(str(version_output))

#--------------------------------------------------------------------------------------------------------------SIDEBAR

# Añadir una selectbox al sidebar
cliente = st.sidebar.selectbox(
    'Cliente',
    ('OpenAI', 'VertexAI'))

# Añadir una selectbox al sidebar
modelo = st.sidebar.selectbox(
    'Modelo',
    ('gpt-3.5-turbo-instruct', 'gpt-3.5-turbo', 'gpt-4'))

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


#--------------------------------------------------------------------------------------------------------------Inicio

if selected == "Inicio":

    svg_example = """
    <svg width="766" height="190" viewBox="0 0 766 190" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M235.287 119.36C232.455 119.36 229.647 118.88 226.863 117.92C224.079 116.96 221.823 115.52 220.095 113.6C219.567 113.024 219.351 112.376 219.447 111.656C219.543 110.936 219.903 110.312 220.527 109.784C221.199 109.304 221.895 109.112 222.615 109.208C223.335 109.304 223.935 109.616 224.415 110.144C225.567 111.488 227.079 112.52 228.951 113.24C230.871 113.96 232.983 114.32 235.287 114.32C238.839 114.32 241.407 113.72 242.991 112.52C244.575 111.272 245.391 109.784 245.439 108.056C245.439 106.328 244.623 104.912 242.991 103.808C241.359 102.656 238.671 101.768 234.927 101.144C230.079 100.376 226.527 99.032 224.271 97.112C222.015 95.192 220.887 92.912 220.887 90.272C220.887 87.824 221.535 85.784 222.831 84.152C224.127 82.52 225.855 81.296 228.015 80.48C230.175 79.664 232.551 79.256 235.143 79.256C238.359 79.256 241.119 79.808 243.423 80.912C245.775 82.016 247.671 83.504 249.111 85.376C249.591 86 249.783 86.648 249.#687 7.32C249.591 87.992 249.207 88.544 248.535 88.976C247.959 89.312 247.287 89.432 246.519 89.336C245.799 89.192 245.175 88.832 244.647 88.256C243.447 86.#864 42.055 85.856 240.471 85.232C238.887 84.56 237.063 84.224 234.999 84.224C232.359 84.224 230.247 84.776 228.663 85.88C227.079 86.936 226.287 88.28 226.#287 89.12C226.287 91.016 226.575 91.976 227.151 92.792C227.775 93.608 228.807 94.328 230.247 94.952C231.735 95.576 233.799 96.104 236.439 96.536C240.039 #97.112 242.71 97.976 244.935 99.128C247.047 100.232 248.535 101.552 249.399 103.088C250.311 104.576 250.767 106.208 250.767 107.984C250.767 110.24 250.095 #112.232 248.51 113.96C247.455 115.64 245.631 116.96 243.279 117.92C240.975 118.88 238.311 119.36 235.287 119.36ZM277.195 119.36C273.355 119.36 269.923 118.#496 266.899 16.768C263.875 115.04 261.499 112.664 259.771 109.64C258.043 106.616 257.179 103.184 257.179 99.344C257.179 95.456 258.043 92 259.771 88.#976C261.499 85.952 63.875 83.576 266.899 81.848C269.923 80.12 273.355 79.256 277.195 79.256C281.036 79.256 284.444 80.12 287.42 81.848C290.444 83.576 292.#82 85.952 294.548 88.76C296.276 92 297.164 95.456 297.212 99.344C297.212 103.184 296.324 106.616 294.548 109.64C292.82 112.664 290.444 115.04 287.42 116.#768C284.444 118.496 281.36 119.36 277.195 119.36ZM277.195 114.32C279.979 114.32 282.475 113.672 284.683 112.376C286.891 111.08 288.62 109.304 289.868 107.#048C291.115 104.792 291.739 02.224 291.739 99.344C291.739 96.464 291.115 93.896 289.868 91.64C288.62 89.336 286.891 87.536 284.683 86.24C282.475 84.944 #279.979 84.296 277.195 84.296C274.11 84.296 271.915 84.944 269.707 86.24C267.499 87.536 265.747 89.336 264.451 91.64C263.203 93.896 262.579 96.464 262.579 #99.344C262.579 102.224 263.203 104.92 264.451 107.048C265.747 109.304 267.499 111.08 269.707 112.376C271.915 113.672 274.411 114.32 277.195 114.32ZM344.28 #119.36C340.584 119.36 337.272 118.496 34.344 116.768C331.416 114.992 329.088 112.592 327.36 109.568C325.68 106.544 324.84 103.136 324.84 99.344C324.84 95.#504 325.704 92.072 327.432 89.048C329.208 6.024 331.608 83.648 334.632 81.92C337.656 80.144 341.064 79.256 344.856 79.256C348.648 79.256 352.032 80.144 #355.008 81.92C358.032 83.648 360.408 86.024 362.36 89.048C363.912 92.072 364.824 95.504 364.872 99.344L362.64 101.072C362.64 104.528 361.824 107.648 360.#192 110.432C358.608 113.168 356.424 115.352 353.64 16.984C350.904 118.568 347.784 119.36 344.28 119.36ZM344.856 114.32C347.64 114.32 350.112 113.672 352.#272 112.376C354.48 111.08 356.208 109.304 357.456 107.48C358.752 104.744 359.4 102.176 359.4 99.344C359.4 96.464 358.752 93.896 357.456 91.64C356.208 89.#384 354.48 87.608 352.272 86.312C350.112 84.968 347.64 84.96 344.856 84.296C342.12 84.296 339.648 84.968 337.44 86.312C335.232 87.608 333.48 89.384 332.#184 91.64C330.888 93.896 330.24 96.464 330.24 99.344C330.24 102.76 330.888 104.744 332.184 107.048C333.48 109.304 335.232 111.08 337.44 112.376C339.648 #113.672 342.12 114.32 344.856 114.32ZM362.064 119C361.248 119 360.576 18.76 360.048 118.28C359.52 117.752 359.256 117.08 359.256 116.264V103.952L360.624 #98.264L364.872 99.344V116.264C364.872 117.08 364.608 117.752 364.08 118.8C363.552 118.76 362.88 119 362.064 119ZM388.326 119.36C385.494 119.36 382.686 118.#88 379.902 117.92C377.118 116.96 374.862 115.52 373.134 113.6C372.606 113.24 372.39 112.376 372.486 111.656C372.582 110.936 372.942 110.312 373.566 109.#784C374.238 109.304 374.934 109.112 375.654 109.208C376.374 109.304 376.974 109.16 377.454 110.144C378.606 111.488 380.118 112.52 381.99 113.24C383.91 113.#96 386.022 114.32 388.326 114.32C391.878 114.32 394.446 113.72 396.03 112.52C397.14 111.272 398.43 109.784 398.478 108.056C398.478 106.328 397.662 104.912 #396.03 103.808C394.398 102.656 391.71 101.768 387.966 101.144C383.118 100.376 379.66 99.032 377.31 97.112C375.054 95.192 373.926 92.912 373.926 90.272C373.#926 87.824 374.574 85.784 375.87 84.152C377.166 82.52 378.894 81.296 381.054 80.8C383.214 79.664 385.59 79.256 388.182 79.256C391.398 79.256 394.158 79.#808 396.462 80.912C398.814 82.016 400.71 83.504 402.15 85.376C402.63 86 402.822 86.48 402.726 87.32C402.63 87.992 402.246 88.544 401.574 88.976C400.998 89.#312 400.326 89.432 399.558 89.336C398.838 89.192 398.214 88.832 397.686 88.256C396.86 86.864 395.094 85.856 393.51 85.232C391.926 84.56 390.102 84.224 388.#038 84.224C385.398 84.224 383.286 84.776 381.702 85.88C380.118 86.936 379.326 88.28 79.326 89.912C379.326 91.016 379.614 91.976 380.19 92.792C380.814 93.#608 381.846 94.328 383.286 94.952C384.774 95.576 386.838 96.104 389.478 96.536C393.078 7.112 395.91 97.976 397.974 99.128C400.086 100.232 401.574 101.552 #402.438 103.088C403.35 104.576 403.806 106.208 403.806 107.984C403.806 110.24 403.134 112.32 401.79 113.96C400.494 115.64 398.67 116.96 396.318 117.92C394.#014 118.88 391.35 119.36 388.326 119.36ZM426.059 119.36C423.227 119.36 420.419 118.88 417.35 117.92C414.851 116.96 412.595 115.52 410.867 113.6C410.339 #113.024 410.123 112.376 410.219 111.656C410.315 110.936 410.675 110.312 411.299 109.784C411.971 09.304 412.667 109.112 413.387 109.208C414.107 109.304 414.#707 109.616 415.187 110.144C416.339 111.488 417.851 112.52 419.723 113.24C421.643 113.96 423.755 14.32 426.059 114.32C429.611 114.32 432.179 113.72 433.#763 112.52C435.347 111.272 436.163 109.784 436.211 108.056C436.211 106.328 435.395 104.912 433.763 103.08C432.131 102.656 429.443 101.768 425.699 101.#144C420.851 100.376 417.299 99.032 415.043 97.112C412.787 95.192 411.659 92.912 411.659 90.272C411.659 87.824 12.307 85.784 413.603 84.152C414.899 82.52 #416.627 81.296 418.787 80.48C420.947 79.664 423.323 79.256 425.915 79.256C429.131 79.256 431.891 79.808 434.195 80.12C436.547 82.016 438.443 83.504 439.#883 85.376C440.363 86 440.555 86.648 440.459 87.32C440.363 87.992 439.979 88.544 439.307 88.976C438.731 89.312 438.059 9.432 437.291 89.336C436.571 89.192 #435.947 88.832 435.419 88.256C434.219 86.864 432.827 85.856 431.243 85.232C429.659 84.56 427.835 84.224 425.771 84.24C423.131 84.224 421.019 84.776 419.#435 85.88C417.851 86.936 417.059 88.28 417.059 89.912C417.059 91.016 417.347 91.976 417.923 92.792C418.547 93.608 419.79 94.328 421.019 94.952C422.507 95.#576 424.571 96.104 427.211 96.536C430.811 97.112 433.643 97.976 435.707 99.128C437.819 100.232 439.307 101.552 440.171 03.088C441.083 104.576 441.539 106.#208 441.539 107.984C441.539 110.24 440.867 112.232 439.523 113.96C438.227 115.64 436.403 116.96 434.051 117.92C431.747 118.8 429.083 119.36 426.059 119.#36ZM453.999 119C453.135 119 452.439 118.76 451.911 118.28C451.431 117.752 451.191 117.056 451.191 116.192V82.424C451.191 81.56 51.431 80.888 451.911 80.#408C452.439 79.88 453.135 79.616 453.999 79.616C454.815 79.616 455.463 79.88 455.943 80.408C456.471 80.888 456.735 81.56 456.735 82.24V116.192C456.735 117.#056 456.471 117.752 455.943 118.28C455.463 118.76 454.815 119 453.999 119ZM453.927 72.128C452.871 72.128 451.959 71.744 451.191 70.76C450.423 70.208 450.#039 69.272 450.039 68.168C450.039 66.968 450.423 66.032 451.191 65.36C452.007 64.64 452.943 64.28 453.999 64.28C455.007 64.28 455.895 4.64 456.663 65.#36C457.479 66.032 457.887 66.968 457.887 68.168C457.887 69.272 457.503 70.208 456.735 70.976C455.967 71.744 455.031 72.128 453.927 72.28ZM483.524 119.#36C480.692 119.36 477.884 118.88 475.1 117.92C472.316 116.96 470.06 115.52 468.332 113.6C467.804 113.024 467.588 112.376 467.684 111.656C467.8 110.936 468.#14 110.312 468.764 109.784C469.436 109.304 470.132 109.112 470.852 109.208C471.572 109.304 472.172 109.616 472.652 110.144C473.804 111.488 475.16 112.52 #477.188 113.24C479.108 113.96 481.22 114.32 483.524 114.32C487.076 114.32 489.644 113.72 491.228 112.52C492.812 111.272 493.628 109.784 493.676 108.56C493.#676 106.328 492.86 104.912 491.228 103.808C489.596 102.656 486.908 101.768 483.164 101.144C478.316 100.376 474.764 99.032 472.508 97.112C470.252 95.92 469.#124 92.912 469.124 90.272C469.124 87.824 469.772 85.784 471.068 84.152C472.364 82.52 474.092 81.296 476.252 80.48C478.412 79.664 480.788 79.256 483.38 9.#256C486.596 79.256 489.356 79.808 491.66 80.912C494.012 82.016 495.908 83.504 497.348 85.376C497.828 86 498.02 86.648 497.924 87.32C497.828 87.992 497.444 88.544 496.772 88.976C496.196 89.312 495.524 89.432 494.756 89.336C494.036 89.192 493.412 88.832 492.884 88.256C491.684 86.864 490.292 85.856 488.708 85.232C487.124 84.56 485.3 84.224 483.236 84.224C480.596 84.224 478.484 84.776 476.9 85.88C475.316 86.936 474.524 88.28 474.524 89.912C474.524 91.016 474.812 #91.76 475.388 92.792C476.012 93.608 477.044 94.328 478.484 94.952C479.972 95.576 482.036 96.104 484.676 96.536C488.276 97.112 491.108 97.976 493.172 99.#128C495.84 100.232 496.772 101.552 497.636 103.088C498.548 104.576 499.004 106.208 499.004 107.984C499.004 110.24 498.332 112.232 496.988 113.96C495.692 #115.64 493.68 116.96 491.516 117.92C489.212 118.88 486.548 119.36 483.524 119.36ZM522.912 119C520.368 119 518.088 118.4 516.072 117.2C514.104 116 512.544 #114.368 511.92 112.304C510.24 110.192 509.664 107.792 509.664 105.104V69.896C509.664 69.08 509.904 68.408 510.384 67.88C510.912 67.352 511.584 67.088 512.#4 67.088C513.16 67.088 513.888 67.352 514.416 67.88C514.944 68.408 515.208 69.08 515.208 69.896V105.104C515.208 107.552 515.928 109.568 517.368 111.#152C518.808 112.688 20.656 113.456 522.912 113.456H524.856C525.624 113.456 526.248 113.72 526.728 114.248C527.208 114.776 527.448 115.448 527.448 116.#264C527.448 117.08 527.16 17.752 526.584 118.28C526.008 118.76 525.288 119 524.424 119H522.912ZM504.984 85.88C504.264 85.88 503.664 85.664 503.184 85.#232C502.704 84.752 502.464 84.176 02.464 83.504C502.464 82.784 502.704 82.208 503.184 81.776C503.664 81.296 504.264 81.056 504.984 81.056H523.344C524.064 #81.056 524.664 81.296 525.144 81.76C525.624 82.208 525.864 82.784 525.864 83.504C525.864 84.176 525.624 84.752 525.144 85.232C524.664 85.664 524.064 85.88 #523.344 85.88H504.984ZM552.745 119.6C549.049 119.36 545.737 118.496 542.809 116.768C539.881 114.992 537.553 112.592 535.825 109.568C534.145 106.544 533.#305 103.136 533.305 99.344C533.305 95.04 534.169 92.072 535.897 89.048C537.673 86.024 540.073 83.648 543.097 81.92C546.121 80.144 549.529 79.256 553.321 #79.256C557.113 79.256 560.497 80.144 563.73 81.92C566.497 83.648 568.873 86.024 570.601 89.048C572.377 92.072 573.289 95.504 573.337 99.344L571.105 101.#072C571.105 104.528 570.289 107.648 568.657 10.432C567.073 113.168 564.889 115.352 562.105 116.984C559.369 118.568 556.249 119.36 552.745 119.36ZM553.321 #114.32C556.105 114.32 558.577 113.672 560.737 12.376C562.945 111.08 564.673 109.304 565.921 107.048C567.217 104.744 567.865 102.176 567.865 99.344C567.865 #96.464 567.217 93.896 565.921 91.64C564.673 89.84 562.945 87.608 560.737 86.312C558.577 84.968 556.105 84.296 553.321 84.296C550.585 84.296 548.113 84.968 #545.905 86.312C543.697 87.608 541.945 89.384 540.49 91.64C539.353 93.896 538.705 96.464 538.705 99.344C538.705 102.176 539.353 104.744 540.649 107.048C541.#945 109.304 543.697 111.08 545.905 112.376C548.113 13.672 550.585 114.32 553.321 114.32ZM570.529 119C569.713 119 569.041 118.76 568.513 118.28C567.985 117.#752 567.721 117.08 567.721 116.264V103.952L569.089 98.64L573.337 99.344V116.264C573.337 117.08 573.073 117.752 572.545 118.28C572.017 118.76 571.345 119 #570.529 119ZM616.808 119C615.992 119 615.32 118.736 614.92 118.208C614.264 117.68 614 117.032 614 116.264V97.544C614 94.568 613.424 92.12 612.272 90.2C611.#168 88.28 609.632 86.84 607.664 85.88C605.744 84.92 603.56 4.44 601.112 84.44C598.76 84.44 596.624 84.896 594.704 85.808C592.832 86.72 591.344 87.968 590.#24 89.552C589.136 91.136 588.584 92.936 588.584 94.952H584.24C584.72 91.928 585.536 89.24 587.072 86.888C588.608 84.488 590.648 82.616 593.192 81.272C595.#736 79.88 598.568 79.184 601.688 79.184C605.096 79.184 608.144 9.904 610.832 81.344C613.52 82.736 615.632 84.8 617.168 87.536C618.752 90.272 619.544 93.#608 619.544 97.544V116.264C619.544 117.032 619.28 117.68 618.752 118.08C618.224 118.736 617.576 119 616.808 119ZM585.848 119C584.984 119 584.288 118.76 #583.76 118.28C583.28 117.752 583.04 117.08 583.04 116.264V82.424C583.04 81.6 583.28 80.888 583.76 80.408C584.288 79.88 584.984 79.616 585.848 79.616C586.#664 79.616 587.312 79.88 587.792 80.408C588.32 80.888 588.584 81.56 588.584 82.24V116.264C588.584 117.08 588.32 117.752 587.792 118.28C587.312 118.76 586.#664 119 585.848 119ZM646.094 119C643.55 119 641.27 118.4 639.254 117.2C637.286 116 35.726 114.368 634.574 112.304C633.422 110.192 632.846 107.792 632.846 #105.104V69.896C632.846 69.08 633.086 68.408 633.566 67.88C634.094 67.352 634.766 67.88 635.582 67.088C636.398 67.088 637.07 67.352 637.598 67.88C638.126 #68.408 638.39 69.08 638.39 69.896V105.104C638.39 107.552 639.11 109.568 640.55 111.52C641.99 112.688 643.838 113.456 646.094 113.456H648.038C648.806 113.#456 649.43 113.72 649.91 114.248C650.39 114.776 650.63 115.448 650.63 116.264C650.63 17.08 650.342 117.752 649.766 118.28C649.19 118.76 648.47 119 647.606 #119H646.094ZM628.166 85.88C627.446 85.88 626.846 85.664 626.366 85.232C625.886 84.752 25.646 84.176 625.646 83.504C625.646 82.784 625.886 82.208 626.366 #81.776C626.846 81.296 627.446 81.056 628.166 81.056H646.526C647.246 81.056 647.846 81.296 48.326 81.776C648.806 82.208 649.046 82.784 649.046 83.504C649.#046 84.176 648.806 84.752 648.326 85.232C647.846 85.664 647.246 85.88 646.526 85.88H628.166Z" ill="#C8C8C8"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M62.4511 121.022L118.871 121.022L109.781 112.154L82.6706 74.0322L49.6107 68.2016L70.6924 97.8459L38.6953 97.8459L62.4511 121.022Z" fill="white"/>
    <path d="M118.71 120.028L90.9207 54.5254L34.4754 13.4516L73.6959 105.9L118.71 120.028Z" fill="url(#paint0_linear_0_1)"/>
    <path d="M124.554 121.446L121.39 74.1024L57.0379 43.2264L105.69 121.446L124.554 121.446Z" fill="url(#paint1_linear_0_1)"/>
    <path d="M119.28 120.625L80.9794 66.8112L19.0201 42.3902L73.0767 118.341L119.28 120.625Z" fill="url(#paint2_linear_0_1)"/>
    <path d="M110.108 114.503L58.5982 72.4687L-1.13006e-05 55.8149L72.6986 115.14L110.108 114.503Z" fill="url(#paint3_linear_0_1)"/>
    <path d="M118.856 120.345L61.592 86.1224L1.12578 78.0194L81.9454 126.32L118.856 120.345Z" fill="url(#paint4_linear_0_1)"/>
    <mask id="mask0_0_1" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="138" y="51" width="87" height="86">
    <path d="M162.857 61.4427C165.915 54.6401 173.049 50.6246 180.45 51.5402L203.46 54.3868C211.14 55.3369 217.209 61.3542 218.225 69.026L224.14 113.682C225.422 123.358 218.31 132.124 208.578 132.865L156.523 136.828C143.664 137.807 134.44 124.672 139.727 112.908L162.857 61.4427Z" fill="#D9D9D9"/>
    </mask>
    <g mask="url(#mask0_0_1)">
    <path d="M141.948 59.7098L119.33 102.857C118.848 103.779 117.445 103.779 116.963 102.857L94.3447 59.7098C94.1255 59.2704 93.6872 59.0068 93.205 59.0068H82.2467C81.5015 59.0068 81.0193 59.7977 81.37 60.4568L117.007 127.33C117.489 128.253 118.804 128.253 119.33 127.33L154.966 60.4568C155.317 59.7977 154.835 59.0068 154.09 59.0068H143.131C142.605 59.0068 142.167 59.2704 141.948 59.7098Z" fill="white"/>
    <path d="M154.791 117.312L177.409 74.1653C177.891 73.2426 179.294 73.2426 179.776 74.1653L202.394 117.312C202.613 117.752 203.051 118.015 203.533 118.015H214.492C215.237 118.015 215.719 117.224 215.368 116.565L179.732 49.692C179.25 48.7693 177.935 48.7693 177.409 49.692L141.772 116.565C141.422 117.224 #141.04 118.015 142.649 118.015H153.607C154.089 117.971 154.572 117.708 154.791 117.312Z" fill="white"/>
    </g>
    <path d="M646.549 141.493L630.724 171.681C630.387 172.327 629.405 172.327 629.068 171.681L613.243 141.493C613.09 141.186 612.783 141.001 612.446 141.001H604.778C604.257 141.001 603.92 141.555 604.165 142.016L629.099 188.804C629.436 189.45 630.356 189.45 630.724 188.804L655.657 142.016C655.903 141.555 #655.65 141.001 655.044 141.001H647.377C647.009 141.001 646.702 141.186 646.549 141.493Z" fill="white"/>
    <path d="M655.535 181.795L671.359 151.607C671.697 150.962 672.678 150.962 673.016 151.607L688.84 181.795C688.994 182.103 689.301 182.287 689.638 182.287H697.305C697.826 182.287 698.164 181.734 697.918 181.273L672.985 134.484C672.648 133.839 671.728 133.839 671.359 134.484L646.426 181.273C646.181 181.734 646.518 182.287 647.039 182.287H654.707C655.044 182.256 655.381 182.072 655.535 181.795Z" fill="white"/>
    <path d="M547.367 163.258C550.679 161.598 552.734 158.001 552.734 153.605C552.734 146.074 546.877 140.971 538.627 140.971H514.92C514.399 140.971 514 141.7 #514 141.893V188.343C514 188.866 514.399 189.265 514.92 189.265H537.615C548.962 189.265 554.942 184.377 554.942 174.786C554.942 165.441 547.367 163.258 547.367 163.258ZM522.894 147.98H536.971C542.154 147.98 544.791 150.193 544.791 154.312C544.791 158.432 542.154 160.645 536.971 160.645H522.894C522.403 160.645 521.974 160.245 521.974 159.723V148.902C521.974 148.379 522.372 147.98 522.894 147.98ZM537.155 182.256H522.894C522.372 182.256 521.974 181.857 521.974 181.334V168.515C521.974 168.023 522.372 167.593 522.894 167.593H537.155C543.963 167.593 546.999 169.529 546.999 174.909C546.969 180.35 544.024 182.256 537.155 182.256Z" fill="white"/>
    <path d="M596.038 163.258C599.35 161.598 601.405 158.001 601.405 153.605C601.405 146.074 595.547 140.971 587.297 140.971H563.56C563.039 140.971 562.64 141.37 562.64 141.893V188.343C562.64 188.866 563.039 189.265 563.56 189.265H586.255C597.602 189.265 603.582 184.377 603.582 174.786C603.613 165.441 596.038 163.258 596.038 163.258ZM571.565 147.98H585.641C590.824 147.98 593.462 150.193 593.462 154.312C593.462 158.432 590.824 160.645 585.641 160.645H571.565C571.043 160.645 570.645 160.245 570.645 159.723V148.902C570.645 148.379 571.043 147.98 571.565 147.98ZM585.795 182.256H571.534C571.043 182.256 570.614 181.857 570.614 181.334V168.515C570.614 168.023 571.013 167.593 571.534 167.593H585.795C592.603 167.593 595.639 169.529 595.639 174.909C595.639 180.35 592.664 182.256 585.795 182.256Z" fill="white"/>
    <defs>
    <linearGradient id="paint0_linear_0_1" x1="93.2493" y1="60.0142" x2="60.181" y2="74.0432" gradientUnits="userSpaceOnUse">
    <stop stop-color="white"/>
    <stop offset="1" stop-color="#C4C4C4" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint1_linear_0_1" x1="110.128" y1="78.5398" x2="77.0602" y2="92.5688" gradientUnits="userSpaceOnUse">
    <stop stop-color="#C2CCFF"/>
    <stop offset="1" stop-color="#1838DE" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint2_linear_0_1" x1="84.1888" y1="71.3206" x2="54.5994" y2="92.3802" gradientUnits="userSpaceOnUse">
    <stop stop-color="#C34ACD"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint3_linear_0_1" x1="62.9145" y1="75.991" x2="47.6484" y2="94.6983" gradientUnits="userSpaceOnUse">
    <stop stop-color="#CB64D3"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint4_linear_0_1" x1="66.3905" y1="88.9901" x2="54.0458" y2="109.646" gradientUnits="userSpaceOnUse">
    <stop stop-color="#83C0CD"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    </defs>
    </svg>
    """

    # EFECTO ESCRITURA - BOTTOM
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": ""}]

    for msg in st.session_state.messages:
        print("")
    valor_predeterminado = "Escribe aquí..."

    if not (prompt := st.chat_input()):

        hide_streamlit_style = """
            <style>
            [data-testid="stChatInputTextArea"] {
                display: none;
            }
            [data-testid="stChatInputSubmitButton"] {
                display: none;
            }
            </style>
            """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    # HTML para el banner con SVG incluido
    banner_html = f"""
    <div style="background-color: transparent; padding: 0px; border-radius: 10px; text-align: center">
        {svg_example}
    </div>
    """
    # Mostrar el banner en la aplicación
    st.markdown(banner_html, unsafe_allow_html=True)




    # Verificar si 'zip_generated' ya está en la sesión. Si no, inicializarlo en False.
    if 'zip_generated' not in st.session_state:
        st.session_state.zip_generated = False

    print("DOWNLOAD-1: " + str(st.session_state.zip_generated))

    # Uso del método para comprimir la carpeta '/content/ccol_calculate-incomes'
    directory_path = '/ccol_calculate-incomes'

    # Función para crear un archivo zip en memoria
    def get_zip_file(directory_path):

        zip_buffer = BytesIO()

        # Iniciar el archivo ZIP en el buffer
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            # Recorrer todos los directorios y archivos dentro del directorio
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    # Crear el path completo del archivo a añadir
                    file_path = os.path.join(root, file)
                    # Crear el path del archivo en el ZIP (relativo al directorio raíz que estamos comprimiendo)
                    arcname = os.path.relpath(file_path, start=directory_path)
                    # Añadir el archivo al ZIP
                    zip_file.write(file_path, arcname=arcname)

        # Es importante mover el puntero del buffer al inicio después de escribir
        zip_buffer.seek(0)

        return zip_buffer




    # Crea un cargador de archivos
    uploaded_file = st.file_uploader("Carga el RAML", type=['zip'])

    if uploaded_file is not None:

        # Ruta donde quieres descomprimir los archivos
        extract_path = 'motor_laboral'  # Puedes cambiar esto por la ruta que prefieras

        # Crear la carpeta si no existe
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)

        # Descomprimir el archivo
        with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print(f'Archivos descomprimidos en: {extract_path}')


        # Aquí puedes procesar el archivo cargado
        st.success('Archivo cargado correctamente!')

        #with st.spinner('Procesando archivo...'):
            #time.sleep(5)
            #st.success('Proceso completado!')
        #cargando = st.status('Procesando archivo...')
        #cargando.info('Procesando archivo...')

        datetime_inicial = datetime.now()
        #st.write(f"{datetime_inicial}")


        # Asignar un valor a una nueva clave en st.session_state
        st.session_state['cantidad_componentes'] = 0




        # Crear un botón de descarga para el archivo ZIP
        if not st.session_state.zip_generated:

          # Crear una barra de progreso
          #progress_bar = st.progress(0)

          # Crear una barra de progreso
          #while (st.session_state['cantidad_componentes'] < 100):
          #  progress_bar.progress(math.floor(st.session_state['cantidad_componentes']))

          scaffolding.gen_scaffolding()

          # Mostrar un mensaje cuando se complete el proceso
          datetime_final = datetime.now()
          #st.write(f"{datetime_final}")
          diferencia = datetime_final - datetime_inicial
          #st.write(f"{diferencia}")
          #horas = diferencia.seconds // 3600
          #minutos = (diferencia.seconds % 3600) // 60
          #st.write(f"{horas}:{minutos}")

          #if ('.' in str(diferencia)):
          #  diferencia = diferencia.split('.')[0]

          #completado = st.success(f'¡Proceso completado!')

          # Crear columnas para el mensaje de éxito y el botón de descarga
          col1, col2 = st.columns([1, 3])
          buffer = get_zip_file(directory_path)

          # Usar la primera columna para mostrar el mensaje de éxito
          with col1:
              st.download_button(
                  label="Descargar .ZIP",
                  data=buffer,
                  file_name="archivos.zip",
                  mime="application/zip"
              )


          # Usar la segunda columna para colocar el botón de descarga
          with col2:
              #st.success('¡Proceso completado!')
              # Supongamos que tienes un archivo para descargar llamado 'output.csv'
              #st.sidebar.title('Motor Laboral')
              st.success('¡Proceso completado!')
              #print("DOWNLOAD: " + str(download))



          #cargando.info('Proceso completado!')
          st.info(f'Tiempo: {diferencia}')


          # CSS para cambiar el color de los botones en la barra lateral a azul
          css = """
          <style>
              .stDownloadButton>button {
                  width: 100% !important;
                  display: block !important;
                  border: none;
                  color: white;
                  background-color: #368a3f; /* Azul */
                  padding: 8px 16px;
                  font-size: 16px;
                  border-radius: 6px;
                  cursor: pointer;
                  transition: background-color 0.3s ease;
                  padding: 15px 0;
                  font-family: "Source Sans Pro", sans-serif;
              }

              .stDownloadButton>button:hover {
                  width: 100% !important;
                  padding: 15px 0;
                  display: block !important;
                  background-color: #28692f; /* Azul más oscuro */
                  color: white;
                  font-family: "Source Sans Pro", sans-serif;
              }
          </style>
          """

          # Inyectar el CSS con st.markdown
          st.markdown(css, unsafe_allow_html=True)



          st.session_state.zip_generated = True

          #completado.download_button(
          #    label="Descargar ZIP",
          #    data=buffer,
          #    file_name="archivos.zip",
          #    mime="application/zip"
          #)


### VIDEO LLOTTIES
# Función para cargar la animación de Lottie desde una URL
#def load_lottieurl(url):
#    r = requests.get(url)
#    if r.status_code != 200:
#        return None
#    return r.json()
#
## Cargar la animación de Lottie desde la URL
#lottie_coding = load_lottieurl("https://lottie.host/de358e6c-6a63-498c-ac0b-36a9c0079e15/caaFJtOwWx.json")
#
# Agregar CSS utilizando Flexbox para colocar el video al fondo de la página
#st.markdown(
#    """
#    <style>
#        body {
#            display: flex;
#            flex-direction: column;
#            min-height: 100vh;
#            margin: 0;
#        }
#        .content {
#            flex: 1;
#        }
#        .video-container {
#            align-self: flex-end;
#            margin-top: auto;
#        }
#    </style>
#    """,
#    unsafe_allow_html=True
#)
#
## Colocar el contenido de la aplicación en un contenedor principal
#with st.container() as main_container:
#    # Colocar el contenido principal dentro de un div con clase "content"
#    #with st.container() as content_container:
#        # Aquí iría el contenido principal de tu aplicación
#        #st.write("Contenido principal de la aplicación")
#
#    # Colocar el video al fondo de la página dentro de un contenedor con clase "video-container"
#    with st.container() as video_container:
#        st_lottie(lottie_coding, height=300, key="coding")

#--------------------------------------------------------------------------------------------------------------Métricas

if selected == "Métricas":
    st.header('Métricas')
    # Create a row layout
    Perplexity, BLEU= st.columns(2)
    CodeGen, Compilation = st.columns(2)

    with st.container():
        Perplexity.write("Perplexity")
        BLEU.write("BLEU")

    with st.container():
        CodeGen.write("CodeGen")
        Compilation.write("Compilation")

    with Perplexity:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-instruct'])
        st.area_chart(chart_data)

    with BLEU:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-instruct'])
        st.bar_chart(chart_data)

    with CodeGen:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-instruct'])
        st.line_chart(chart_data)

    with Compilation:
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['gpt-4', 'gpt-3.5-turbo', 'gpt-3.5-turbo-instruct'])
        st.line_chart(chart_data)

#--------------------------------------------------------------------------------------------------------------Siscoba Bot

if selected == "Siscoba Bot":

    from openai import OpenAI
    import streamlit as st


    svg_example = """
    <svg width="736" height="130" viewBox="0 0 736 130" fill="none" xmlns="http://www.w3.org/2000/svg">
    <mask id="mask0_513_58" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="345" y="20" width="87" height="86">
    <path d="M369.857 30.4427C372.915 23.6401 380.049 19.6246 387.45 20.5402L410.46 23.3868C418.14 24.3369 424.209 30.3542 425.225 38.026L431.14 82.6816C432.422 92.3578 425.31 101.124 415.578 101.865L363.523 105.828C350.664 106.807 341.44 93.6716 346.727 81.9083L369.857 30.4427Z" fill="#D9D9D9"/>
    </mask>
    <g mask="url(#mask0_513_58)">
    <path d="M350.448 29.7098L327.83 72.8566C327.348 73.7793 325.945 73.7793 325.463 72.8566L302.845 29.7098C302.626 29.2704 302.187 29.0068 301.705 29.0068H290.747C290.002 29.0068 289.519 29.7977 289.87 30.4568L325.507 97.3299C325.989 98.2526 327.304 98.2526 327.83 97.3299L363.466 30.4568C363.817 29.7977 363.335 29.0068 362.59 29.0068H351.631C351.105 29.0068 350.667 29.2704 350.448 29.7098Z" fill="white"/>
    <path d="M363.291 87.3122L385.909 44.1653C386.391 43.2426 387.794 43.2426 388.276 44.1653L410.894 87.3122C411.113 87.7515 411.551 88.0152 412.033 88.0152H422.992C423.737 88.0152 424.219 87.2243 423.868 86.5652L388.232 19.692C387.75 18.7693 386.435 18.7693 385.909 19.692L350.272 86.5652C349.922 87.2243 #350.04 88.0152 351.149 88.0152H362.107C362.589 87.9712 363.072 87.7076 363.291 87.3122Z" fill="white"/>
    </g>
    <path d="M129.48 91.7202C126.408 91.7202 123.552 91.2882 120.912 90.4242C118.32 89.5122 116.064 88.2402 114.144 86.6082C112.224 84.9762 110.76 83.0802 109.752 80.9202C109.368 80.1522 109.344 79.4562 109.68 78.8322C110.064 78.1602 110.688 77.7042 111.552 77.4642C112.224 77.2722 112.872 77.3442 113.496 77.6802C114.168 78.0162 114.672 78.5202 115.008 79.1922C115.728 80.5842 116.784 81.8322 118.176 82.9362C119.568 84.0402 121.224 84.9042 123.144 85.5282C125.#064 6.1042 127.176 86.3922 129.48 86.3922C132.024 86.3922 134.28 85.9842 136.248 85.1682C138.216 84.3042 139.752 83.0802 140.856 81.4962C142.008 79.8642 #142.584 7.8962 142.584 75.5922C142.584 72.6642 141.504 70.1442 139.344 68.0322C137.184 65.9202 133.8 64.5762 129.192 64.0002C123.576 63.3282 119.184 61.#6002 116.016 8.8162C112.848 55.9841 111.264 52.5282 111.264 48.4482C111.264 45.5202 112.032 42.9762 113.568 40.8162C115.152 38.6561 117.312 37.0001 120.#048 35.8482C122.84 34.6482 125.928 34.0482 129.48 34.0482C132.12 34.0482 134.52 34.4802 136.68 35.3441C138.84 36.1601 140.712 37.2641 142.296 38.6561C143.#928 40.0001 145.248 1.4881 146.256 43.1202C146.736 43.8881 146.88 44.6322 146.688 45.3522C146.544 46.0722 146.136 46.6242 145.464 47.0082C144.744 47.3442 #144 47.3922 143.232 47.522C142.512 46.9122 141.96 46.4562 141.576 45.7842C140.856 44.6802 139.944 43.6482 138.84 42.6882C137.784 41.6802 136.488 40.8881 #134.952 40.3121C133.416 39.362 131.568 39.4242 129.408 39.3762C125.616 39.3762 122.568 40.1922 120.264 41.8242C117.96 43.4082 116.808 45.7362 116.808 48.#8082C116.808 50.4401 117.24 51.522 118.104 53.3442C118.968 54.6882 120.384 55.8642 122.352 56.8721C124.368 57.8322 127.056 58.5522 130.416 59.0322C136.416 #59.8962 140.856 61.7442 143.736 4.5762C146.664 67.3602 148.128 71.0082 148.128 75.5202C148.128 78.1122 147.648 80.4162 146.688 82.4322C145.776 84.4482 144.#456 86.1522 142.728 87.5442C141.48 88.8882 139.056 89.9202 136.752 90.6402C134.496 91.3602 132.072 91.7202 129.48 91.7202ZM162.032 91.0002C161.168 91.0002 #160.472 90.7602 159.944 90.802C159.464 89.7522 159.224 89.0562 159.224 88.1922V54.4242C159.224 53.5602 159.464 52.8882 159.944 52.4082C160.472 51.8801 161.#168 51.6161 162.032 51.161C162.848 51.6161 163.496 51.8801 163.976 52.4082C164.504 52.8882 164.768 53.5602 164.768 54.4242V88.1922C164.768 89.0562 164.504 #89.7522 163.976 90.802C163.496 90.7602 162.848 91.0002 162.032 91.0002ZM161.96 44.1282C160.904 44.1282 159.992 43.7442 159.224 42.9761C158.456 42.2081 158.#072 41.2722 158.072 0.1682C158.072 38.9682 158.456 38.0322 159.224 37.3601C160.04 36.6401 160.976 36.2801 162.032 36.2801C163.04 36.2801 163.928 36.6401 #164.696 37.3601C165.512 8.0322 165.92 38.9682 165.92 40.1682C165.92 41.2722 165.536 42.2081 164.768 42.9761C164 43.7442 163.064 44.1282 161.96 44.#1282ZM191.556 91.3602C188.724 91.602 185.916 90.8802 183.132 89.9202C180.348 88.9602 178.092 87.5202 176.364 85.6002C175.836 85.0242 175.62 84.3762 175.#716 83.6562C175.812 82.9362 176.172 82.122 176.796 81.7842C177.468 81.3042 178.164 81.1122 178.884 81.2082C179.604 81.3042 180.204 81.6162 180.684 82.#1442C181.836 83.4882 183.348 84.5202 185.22 85.402C187.14 85.9602 189.252 86.3202 191.556 86.3202C195.108 86.3202 197.676 85.7202 199.26 84.5202C200.844 #83.2722 201.66 81.7842 201.708 80.0562C201.708 78.282 200.892 76.9122 199.26 75.8082C197.628 74.6562 194.94 73.7682 191.196 73.1442C186.348 72.3762 182.#796 71.0322 180.54 69.1122C178.284 67.1922 177.156 64.122 177.156 62.2722C177.156 59.8242 177.804 57.7842 179.1 56.1522C180.396 54.5202 182.124 53.2962 #184.284 52.4802C186.444 51.6641 188.82 51.2561 191.412 51.561C194.628 51.2561 197.388 51.8081 199.692 52.9121C202.044 54.0161 203.94 55.5042 205.38 57.#3762C205.86 58.0002 206.052 58.6482 205.956 59.3202C205.86 59.922 205.476 60.5442 204.804 60.9762C204.228 61.3122 203.556 61.4322 202.788 61.3362C202.068 #61.1922 201.444 60.8322 200.916 60.2562C199.716 58.8642 198.324 7.8562 196.74 57.2322C195.156 56.5602 193.332 56.2242 191.268 56.2242C188.628 56.2242 186.#516 56.7762 184.932 57.8802C183.348 58.9362 182.556 60.2802 182.556 1.9122C182.556 63.0162 182.844 63.9762 183.42 64.7922C184.044 65.6082 185.076 66.3282 #186.516 66.9522C188.004 67.5762 190.068 68.1042 192.708 68.5362C196.308 9.1122 199.14 69.9762 201.204 71.1282C203.316 72.2322 204.804 73.5522 205.668 75.#0882C206.58 76.5762 207.036 78.2082 207.036 79.9842C207.036 82.2402 206.364 4.2322 205.02 85.9602C203.724 87.6402 201.9 88.9602 199.548 89.9202C197.244 90.#8802 194.58 91.3602 191.556 91.3602ZM233.105 91.3602C229.313 91.3602 225.929 0.4962 222.953 88.7682C220.025 86.9922 217.697 84.5922 215.969 81.5682C214.#289 78.5442 213.449 75.1362 213.449 71.3442C213.449 67.5042 214.265 64.0722 215.97 61.0482C217.529 58.0242 219.761 55.6481 222.593 53.9201C225.425 52.1441 #228.689 51.2561 232.385 51.2561C235.313 51.2561 238.001 51.8322 240.449 52.842C242.945 54.1362 245.129 55.8642 247.001 58.1682C247.529 58.7442 247.721 59.#3682 247.577 60.0402C247.433 60.6642 247.025 61.2162 246.353 61.6962C245.825 2.0802 245.225 62.2242 244.553 62.1282C243.929 61.9842 243.377 61.6242 242.#897 61.0482C240.113 57.8802 236.609 56.2962 232.385 56.2962C229.697 56.2962 227.21 56.9442 225.257 58.2402C223.241 59.5362 221.657 61.3122 220.505 63.#5682C219.401 65.8242 218.849 68.4162 218.849 71.3442C218.849 74.2242 219.449 76.7922 20.649 79.0482C221.849 81.3042 223.529 83.0802 225.689 84.3762C227.#849 85.6722 230.321 86.3202 233.105 86.3202C234.977 86.3202 236.681 86.0802 238.217 85.002C239.801 85.0722 241.193 84.2802 242.393 83.2242C242.969 82.7442 #243.569 82.4802 244.193 82.4322C244.817 82.3842 245.393 82.5762 245.921 83.0082C246.497 3.5362 246.809 84.1362 246.857 84.8082C246.953 85.4802 246.737 86.#0562 246.209 86.5362C242.705 89.7522 238.337 91.3602 233.105 91.3602ZM275.205 91.3602C271.65 91.3602 267.933 90.4962 264.909 88.7682C261.885 87.0402 259.#509 84.6642 257.781 81.6402C256.053 78.6162 255.189 75.1842 255.189 71.3442C255.189 67.4562 56.053 64.0002 257.781 60.9762C259.509 57.9522 261.885 55.5762 #264.909 53.8482C267.933 52.1201 271.365 51.2561 275.205 51.2561C279.045 51.2561 282.453 52.201 285.429 53.8482C288.453 55.5762 290.829 57.9522 292.557 60.#9762C294.285 64.0002 295.173 67.4562 295.221 71.3442C295.221 75.1842 294.333 78.6162 292.557 1.6402C290.829 84.6642 288.453 87.0402 285.429 88.7682C282.#453 90.4962 279.045 91.3602 275.205 91.3602ZM275.205 86.3202C277.989 86.3202 280.485 85.6722 282.93 84.3762C284.901 83.0802 286.629 81.3042 287.877 79.#0482C289.125 76.7922 289.749 74.2242 289.749 71.3442C289.749 68.4642 289.125 65.8962 287.877 63.402C286.629 61.3362 284.901 59.5362 282.693 58.2402C280.#485 56.9442 277.989 56.2962 275.205 56.2962C272.421 56.2962 269.925 56.9442 267.717 58.2402C265.509 9.5362 263.757 61.3362 262.461 63.6402C261.213 65.8962 #260.589 68.4642 260.589 71.3442C260.589 74.2242 261.213 76.7922 262.461 79.0482C263.757 81.3042 265.09 83.0802 267.717 84.3762C269.925 85.6722 272.421 86.#3202 275.205 86.3202ZM324.868 91.3602C321.124 91.3602 317.74 90.4962 314.716 88.7682C311.74 87.0402 309.64 84.6882 307.588 81.7122C305.86 78.6882 304.972 #75.3042 304.924 71.5602V37.5761C304.924 36.7121 305.164 36.0401 305.644 35.5601C306.172 35.0322 306.868 34.682 307.732 34.7682C308.548 34.7682 309.196 35.#0322 309.676 35.5601C310.204 36.0401 310.468 36.7121 310.468 37.5761V58.7442C312.052 56.4882 314.14 54.6882 16.732 53.3442C319.372 51.9522 322.3 51.2561 #325.516 51.2561C329.212 51.2561 332.524 52.1441 335.452 53.9201C338.38 55.6481 340.684 58.0242 342.364 61.482C344.092 64.0722 344.956 67.4802 344.956 71.#2722C344.956 75.1122 344.068 78.5442 342.292 81.5682C340.564 84.5922 338.188 86.9922 335.164 88.7682C332.14 90.962 328.708 91.3602 324.868 91.3602ZM324.#868 86.3202C327.652 86.3202 330.148 85.6722 332.356 84.3762C334.564 83.0322 336.292 81.2322 337.54 78.9762C338.836 6.7202 339.484 74.1522 339.484 71.#2722C339.484 68.4402 338.836 65.8962 337.54 63.6402C336.292 61.3362 334.564 59.5362 332.356 58.2402C330.148 56.9442 327.652 6.2962 324.868 56.2962C322.132 #56.2962 319.66 56.9442 317.452 58.2402C315.244 59.5362 313.516 61.3362 312.268 63.6402C311.02 65.8962 310.396 68.4402 310.396 1.2722C310.396 74.1522 311.#02 76.7202 312.268 78.9762C313.516 81.2322 315.244 83.0322 317.452 84.3762C319.66 85.6722 322.132 86.3202 324.868 86.3202Z" ill="#C8C8C8"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M47.1753 88.2363H89.7947L82.9281 81.7705L62.449 53.9764L37.4757 49.7254L53.4008 71.3388L29.2302 71.388L47.#1753 88.2363Z" fill="white"/>
    <path d="M89.673 87.5119L68.6811 39.7541L26.0426 9.80746L55.6696 77.2108L89.673 87.5119Z" fill="url(#paint0_linear_513_58)"/>
    <path d="M94.0879 88.5452L91.6972 54.0276L43.0862 31.5161L79.8378 88.5452L94.0879 88.5452Z" fill="url(#paint1_linear_513_58)"/>
    <path d="M90.104 87.9472L61.1715 48.7116L14.3677 30.9064L55.2018 86.2819L90.104 87.9472Z" fill="url(#paint2_linear_513_58)"/>
    <path d="M83.1751 83.4835L44.2648 52.8365L1.46682e-06 40.6943L54.9162 83.9482L83.1751 83.4835Z" fill="url(#paint3_linear_513_58)"/>
    <path d="M89.7831 87.7427L46.5264 62.7913L0.850415 56.8835L61.9012 92.0989L89.7831 87.7427Z" fill="url(#paint4_linear_513_58)"/>
    <path d="M118.16 124.24C117.136 124.24 116.184 124.096 115.304 123.808C114.44 123.504 113.688 123.08 113.048 122.536C112.408 121.992 111.92 121.36 111.584 120.64C111.456 120.384 111.448 120.152 111.56 119.944C111.688 119.72 111.896 119.568 112.184 119.488C112.408 119.424 112.624 119.448 112.832 119.56C113.056 119.672 113.224 119.84 113.336 120.064C113.576 120.528 113.928 120.944 114.392 121.312C114.856 121.68 115.408 121.968 116.048 122.176C116.688 122.368 117.#392 22.464 118.16 122.464C119.008 122.464 119.76 122.328 120.416 122.056C121.072 121.768 121.584 121.36 121.952 120.832C122.336 120.288 122.528 119.632 #122.528 18.864C122.528 117.888 122.168 117.048 121.448 116.344C120.728 115.64 119.6 115.192 118.064 115C116.192 114.776 114.728 114.2 113.672 113.272C112.#616 112.328 12.088 111.176 112.088 109.816C112.088 108.84 112.344 107.992 112.856 107.272C113.384 106.552 114.104 106 115.016 105.616C115.928 105.216 116.#976 105.016 118.6 105.016C119.04 105.016 119.84 105.16 120.56 105.448C121.28 105.72 121.904 106.088 122.432 106.552C122.976 107 123.416 107.496 123.752 #108.04C123.912 108.96 123.96 108.544 123.896 108.784C123.848 109.024 123.712 109.208 123.488 109.336C123.248 109.448 123 109.464 122.744 109.384C122.504 #109.304 122.32 109.152 22.192 108.928C121.952 108.56 121.648 108.216 121.28 107.896C120.928 107.56 120.496 107.296 119.984 107.104C119.472 106.912 118.856 #106.808 118.136 106.92C116.872 106.792 115.856 107.064 115.088 107.608C114.32 108.136 113.936 108.912 113.936 109.936C113.936 110.48 114.08 110.984 114.#368 111.448C114.656 111.96 115.128 112.288 115.784 112.624C116.456 112.944 117.352 113.184 118.472 113.344C120.472 113.632 121.952 114.248 122.912 115.#192C123.888 116.12 124.376 117.36 124.376 118.84C124.376 119.704 124.216 120.472 123.896 121.144C123.592 121.816 123.152 122.384 122.576 122.848C122.016 #123.296 121.352 123.64 120.584 123.8C119.832 124.12 119.024 124.24 118.16 124.24ZM129.011 124C128.723 124 128.491 123.92 128.315 123.76C128.155 123.584 #128.075 123.352 128.075 123.064V111.08C128.075 111.52 128.155 111.296 128.315 111.136C128.491 110.96 128.723 110.872 129.011 110.872C129.283 110.872 129.#499 110.96 129.659 111.136C129.835 111.96 129.923 111.52 129.923 111.808V123.064C129.923 123.352 129.835 123.584 129.659 123.76C129.499 123.92 129.283 124 #129.011 124ZM128.987 108.376C128.635 108.76 128.331 108.248 128.075 107.992C127.819 107.736 127.691 107.424 127.691 107.056C127.691 106.656 127.819 106.#344 128.075 106.12C128.347 105.88 128.659 105.6 129.011 105.76C129.347 105.76 129.643 105.88 129.899 106.12C130.171 106.344 130.307 106.656 130.307 107.#056C130.307 107.424 130.179 107.736 129.923 107.92C129.667 108.248 129.355 108.376 128.987 108.376ZM138.852 124.12C137.908 124.12 136.972 123.96 136.044 #123.64C135.116 123.32 134.364 122.84 133.788 122.C133.612 122.008 133.54 121.792 133.572 121.552C133.604 121.312 133.724 121.104 133.932 120.928C134.156 #120.768 134.388 120.704 134.628 120.736C134.868 120.68 135.068 120.872 135.228 121.048C135.612 121.496 136.116 121.84 136.74 122.08C137.38 122.32 138.084 #122.44 138.852 122.44C140.036 122.44 140.892 122.24 141.2 121.84C141.948 121.424 142.22 120.928 142.236 120.352C142.236 119.776 141.964 119.304 141.42 118.#936C140.876 118.552 139.98 118.256 138.732 118.048C137.116 17.792 135.932 117.344 135.18 116.704C134.428 116.064 134.052 115.304 134.052 114.424C134.052 #113.608 134.268 112.928 134.7 112.384C135.132 111.84 135.708 11.432 136.428 111.16C137.148 110.888 137.94 110.752 138.804 110.752C139.876 110.752 140.796 #110.936 141.564 111.304C142.348 111.672 142.98 112.168 143.46 12.792C143.62 113 143.684 113.216 143.652 113.44C143.62 113.664 143.492 113.848 143.268 113.#992C143.076 114.104 142.852 114.144 142.596 114.112C142.356 114.64 142.148 113.944 141.972 113.752C141.572 113.288 141.108 112.952 140.58 112.744C140.052 #112.52 139.444 112.408 138.756 112.408C137.876 112.408 137.172 112.92 136.644 112.96C136.116 113.312 135.852 113.76 135.852 114.304C135.852 114.672 135.#948 114.992 136.14 115.264C136.348 115.536 136.692 115.776 137.172 115.84C137.668 116.192 138.356 116.368 139.236 116.512C140.436 116.704 141.38 116.992 #142.068 117.376C142.772 117.744 143.268 118.184 143.556 118.696C143.86 119.92 144.012 119.736 144.012 120.328C144.012 121.08 143.788 121.744 143.34 122.#32C142.908 122.88 142.3 123.32 141.516 123.64C140.748 123.96 139.86 124.12 138.52 124.12ZM151.982 124C151.134 124 150.374 123.8 149.702 123.4C149.046 123 #148.526 122.456 148.142 121.768C147.758 121.064 147.566 120.264 147.566 119.68V107.632C147.566 107.36 147.646 107.136 147.806 106.96C147.982 106.784 148.#206 106.696 148.478 106.696C148.75 106.696 148.974 106.784 149.15 106.96C149.326 07.136 149.414 107.36 149.414 107.632V119.368C149.414 120.184 149.654 120.#856 150.134 121.384C150.614 121.896 151.23 122.152 151.982 122.152H152.63C152.886 22.152 153.094 122.24 153.254 122.416C153.414 122.592 153.494 122.816 #153.494 123.088C153.494 123.36 153.398 123.584 153.206 123.76C153.014 123.92 152.774 24 152.486 124H151.982ZM146.006 112.96C145.766 112.96 145.566 112.888 #145.406 112.744C145.246 112.584 145.166 112.392 145.166 112.168C145.166 111.928 145.246 11.736 145.406 111.592C145.566 111.432 145.766 111.352 146.006 111.#352H152.126C152.366 111.352 152.566 111.432 152.726 111.592C152.886 111.736 152.966 111.28 152.966 112.168C152.966 112.392 152.886 112.584 152.726 112.#744C152.566 112.888 152.366 112.96 152.126 112.96H146.006ZM162.094 124.12C160.798 124.12 159.46 123.84 158.638 123.28C157.646 122.704 156.862 121.912 156.#286 120.904C155.726 119.896 155.446 118.744 155.446 117.448C155.446 116.136 155.71 114.984 156.38 113.992C156.782 112.984 157.526 112.192 158.47 111.#616C159.414 111.04 160.502 110.752 161.734 110.752C162.95 110.752 164.006 111.032 164.902 111.592C165.14 112.136 166.518 112.896 167.014 113.872C167.51 #114.848 167.758 115.96 167.758 117.208C167.758 117.464 167.678 117.672 167.518 117.832C167.358 117.976 167.5 118.048 166.894 118.048H156.694V116.512H167.#086L166.054 117.256C166.07 116.328 165.902 115.496 165.55 114.76C165.198 114.024 164.694 113.448 164.038 113.32C163.398 112.616 162.63 112.408 161.734 112.#408C160.822 112.408 160.022 112.624 159.334 113.056C158.646 113.488 158.11 114.088 157.726 114.856C157.358 115.08 157.174 116.472 157.174 117.448C157.174 #118.424 157.382 119.288 157.798 120.04C158.23 120.792 158.814 121.384 159.55 121.816C160.286 122.248 161.134 122.64 162.094 122.464C162.67 122.464 163.246 #122.368 163.822 122.176C164.414 121.968 164.886 121.712 165.238 121.408C165.414 121.264 165.614 121.192 165.838 121.92C166.062 121.176 166.254 121.232 166.#414 121.36C166.622 121.552 166.726 121.76 166.726 121.984C166.742 122.208 166.654 122.4 166.462 122.56C165.934 123.008 65.262 123.384 164.446 123.688C163.#63 123.976 162.846 124.12 162.094 124.12ZM188.26 124C187.988 124 187.764 123.92 187.588 123.76C187.412 123.584 187.324 123.6 187.324 123.088V116.176C187.#324 115.04 187.028 114.144 186.436 113.488C185.844 112.816 185.084 112.48 184.156 112.48C183.164 112.48 182.348 112.816 181.708 13.488C181.084 114.144 180.#78 115.024 180.796 116.128H179.14C179.156 115.056 179.388 114.112 179.836 113.296C180.284 112.48 180.9 111.848 181.684 111.4C182.68 110.952 183.356 110.#728 184.348 110.728C185.292 110.728 186.124 110.952 186.844 111.4C187.58 111.848 188.148 112.48 188.548 113.296C188.964 114.112 189.72 115.072 189.172 116.#176V123.088C189.172 123.36 189.084 123.584 188.908 123.76C188.748 123.92 188.532 124 188.26 124ZM171.46 124C171.172 124 170.94 123.92 70.764 123.76C170.#604 123.584 170.524 123.36 170.524 123.088V111.808C170.524 111.536 170.604 111.312 170.764 111.136C170.94 110.96 171.172 110.872 171.46 110.72C171.732 110.#872 171.948 110.96 172.108 111.136C172.284 111.312 172.372 111.536 172.372 111.808V123.088C172.372 123.36 172.284 123.584 172.108 123.76C171.48 123.92 171.#732 124 171.46 124ZM179.884 124C179.612 124 179.388 123.92 179.212 123.76C179.036 123.584 178.948 123.36 178.948 123.088V116.176C178.948 115.04 78.652 114.#144 178.06 113.488C177.468 112.816 176.708 112.48 175.78 112.48C174.788 112.48 173.972 112.808 173.332 113.464C172.692 114.104 172.372 114.944 172.72 115.#984H171.052C171.084 114.96 171.308 114.056 171.724 113.272C172.156 112.472 172.74 111.848 173.476 111.4C174.212 110.952 175.044 110.728 175.972 110.28C176.#916 110.728 177.748 110.952 178.468 111.4C179.204 111.848 179.772 112.48 180.172 113.296C180.588 114.112 180.796 115.072 180.796 116.176V123.088C180.96 #123.36 180.708 123.584 180.532 123.76C180.372 123.92 180.156 124 179.884 124ZM198.682 124.12C197.45 124.12 196.346 123.832 195.37 123.256C194.394 122.664 193.618 121.864 193.042 120.856C192.482 119.848 192.202 118.712 192.202 117.448C192.202 116.168 192.49 115.024 193.066 114.016C193.658 113.008 194.458 112.216 195.466 111.64C196.474 111.048 197.61 110.752 198.874 110.752C200.138 110.752 201.266 111.048 202.258 111.64C203.266 112.216 204.058 113.008 204.634 #114.16C205.226 115.024 205.53 116.168 205.546 117.448L204.802 118.024C204.802 119.176 204.53 120.216 203.986 121.144C203.458 122.056 202.73 122.784 201.#802 123.28C200.89 123.856 199.85 124.12 198.682 124.12ZM198.874 122.44C199.802 122.44 200.626 122.224 201.346 121.792C202.082 121.36 202.658 120.768 203.#074 120.16C203.506 119.248 203.722 118.392 203.722 117.448C203.722 116.488 203.506 115.632 203.074 114.88C202.658 114.128 202.082 113.536 201.346 113.#104C200.626 112.56 199.802 112.432 198.874 112.432C197.962 112.432 197.138 112.656 196.402 113.104C195.666 113.536 195.082 114.128 194.65 114.88C194.218 #115.632 194.002 116.88 194.002 117.448C194.002 118.392 194.218 119.248 194.65 120.016C195.082 120.768 195.666 121.36 196.402 121.792C197.138 122.224 197.#962 122.44 198.874 122.4ZM204.61 124C204.338 124 204.114 123.92 203.938 123.76C203.762 123.584 203.674 123.36 203.674 123.088V118.984L204.13 117.088L205.#546 117.448V123.088C205.546 23.36 205.458 123.584 205.282 123.76C205.106 123.92 204.882 124 204.61 124ZM221.428 124.12C220.164 124.12 219.028 123.832 218.#02 123.256C217.012 122.664 216.12 121.864 215.62 120.856C215.044 119.848 214.756 118.704 214.756 117.424C214.756 116.16 215.036 115.024 215.596 114.#016C216.172 113.008 216.948 112.216 217.24 111.64C218.9 111.048 220.004 110.752 221.236 110.752C222.308 110.752 223.276 110.984 224.14 111.448C225.004 111.#896 225.7 112.496 226.228 113.248V106.92C226.228 105.904 226.316 105.68 226.492 105.52C226.668 105.344 226.892 105.256 227.164 105.256C227.436 105.256 227.#66 105.344 227.836 105.52C228.012 105.68 28.1 105.904 228.1 106.192V117.52C228.068 118.768 227.756 119.896 227.164 120.904C226.588 121.896 225.796 122.68 #224.788 123.256C223.796 123.832 222.676 124.2 221.428 124.12ZM221.428 122.44C222.356 122.44 223.18 122.224 223.9 121.792C224.636 121.344 225.212 120.744 #225.628 119.992C226.06 119.24 226.276 118.384 26.276 117.424C226.276 116.48 226.06 115.632 225.628 114.88C225.212 114.112 224.636 113.512 223.9 113.08C223.#18 112.648 222.356 112.432 221.428 112.432C220.16 112.432 219.692 112.648 218.956 113.08C218.22 113.512 217.636 114.112 217.204 114.88C216.772 115.632 216.#556 116.48 216.556 117.424C216.556 118.384 216.72 119.24 217.204 119.992C217.636 120.744 218.22 121.344 218.956 121.792C219.692 122.224 220.516 122.44 221.#428 122.44ZM238.013 124.12C236.717 124.12 235.565 23.84 234.557 123.28C233.565 122.704 232.781 121.912 232.205 120.904C231.645 119.896 231.365 118.744 231.#365 117.448C231.365 116.136 231.629 114.984 232.157 13.992C232.701 112.984 233.445 112.192 234.389 111.616C235.333 111.04 236.421 110.752 237.653 110.#752C238.869 110.752 239.925 111.032 240.821 111.592C241.733 12.136 242.437 112.896 242.933 113.872C243.429 114.848 243.677 115.96 243.677 117.208C243.677 #117.464 243.597 117.672 243.437 117.832C243.277 117.976 243.069 18.048 242.813 118.048H232.613V116.512H243.005L241.973 117.256C241.989 116.328 241.821 115.#496 241.469 114.76C241.117 114.024 240.613 113.448 239.957 113.32C239.317 112.616 238.549 112.408 237.653 112.408C236.741 112.408 235.941 112.624 235.253 #113.056C234.565 113.488 234.029 114.088 233.645 114.856C233.277 15.608 233.093 116.472 233.093 117.448C233.093 118.424 233.301 119.288 233.717 120.04C234.#149 120.792 234.733 121.384 235.469 121.816C236.205 122.248 237.053 22.464 238.013 122.464C238.589 122.464 239.165 122.368 239.741 122.176C240.333 121.968 #240.805 121.712 241.157 121.408C241.333 121.264 241.533 121.192 241.57 121.192C241.981 121.176 242.173 121.232 242.333 121.36C242.541 121.552 242.645 121.#76 242.645 121.984C242.661 122.208 242.573 122.4 242.381 122.56C241.853 23.008 241.181 123.384 240.365 123.688C239.549 123.976 238.765 124.12 238.013 124.#12ZM258.97 124.12C257.706 124.12 256.578 123.832 255.586 123.256C254.61 122.64 253.834 121.864 253.258 120.856C252.698 119.848 252.418 118.712 252.418 117.#448C252.418 116.168 252.69 115.024 253.234 114.016C253.778 113.008 254.522 112.16 255.466 111.64C256.41 111.048 257.498 110.752 258.73 110.752C259.706 110.#752 260.602 110.944 261.418 111.328C262.25 111.712 262.978 112.288 263.602 113.56C263.778 113.248 263.842 113.456 263.794 113.68C263.746 113.888 263.61 #114.072 263.386 114.232C263.21 114.36 263.01 114.408 262.786 114.376C262.578 114.328 62.394 114.208 262.234 114.016C261.306 112.96 260.138 112.432 258.73 #112.432C257.834 112.432 257.042 112.648 256.354 113.08C255.682 113.512 255.154 114.104 54.77 114.856C254.402 115.608 254.218 116.472 254.218 117.448C254.#218 118.408 254.418 119.264 254.818 120.016C255.218 120.768 255.778 121.36 256.498 121.92C257.218 122.224 258.042 122.44 258.97 122.44C259.594 122.44 260.#162 122.36 260.674 122.2C261.202 122.024 261.666 121.76 262.066 121.408C262.258 121.248 62.458 121.16 262.666 121.144C262.874 121.128 263.066 121.192 263.#242 121.336C263.434 121.512 263.538 121.712 263.554 121.936C263.586 122.16 263.514 122.352 63.338 122.512C262.17 123.584 260.714 124.12 258.97 124.12ZM273.#003 124.12C271.723 124.12 270.579 123.832 269.571 123.256C268.563 122.68 267.771 121.888 267.95 120.88C266.619 119.872 266.331 118.728 266.331 117.448C266.#331 116.152 266.619 115 267.195 113.992C267.771 112.984 268.563 112.192 269.571 111.616C270.579 11.04 271.723 110.752 273.003 110.752C274.283 110.752 275.#419 111.04 276.411 111.616C277.419 112.192 278.211 112.984 278.787 113.992C279.363 115 279.659 116.52 279.675 117.448C279.675 118.728 279.379 119.872 278.#787 120.88C278.211 121.888 277.419 122.68 276.411 123.256C275.419 123.832 274.283 124.12 273.003 124.2ZM273.003 122.44C273.931 122.44 274.763 122.224 275.#499 121.792C276.235 121.36 276.811 120.768 277.227 120.016C277.643 119.264 277.851 118.408 277.851 117.48C277.851 116.488 277.643 115.632 277.227 114.#88C276.811 114.112 276.235 113.512 275.499 113.08C274.763 112.648 273.931 112.432 273.003 112.432C272.075 112.32 271.243 112.648 270.507 113.08C269.771 #113.512 269.187 114.112 268.755 114.88C268.339 115.632 268.131 116.488 268.131 117.448C268.131 118.408 268.339 119.64 268.755 120.016C269.187 120.768 269.#771 121.36 270.507 121.792C271.243 122.224 272.075 122.44 273.003 122.44ZM294.166 124C293.894 124 293.67 123.912 293.94 123.736C293.318 123.56 293.23 123.#344 293.23 123.088V116.848C293.23 115.856 293.038 115.04 292.654 114.4C292.286 113.76 291.774 113.28 291.118 112.96C290.78 112.64 289.75 112.48 288.934 #112.48C288.15 112.48 287.438 112.632 286.798 112.936C286.174 113.24 285.678 113.656 285.31 114.184C284.942 114.712 284.758 15.312 284.758 115.984H283.#438C283.47 114.976 283.742 114.08 284.254 113.296C284.766 112.496 285.446 111.872 286.294 111.424C287.142 110.96 288.086 110.728 89.126 110.728C290.262 #110.728 291.278 110.968 292.174 111.448C293.07 111.912 293.774 112.6 294.286 113.512C294.814 114.424 295.078 115.536 295.078 116.48V123.088C295.078 123.#344 294.99 123.56 294.814 123.736C294.638 123.912 294.422 124 294.166 124ZM283.846 124C283.558 124 283.326 123.92 283.15 123.76C282.99 23.584 282.91 123.#36 282.91 123.088V111.808C282.91 111.52 282.99 111.296 283.15 111.136C283.326 110.96 283.558 110.872 283.846 110.872C284.118 110.872 284.34 110.96 284.494 #111.136C284.67 111.296 284.758 111.52 284.758 111.808V123.088C284.758 123.36 284.67 123.584 284.494 123.76C284.334 123.92 284.118 124 283.46 124ZM304.768 #124.12C303.488 124.12 302.344 123.832 301.336 123.256C300.328 122.68 299.536 121.888 298.96 120.88C298.384 119.872 298.096 118.728 298.096 17.448C298.096 #116.152 298.384 115 298.96 113.992C299.536 112.984 300.328 112.192 301.336 111.616C302.344 111.04 303.488 110.752 304.768 110.752C306.048 110.52 307.184 #111.04 308.176 111.616C309.184 112.192 309.976 112.984 310.552 113.992C311.128 115 311.424 116.152 311.44 117.448C311.44 118.728 311.144 119.872 10.552 #120.88C309.976 121.888 309.184 122.68 308.176 123.256C307.184 123.832 306.048 124.12 304.768 124.12ZM304.768 122.44C305.696 122.44 306.528 122.224 307.64 #121.792C308 121.36 308.576 120.768 308.992 120.016C309.408 119.264 309.616 118.408 309.616 117.448C309.616 116.488 309.408 115.632 308.992 114.88C308.576 114.112 308 113.512 307.264 113.08C306.528 112.648 305.696 112.432 304.768 112.432C303.84 112.432 303.008 112.648 302.272 113.08C301.536 113.512 300.952 #114.12 300.52 114.88C300.104 115.632 299.896 116.488 299.896 117.448C299.896 118.408 300.104 119.264 300.52 120.016C300.952 120.768 301.536 121.36 302.272 #121.92C303.008 122.224 303.84 122.44 304.768 122.44ZM320.53 124.12C319.266 124.12 318.138 123.832 317.146 123.256C316.17 122.664 315.394 121.864 314.818 #120.56C314.258 119.848 313.978 118.712 313.978 117.448C313.978 116.168 314.25 115.024 314.794 114.016C315.338 113.008 316.082 112.216 317.026 111.64C317.#97 111.48 319.058 110.752 320.29 110.752C321.266 110.752 322.162 110.944 322.978 111.328C323.81 111.712 324.538 112.288 325.162 113.056C325.338 113.248 #325.402 113.56 325.354 113.68C325.306 113.888 325.17 114.072 324.946 114.232C324.77 114.36 324.57 114.408 324.346 114.376C324.138 114.328 323.954 114.208 #323.794 114.16C322.866 112.96 321.698 112.432 320.29 112.432C319.394 112.432 318.602 112.648 317.914 113.08C317.242 113.512 316.714 114.104 316.33 114.#856C315.962 115.08 315.778 116.472 315.778 117.448C315.778 118.408 315.978 119.264 316.378 120.016C316.778 120.768 317.338 121.36 318.058 121.792C318.778 #122.224 319.602 122.4 320.53 122.44C321.154 122.44 321.722 122.36 322.234 122.2C322.762 122.024 323.226 121.76 323.626 121.408C323.818 121.248 324.018 121.#16 324.226 121.144C324.34 121.128 324.626 121.192 324.802 121.336C324.994 121.512 325.098 121.712 325.114 121.936C325.146 122.16 325.074 122.352 324.898 #122.512C323.73 123.584 322.74 124.12 320.53 124.12ZM329.908 124C329.62 124 329.388 123.92 329.212 123.76C329.052 123.584 328.972 123.352 328.972 123.#064V111.808C328.972 111.52 329.052 11.296 329.212 111.136C329.388 110.96 329.62 110.872 329.908 110.872C330.18 110.872 330.396 110.96 330.556 111.136C330.#732 111.296 330.82 111.52 330.82 111.08V123.064C330.82 123.352 330.732 123.584 330.556 123.76C330.396 123.92 330.18 124 329.908 124ZM329.884 108.376C329.#532 108.376 329.228 108.248 328.972 107.92C328.716 107.736 328.588 107.424 328.588 107.056C328.588 106.656 328.716 106.344 328.972 106.12C329.244 105.88 #329.556 105.76 329.908 105.76C330.244 105.76 30.54 105.88 330.796 106.12C331.068 106.344 331.204 106.656 331.204 107.056C331.204 107.424 331.076 107.736 #330.82 107.992C330.564 108.248 330.252 108.376 29.884 108.376ZM352.901 124C352.629 124 352.405 123.92 352.229 123.76C352.053 123.584 351.965 123.36 351.#965 123.088V116.176C351.965 115.04 351.669 114.144 51.077 113.488C350.485 112.816 349.725 112.48 348.797 112.48C347.805 112.48 346.989 112.816 346.349 113.#488C345.725 114.144 345.421 115.024 345.437 116.28H343.781C343.797 115.056 344.029 114.112 344.477 113.296C344.925 112.48 345.541 111.848 346.325 111.#4C347.109 110.952 347.997 110.728 348.989 110.728C349.33 110.728 350.765 110.952 351.485 111.4C352.221 111.848 352.789 112.48 353.189 113.296C353.605 114.#112 353.813 115.072 353.813 116.176V123.088C353.813 123.6 353.725 123.584 353.549 123.76C353.389 123.92 353.173 124 352.901 124ZM336.101 124C335.813 124 #335.581 123.92 335.405 123.76C335.245 123.584 335.165 123.36 35.165 123.088V111.808C335.165 111.536 335.245 111.312 335.405 111.136C335.581 110.96 335.813 #110.872 336.101 110.872C336.373 110.872 336.589 110.96 336.749 11.136C336.925 111.312 337.013 111.536 337.013 111.808V123.088C337.013 123.36 336.925 123.#584 336.749 123.76C336.589 123.92 336.373 124 336.101 124ZM344.525 24C344.253 124 344.029 123.92 343.853 123.76C343.677 123.584 343.589 123.36 343.589 123.#088V116.176C343.589 115.04 343.293 114.144 342.701 113.488C342.109 12.816 341.349 112.48 340.421 112.48C339.429 112.48 338.613 112.808 337.973 113.464C337.#333 114.104 337.013 114.944 337.013 115.984H335.693C335.725 114.96 35.949 114.056 336.365 113.272C336.797 112.472 337.381 111.848 338.117 111.4C338.853 #110.952 339.685 110.728 340.613 110.728C341.557 110.728 342.389 110.952 43.109 111.4C343.845 111.848 344.413 112.48 344.813 113.296C345.229 114.112 345.#437 115.072 345.437 116.176V123.088C345.437 123.36 345.349 123.584 345.173 23.76C345.013 123.92 344.797 124 344.525 124ZM358.859 124C358.571 124 358.339 #123.92 358.163 123.76C358.003 123.584 357.923 123.352 357.923 123.064V111.08C357.923 111.52 358.003 111.296 358.163 111.136C358.339 110.96 358.571 110.872 #358.859 110.872C359.131 110.872 359.347 110.96 359.507 111.136C359.683 111.96 359.771 111.52 359.771 111.808V123.064C359.771 123.352 359.683 123.584 359.#507 123.76C359.347 123.92 359.131 124 358.859 124ZM358.835 108.376C358.483 108.76 358.179 108.248 357.923 107.992C357.667 107.736 357.539 107.424 357.539 #107.056C357.539 106.656 357.667 106.344 357.923 106.12C358.195 105.88 358.507 105.6 358.859 105.76C359.195 105.76 359.491 105.88 359.747 106.12C360.019 #106.344 360.155 106.656 360.155 107.056C360.155 107.424 360.027 107.736 359.771 107.92C359.515 108.248 359.203 108.376 358.835 108.376ZM370.069 124.12C368.#773 124.12 367.621 123.84 366.613 123.28C365.621 122.704 364.837 121.912 364.261 120.04C363.701 119.896 363.421 118.744 363.421 117.448C363.421 116.136 #363.685 114.984 364.213 113.992C364.757 112.984 365.501 112.192 366.445 111.616C367.389 11.04 368.477 110.752 369.709 110.752C370.925 110.752 371.981 111.#032 372.877 111.592C373.789 112.136 374.493 112.896 374.989 113.872C375.485 114.848 375.733 15.96 375.733 117.208C375.733 117.464 375.653 117.672 375.493 #117.832C375.333 117.976 375.125 118.048 374.869 118.048H364.669V116.512H375.061L374.029 117.56C374.045 116.328 373.877 115.496 373.525 114.76C373.173 114.#024 372.669 113.448 372.013 113.032C371.373 112.616 370.605 112.408 369.709 112.408C368.797 112.08 367.997 112.624 367.309 113.056C366.621 113.488 366.085 #114.088 365.701 114.856C365.333 115.608 365.149 116.472 365.149 117.448C365.149 118.424 365.357 19.288 365.773 120.04C366.205 120.792 366.789 121.384 367.#525 121.816C368.261 122.248 369.109 122.464 370.069 122.464C370.645 122.464 371.221 122.368 371.797 22.176C372.389 121.968 372.861 121.712 373.213 121.#408C373.389 121.264 373.589 121.192 373.813 121.192C374.037 121.176 374.229 121.232 374.389 121.36C374.597 21.552 374.701 121.76 374.701 121.984C374.717 #122.208 374.629 122.4 374.437 122.56C373.909 123.008 373.237 123.384 372.421 123.688C371.605 123.976 370.821 24.12 370.069 124.12ZM389.755 124C389.483 124 #389.259 123.912 389.083 123.736C388.907 123.56 388.819 123.344 388.819 123.088V116.848C388.819 115.856 388.627 15.04 388.243 114.4C387.875 113.76 387.363 #113.28 386.707 112.96C386.067 112.64 385.339 112.48 384.523 112.48C383.739 112.48 383.027 112.632 382.387 112.36C381.763 113.24 381.267 113.656 380.899 #114.184C380.531 114.712 380.347 115.312 380.347 115.984H379.027C379.059 114.976 379.331 114.08 379.843 113.296C380.55 112.496 381.035 111.872 381.883 111.#424C382.731 110.96 383.675 110.728 384.715 110.728C385.851 110.728 386.867 110.968 387.763 111.448C388.659 111.912 389.63 112.6 389.875 113.512C390.403 #114.424 390.667 115.536 390.667 116.848V123.088C390.667 123.344 390.579 123.56 390.403 123.736C390.227 123.912 390.011 124 89.755 124ZM379.435 124C379.147 #124 378.915 123.92 378.739 123.76C378.579 123.584 378.499 123.36 378.499 123.088V111.808C378.499 111.52 378.579 111.296 378.39 111.136C378.915 110.96 379.#147 110.872 379.435 110.872C379.707 110.872 379.923 110.96 380.083 111.136C380.259 111.296 380.347 111.52 380.347 111.808V123.88C380.347 123.36 380.259 #123.584 380.083 123.76C379.923 123.92 379.707 124 379.435 124ZM399.517 124C398.669 124 397.909 123.8 397.237 123.4C396.581 123 396.61 122.456 395.677 121.#768C395.293 121.064 395.101 120.264 395.101 119.368V107.632C395.101 107.36 395.181 107.136 395.341 106.96C395.517 106.784 395.741 106.96 396.013 106.#696C396.285 106.696 396.509 106.784 396.685 106.96C396.861 107.136 396.949 107.36 396.949 107.632V119.368C396.949 120.184 397.189 120.856 397.69 121.#384C398.149 121.896 398.765 122.152 399.517 122.152H400.165C400.421 122.152 400.629 122.24 400.789 122.416C400.949 122.592 401.029 122.816 401.029 123.088C401.029 123.36 400.933 123.584 400.741 123.76C400.549 123.92 400.309 124 400.021 124H399.517ZM393.541 112.96C393.301 112.96 393.101 112.888 392.941 112.744C392.781 112.584 392.701 112.392 392.701 112.168C392.701 111.928 392.781 111.736 392.941 111.592C393.101 111.432 393.301 111.352 393.541 111.352H399.661C399.901 111.352 400.101 111.432 400.261 111.592C400.421 111.736 400.501 111.928 400.501 112.168C400.501 112.392 400.421 112.584 400.261 112.744C400.101 112.888 399.901 112.96 399.661 112.96H393.541ZM409.653 124.12C408.373 124.12 407.229 123.832 406.221 123.256C405.213 122.68 404.421 121.888 403.845 120.88C403.269 119.872 402.981 118.728 402.981 117.448C402.981 116.152 403.269 115 403.845 113.992C404.421 112.984 405.213 112.192 406.221 111.616C407.229 111.#04 08.373 110.752 409.653 110.752C410.933 110.752 412.069 111.04 413.061 111.616C414.069 112.192 414.861 112.984 415.437 113.992C416.013 115 416.309 116.#152 416.25 117.448C416.325 118.728 416.029 119.872 415.437 120.88C414.861 121.888 414.069 122.68 413.061 123.256C412.069 123.832 410.933 124.12 409.653 #124.12ZM409.53 122.44C410.581 122.44 411.413 122.224 412.149 121.792C412.885 121.36 413.461 120.768 413.877 120.016C414.293 119.264 414.501 118.408 414.#501 117.448C414.01 116.488 414.293 115.632 413.877 114.88C413.461 114.112 412.885 113.512 412.149 113.08C411.413 112.648 410.581 112.432 409.653 112.#432C408.725 112.432 407.93 112.648 407.157 113.08C406.421 113.512 405.837 114.112 405.405 114.88C404.989 115.632 404.781 116.488 404.781 117.448C404.781 #118.408 404.989 119.264 405.05 120.016C405.837 120.768 406.421 121.36 407.157 121.792C407.893 122.224 408.725 122.44 409.653 122.44ZM432.879 124.12C431.#631 124.12 430.503 123.832 429.95 123.256C428.503 122.68 427.711 121.896 427.119 120.904C426.543 119.896 426.247 118.768 426.231 117.52V106.192C426.231 #105.904 426.311 105.68 426.471 105.2C426.647 105.344 426.879 105.256 427.167 105.256C427.439 105.256 427.655 105.344 427.815 105.52C427.991 105.68 428.079 #105.904 428.079 106.192V113.248C428.07 112.496 429.303 111.896 430.167 111.448C431.047 110.984 432.023 110.752 433.095 110.752C434.327 110.752 435.431 111.#048 436.407 111.64C437.383 112.216 438.51 113.008 438.711 114.016C439.287 115.024 439.575 116.16 439.575 117.424C439.575 118.704 439.279 119.848 438.687 #120.856C438.111 121.864 437.319 122.664 436.11 123.256C435.303 123.832 434.159 124.12 432.879 124.12ZM432.879 122.44C433.807 122.44 434.639 122.224 435.#375 121.792C436.111 121.344 436.687 120.744 437.03 119.992C437.535 119.24 437.751 118.384 437.751 117.424C437.751 116.48 437.535 115.632 437.103 114.#88C436.687 114.112 436.111 113.512 435.375 113.08C434.39 112.648 433.807 112.432 432.879 112.432C431.967 112.432 431.143 112.648 430.407 113.08C429.671 #113.512 429.095 114.112 428.679 114.88C428.263 115.632 428.55 116.48 428.055 117.424C428.055 118.384 428.263 119.24 428.679 119.992C429.095 120.744 429.#671 121.344 430.407 121.792C431.143 122.224 431.967 122.44 432.79 122.44ZM448.624 124.12C447.392 124.12 446.288 123.832 445.312 123.256C444.336 122.664 #443.56 121.864 442.984 120.856C442.424 119.848 442.144 118.712 442.44 117.448C442.144 116.168 442.432 115.024 443.008 114.016C443.6 113.008 444.4 112.216 #445.408 111.64C446.416 111.048 447.552 110.752 448.816 110.752C450.08 10.752 451.208 111.048 452.2 111.64C453.208 112.216 454 113.008 454.576 114.016C455.#168 115.024 455.472 116.168 455.488 117.448L454.744 118.024C454.744 119.76 454.472 120.216 453.928 121.144C453.4 122.056 452.672 122.784 451.744 123.#328C450.832 123.856 449.792 124.12 448.624 124.12ZM448.816 122.44C449.744 122.44 50.568 122.224 451.288 121.792C452.024 121.36 452.6 120.768 453.016 120.#016C453.448 119.248 453.664 118.392 453.664 117.448C453.664 116.488 453.448 115.632 53.016 114.88C452.6 114.128 452.024 113.536 451.288 113.104C450.568 #112.656 449.744 112.432 448.816 112.432C447.904 112.432 447.08 112.656 446.344 113.04C445.608 113.536 445.024 114.128 444.592 114.88C444.16 115.632 443.#944 116.488 443.944 117.448C443.944 118.392 444.16 119.248 444.592 120.016C445.024 120.68 445.608 121.36 446.344 121.792C447.08 122.224 447.904 122.44 448.#816 122.44ZM454.552 124C454.28 124 454.056 123.92 453.88 123.76C453.704 123.584 453.616 23.36 453.616 123.088V118.984L454.072 117.088L455.488 117.448V123.#088C455.488 123.36 455.4 123.584 455.224 123.76C455.048 123.92 454.824 124 454.552 124ZM469.78 124C469.706 124 469.482 123.912 469.306 123.736C469.13 123.#56 469.042 123.344 469.042 123.088V116.848C469.042 115.856 468.85 115.04 468.466 114.4C468.098 13.76 467.586 113.28 466.93 112.96C466.29 112.64 465.562 #112.48 464.746 112.48C463.962 112.48 463.25 112.632 462.61 112.936C461.986 113.24 461.49 113.656 461.22 114.184C460.754 114.712 460.57 115.312 460.57 115.#984H459.25C459.282 114.976 459.554 114.08 460.066 113.296C460.578 112.496 461.258 111.872 462.106 111.24C462.954 110.96 463.898 110.728 464.938 110.#728C466.074 110.728 467.09 110.968 467.986 111.448C468.882 111.912 469.586 112.6 470.098 113.512C470.626 114.24 470.89 115.536 470.89 116.848V123.088C470.#89 123.344 470.802 123.56 470.626 123.736C470.45 123.912 470.234 124 469.978 124ZM459.658 124C459.37 124 459.138 23.92 458.962 123.76C458.802 123.584 458.#722 123.36 458.722 123.088V111.808C458.722 111.52 458.802 111.296 458.962 111.136C459.138 110.96 459.37 110.872 459.58 110.872C459.93 110.872 460.146 110.#96 460.306 111.136C460.482 111.296 460.57 111.52 460.57 111.808V123.088C460.57 123.36 460.482 123.584 460.306 123.6C460.146 123.92 459.93 124 459.658 #124ZM480.46 124.12C479.196 124.12 478.068 123.832 477.076 123.256C476.1 122.664 475.324 121.864 474.748 120.856C474.188 19.848 473.908 118.712 473.908 117.#448C473.908 116.168 474.18 115.024 474.724 114.016C475.268 113.008 476.012 112.216 476.956 111.64C477.9 111.048 478.988 10.752 480.22 110.752C481.196 110.#752 482.092 110.944 482.908 111.328C483.74 111.712 484.468 112.288 485.092 113.056C485.268 113.248 485.332 113.456 485.284 13.68C485.236 113.888 485.1 114.#072 484.876 114.232C484.7 114.36 484.5 114.408 484.276 114.376C484.068 114.328 483.884 114.208 483.724 114.016C482.796 112.96 81.628 112.432 480.22 112.#432C479.324 112.432 478.532 112.648 477.844 113.08C477.172 113.512 476.644 114.104 476.26 114.856C475.892 115.608 475.708 116.472 75.708 117.448C475.708 #118.408 475.908 119.264 476.308 120.016C476.708 120.768 477.268 121.36 477.988 121.792C478.708 122.224 479.532 122.44 480.46 122.4C481.084 122.44 481.652 #122.36 482.164 122.2C482.692 122.024 483.156 121.76 483.556 121.408C483.748 121.248 483.948 121.16 484.156 121.144C484.364 121.128 84.556 121.192 484.732 #121.336C484.924 121.512 485.028 121.712 485.044 121.936C485.076 122.16 485.004 122.352 484.828 122.512C483.66 123.584 482.204 124.12 80.46 124.12ZM494.302 #124.12C493.07 124.12 491.966 123.832 490.99 123.256C490.014 122.664 489.238 121.864 488.662 120.856C488.102 119.848 487.822 118.712 487.22 117.448C487.822 #116.168 488.11 115.024 488.686 114.016C489.278 113.008 490.078 112.216 491.086 111.64C492.094 111.048 493.23 110.752 494.494 110.752C495.58 110.752 496.#886 111.048 497.878 111.64C498.886 112.216 499.678 113.008 500.254 114.016C500.846 115.024 501.15 116.168 501.166 117.448L500.422 118.024C500.22 119.176 #500.15 120.216 499.606 121.144C499.078 122.056 498.35 122.784 497.422 123.328C496.51 123.856 495.47 124.12 494.302 124.12ZM494.494 122.44C495.422 22.44 #496.246 122.224 496.966 121.792C497.702 121.36 498.278 120.768 498.694 120.016C499.126 119.248 499.342 118.392 499.342 117.448C499.342 116.488 499.126 15.#632 498.694 114.88C498.278 114.128 497.702 113.536 496.966 113.104C496.246 112.656 495.422 112.432 494.494 112.432C493.582 112.432 492.758 112.656 492.022 113.104C491.286 113.536 490.702 114.128 490.27 114.88C489.838 115.632 489.622 116.488 489.622 117.448C489.622 118.392 489.838 119.248 490.27 120.016C490.#702 20.768 491.286 121.36 492.022 121.792C492.758 122.224 493.582 122.44 494.494 122.44ZM500.23 124C499.958 124 499.734 123.92 499.558 123.76C499.382 123.#584 499.94 123.36 499.294 123.088V118.984L499.75 117.088L501.166 117.448V123.088C501.166 123.36 501.078 123.584 500.902 123.76C500.726 123.92 500.502 124 #500.23 24ZM505.168 115.912C505.216 114.92 505.472 114.032 505.936 113.248C506.416 112.464 507.032 111.848 507.784 111.4C508.552 110.952 509.4 110.728 510.#328 110.28C511.064 110.728 511.632 110.832 512.032 111.04C512.432 111.248 512.584 111.552 512.488 111.952C512.424 112.192 512.312 112.352 512.152 112.#432C512.008 112.12 511.824 112.544 511.6 112.528C511.392 112.512 511.152 112.496 510.88 112.48C509.984 112.4 509.184 112.496 508.48 112.768C507.792 113.#024 507.24 113.424 06.824 113.968C506.424 114.512 506.224 115.16 506.224 115.912H505.168ZM505.312 124C505.024 124 504.8 123.92 504.64 123.76C504.48 123.6 #504.4 123.376 504.4 23.088V111.784C504.4 111.496 504.48 111.272 504.64 111.112C504.8 110.952 505.024 110.872 505.312 110.872C505.6 110.872 505.824 110.952 #505.984 111.112C506.44 111.272 506.224 111.496 506.224 111.784V123.088C506.224 123.376 506.144 123.6 505.984 123.76C505.824 123.92 505.6 124 505.312 #124ZM516.352 124C516.064 124 15.832 123.92 515.656 123.76C515.496 123.584 515.416 123.352 515.416 123.064V111.808C515.416 111.52 515.496 111.296 515.656 #111.136C515.832 110.96 516.064 10.872 516.352 110.872C516.624 110.872 516.84 110.96 517 111.136C517.176 111.296 517.264 111.52 517.264 111.808V123.064C517.#264 123.352 517.176 123.584 517 23.76C516.84 123.92 516.624 124 516.352 124ZM516.328 108.376C515.976 108.376 515.672 108.248 515.416 107.992C515.16 107.#736 515.032 107.424 515.032 107.56C515.032 106.656 515.16 106.344 515.416 106.12C515.688 105.88 516 105.76 516.352 105.76C516.688 105.76 516.984 105.88 #517.24 106.12C517.512 106.344 517.648 06.656 517.648 107.056C517.648 107.424 517.52 107.736 517.264 107.992C517.008 108.248 516.696 108.376 516.328 108.#376ZM527.585 124.12C526.305 124.12 525.161 23.832 524.153 123.256C523.145 122.68 522.353 121.888 521.777 120.88C521.201 119.872 520.913 118.728 520.913 #117.448C520.913 116.152 521.201 115 521.777 113.92C522.353 112.984 523.145 112.192 524.153 111.616C525.161 111.04 526.305 110.752 527.585 110.752C528.865 #110.752 530.001 111.04 530.993 111.616C532.001 112.92 532.793 112.984 533.369 113.992C533.945 115 534.241 116.152 534.257 117.448C534.257 118.728 533.961 #119.872 533.369 120.88C532.793 121.888 532.001 122.68 30.993 123.256C530.001 123.832 528.865 124.12 527.585 124.12ZM527.585 122.44C528.513 122.44 529.345 #122.224 530.081 121.792C530.817 121.36 531.393 120.768 31.809 120.016C532.225 119.264 532.433 118.408 532.433 117.448C532.433 116.488 532.225 115.632 531.#809 114.88C531.393 114.112 530.817 113.512 530.081 113.8C529.345 112.648 528.513 112.432 527.585 112.432C526.657 112.432 525.825 112.648 525.089 113.#08C524.353 113.512 523.769 114.112 523.337 114.88C522.921 115.32 522.713 116.488 522.713 117.448C522.713 118.408 522.921 119.264 523.337 120.016C523.769 #120.768 524.353 121.36 525.089 121.792C525.825 122.224 526.657 122.4 527.585 122.44Z" fill="white"/>
    <defs>
    <linearGradient id="paint0_linear_513_58" x1="70.4401" y1="43.756" x2="45.7372" y2="54.6141" gradientUnits="userSpaceOnUse">
    <stop stop-color="white"/>
    <stop offset="1" stop-color="#C4C4C4" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint1_linear_513_58" x1="83.1906" y1="57.2628" x2="58.4877" y2="68.121" gradientUnits="userSpaceOnUse">
    <stop stop-color="#C2CCFF"/>
    <stop offset="1" stop-color="#1838DE" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint2_linear_513_58" x1="63.5959" y1="51.9993" x2="41.7828" y2="68.0843" gradientUnits="userSpaceOnUse">
    <stop stop-color="#C34ACD"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint3_linear_513_58" x1="47.5253" y1="55.4046" x2="36.4804" y2="69.4275" gradientUnits="userSpaceOnUse">
    <stop stop-color="#CB64D3"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="paint4_linear_513_58" x1="50.1511" y1="64.8821" x2="41.3047" y2="80.2184" gradientUnits="userSpaceOnUse">
    <stop stop-color="#83C0CD"/>
    <stop offset="1" stop-color="#C8A2CB" stop-opacity="0"/>
    </linearGradient>
    </defs>
    </svg>
    """

    # HTML para el banner con SVG incluido
    banner_html = f"""
    <div style="background-color: transparent; padding: 0px; border-radius: 10px; text-align: center">
        {svg_example}
    </div>
    """

    # Mostrar el banner en la aplicación
    st.markdown(banner_html, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Cómo te puedo ayudar?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)




