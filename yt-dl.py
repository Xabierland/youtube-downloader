# Script para descargar videos de youtube

# Librerias

# Para descargar las librerias usar el comando en la terminal: pip install pytube3
# No es necesario instalar la liberia os ya que viene de serie
from pytube import YouTube
import os

# Variables

# Sub-Programas


# Funciones principales
def insert_url():
    print("Insert URL")

def v_dl():
    print("Download video")

def a_dl():
    print("Audio Video")

def all_dl():
    print("Descargar todo")

# Menu Principal
def main():
    print("\t \t       YOUTUBE DOWNLOADER")
    print("\t \t \t by Xabierland")
    print("\n")
    print("\t \t \t MENU DE OPCIONES")
    print("")
    print("\t [1] Introducir URL")
    print("")
    print("\t [2] Descargar video de youtube.")
    print("\t [3] Descargar solo audio de youtube.")
    print("")
    print("\t [4] Descargar tanto video como audio.")
    print("")
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
        v_dl()
    elif option=='3':
        os.system("cls")
        a_dl()
    elif option=='4':
        os.system("cls")
        all_dl()
    elif option=='9':
        os.system("cls")
        print("CREDITOS")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
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