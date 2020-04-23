# Script para descargar videos de youtube

# Librerias

# Para descargar las librerias usar el comando en la terminal: pip install pytube3
# No es necesario instalar la liberia os y Path ya que viene de serie
from pytube3 import YouTube
import os
from pathlib import Path

# Variables
path_download=str(os.path.join(Path.home(), "Downloads"))

# Funciones principales
def insert_url():
    print("Cual es la URL a descargar: ", end="")
    url=input()
    url=("'"+url+"'")
    yt=YouTube(url)
    print("¿Es este el video que has seleccionado?")
    print(yt.title)
    print("[S/N]", end="")
    opcion=input()
    if opcion=='S' or opcion=='s':
        os.system("cls")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        os.system("cls")
        main()
    elif opcion=='N' or opcion=='n':
        os.system("cls")
        print("Vuelve a introducir la URL")
        insert_url()
    else:
        os.system("cls")
        print("ERROR: Valor introducido erroneo")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        os.system("cls")
        main()    
    
def mostrar_url():
    print(yt)
    print("\n")
    print("Pulsa cualquier tecla para continuar")
    volver=input()
    main()

def v_dl():
    print("Descargando video...")
    print(yt.streams.filter(file_extension='mp4').first().download(path_download))
    print("Video descargado con exito")
    print("Pulsa cualquier tecla para continuar")
    volver=input()
    main()

def a_dl():
    print("Descargando audio...")
    print(yt.streams.filter(only_audio=True).first().download(path_download))
    print("Audio descargado con exito")
    print("Pulsa cualquier tecla para continuar")
    volver=input()
    main()
    
def all_dl():
    print("Descargar todo...")
    print(yt.streams.filter(file_extension='mp4').first().download(path_download))
    print("Video descargado con exito")
    print(yt.streams.filter(only_audio=True).first().download(path_download))
    print("Audio descargado con exito")
    print("Pulsa cualquier tecla para continuar")
    volver=input()
    main()


# Menu Principal
def main():
    #os.system("cls")

    print("\t \t       YOUTUBE DOWNLOADER")
    print("\t \t \t by Xabierland")
    print("\n")
    print("\t \t \t MENU DE OPCIONES")
    print("")
    print("\t [1] Introducir URL")
    print("\t [2] Mostrar URL")
    print("")
    print("\t [3] Descargar video de youtube.")
    print("\t [4] Descargar solo audio de youtube.")
    print("")
    print("\t [5] Descargar tanto video como audio.")
    print("")
    print("\t [8] Proximos cambios.")
    print("\t [9] Creditos.")
    print("\t [0] Salir.")
    print("\n")
    print("Opcion", end=": ")
    
    option=input()
    # Arbol de opciones
    if option=='1':
        os.system("cls")
        insert_url()
    elif option=='2':
        os.system("cls")
        mostrar_url()
    elif option=='3':
        os.system("cls")
        v_dl()
    elif option=='4':
        os.system("cls")
        a_dl()
    elif option=='5':
        os.system("cls")
        all_dl()
    elif option=='8':
        os.system("cls")
        print("CAMBIOS")
        print("")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    elif option=='9':
        os.system("cls")
        print("CREDITOS")
        print("")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    elif option=='0':
        os.system("cls")
        exit
    else:
        os.system("cls")
        print("'"+ option + "'" + " no es una opcion valida del menu.")
        main()

# DONDE EMPIEZA LA MAGIA
os.system("cls")
main()