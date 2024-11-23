import subprocess
import os

def compilar():
    # Ruta al archivo .java
    #java_file = "ruta/al/archivo.java"

    # Obtener la ruta del directorio actual
    #current_directory = os.getcwd()
#
    #print("Ruta del proyecto:", current_directory)
#
#
    #print(java_file)
#
    #ruta_completa = current_directory + "\\" + java_file.replace("/", "\\" )
    #ruta_completa = ruta_completa.replace("\\", "/")
    #print("RATA: " + ruta_completa.replace("\\", "/"))
    # Comando para compilar el archivo .java
    #command = ["javac", "C:\\Users\\SURAMERICANA\\PycharmProjects\\asoAsistantv2\\ccol_calculate-incomes\\facade\\v0\\dto\\InformationSources.java"]

    # Ejecutar el comando
    #result = subprocess.run(command, capture_output=True, text=True)

    # Imprimir la salida del comando
    #print(result.stdout)
    #print(result.stderr)

    # Ruta al archivo .bat
    bat_file = "/workspaces/chatbot/install.sh"
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


