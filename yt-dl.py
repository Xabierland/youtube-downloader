# Script para descargar videos de youtube

# Librerias

# Para descargar las librerias usar el comando en la terminal: pip install pytube3
# No es necesario instalar la liberia os y Path ya que viene de serie
from pytube import YouTube
import os
from pathlib import Path

# Variables
yt=''
path_download=str(os.path.join(Path.home(), "Downloads\\yt-dl"))
try:
    os.mkdir(path_download)
except OSError:
    print("La creación del directorio %s falló" % path_download)
else:
    print("Se ha creado el directorio: %s " % path_download)



#Sub-Programas
def save_url(url):
    # Importamos la variable global
    global yt
    # La guardamos de forma correcta
    yt=("'"+url+"'")


def dl_video(link):
    print(link.streams.filter(file_extension='mp4').get_highest_resolution().download(path_download))

def dl_audio(link):
    print(link.streams.filter(only_audio=True).first().download(path_download))
    # COMBIERTE EL ARCHIVO A MP3
    path_audio_file=str(os.path.join(path_download, link.title + '.mp4'))
    base, ext = os.path.splitext(path_audio_file)
    new_file = base + '.mp3'
    os.rename(path_audio_file, new_file)


# Funciones principales
def insert_url():
    print("Cual es la URL a descargar: ", end="")
    url=input()
    save_url(url)
    global yt
    print("Leyendo URL...")
    yt_main=YouTube(yt)
    print("¿Es este el video que has seleccionado?")
    print(yt_main.title)
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
    global yt
    if yt!='':  
        print("Leyendo URL...")
        yt_main=YouTube(yt)
        print("\t" + yt_main.title)
        print(yt)
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()

def v_dl():
    global yt
    if yt!='':
        print("Leyendo URL...")
        yt_main=YouTube(yt)
        print("Descargando video...")
        dl_video(yt_main)
        print("Video descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()

def a_dl():
    global yt
    if yt!='':
        print("Leyendo URL...")
        yt_main=YouTube(yt)
        print("Descargando audio...")
        dl_audio(yt_main)
        print("Audio descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    
def all_dl():
    global yt
    if yt!='':
        print("Leyendo URL...")
        yt_main=YouTube(yt)
        print("Descargar todo...")
        dl_audio(yt_main)
        print("Audio descargado con exito")
        dl_video(yt_main)
        print("Video descargado con exito")        
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()


# Menu Principal
def main2():
    os.system("cls")

    print("\t \t    YOUTUBE DOWNLOADER v1.0")
    print("\t \t \t by Xabierland")
    print("\n")
    print("\t \t \t MENU DE OPCIONES")
    print("")
    print("\t [1] Introducir URL. [Playlist]")
    print("\t [2] Mostrar URL. [Playlist]")
    print("")
    print("\t [3] Descargar video de youtube. [Playlist]")
    print("\t [4] Descargar solo audio de youtube. [Playlist]")
    print("\t [5] Descargar tanto video como audio. [Playlist]")
    print("")
    print("\t [6] Ant.Pagina")
    print("")
    print("\t [8] Notas del parche.")
    print("\t [9] Proximamente.")
    print("\t [0] Creditos.")
    print("\t [00] Salir.")
    print("\n")
    print("Pagina 2")
    print("")
    print("Opcion", end=": ")
    option=input()

    # Arbol de opciones
    if option=='1':
        os.system("cls")
        insert_url_pl()
    elif option=='2':
        os.system("cls")
        mostrar_url_pl()
    elif option=='3':
        os.system("cls")
        v_dl_pl()
    elif option=='4':
        os.system("cls")
        a_dl_pl()
    elif option=='5':
        os.system("cls")
        all_dl_pl()
    elif option=='6':
        os.system("cls")
        main()
    elif option=='8':
        os.system("cls")
        f= open("changelog.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main2()
    elif option=='9':
        os.system("cls")
        f= open("proximamente.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main2()
    elif option=='0':
        os.system("cls")
        f= open("creditos.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main2()
    elif option=='00':
        os.system("cls")
        exit
    else:
        os.system("cls")
        print("'"+ option + "'" + " no es una opcion valida del menu.")
        main2()

def main():
    os.system("cls")

    print("\t \t    YOUTUBE DOWNLOADER v1.0")
    print("\t \t \t by Xabierland")
    print("\n")
    print("\t \t \t MENU DE OPCIONES")
    print("")
    print("\t [1] Introducir URL")
    print("\t [2] Mostrar URL")
    print("")
    print("\t [3] Descargar video de youtube.")
    print("\t [4] Descargar solo audio de youtube.")
    print("\t [5] Descargar tanto video como audio.")
    print("")
    print("\t [7] Sig.Pagina")
    print("")
    print("\t [8] Notas del parche.")
    print("\t [9] Proximamente.")
    print("\t [0] Creditos.")
    print("\t [00] Salir.")
    print("\n")
    print("Pagina 1")
    print("")
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
    elif option=='7':
        os.system("cls")
        main2()
    elif option=='8':
        os.system("cls")
        f= open("changelog.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    elif option=='9':
        os.system("cls")
        f= open("proximamente.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    elif option=='0':
        os.system("cls")
        f= open("creditos.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        volver=input()
        main()
    elif option=='00':
        os.system("cls")
        exit
    else:
        os.system("cls")
        print("'"+ option + "'" + " no es una opcion valida del menu.")
        main()

# DONDE EMPIEZA LA MAGIA
os.system("cls")
main()