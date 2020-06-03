# Script para descargar videos de youtube

#Programa creado el 23/04/2020 por Xabier Gabiña ak.Xabierland
#Mi Github: https://github.com/Xabierland
#Mi Twitter: https://twitter.com/Xabierland
#Mi Instagram: https://www.instagram.com/xabierland/
#Mi Web: https://xabierland.eus/
# Acepto donaciones a traves de PayPal
# https://paypal.me/xabierland/

# Librerias
# Para descargar las librerias usar el comando en la terminal: pip install pytube and pip install pytube3
# No es necesario instalar la liberia os y Path ya que viene de serie
from pytube import YouTube, Playlist
from pathlib import Path
from os import remove, environ
import datetime, time, os

# Variables
yt=''   # URL DE UN SOLO VIDEO
pl=''   # URL DE UNA PLAYLIST
path_download=''
path_download_pl=''

# LOGICA DE ALMACENAMIENTO DE LOS VIDEOS
if os.name == "posix":
    if 'ANDROID_ARGUMENT' in environ:
        path_download=str(os.path.join(Path.home(), "sdcard\\Movies"))
        try:
            os.mkdir(path_download)
        except OSError:
            print("La creacion del directorio %s fallo" % path_download)
        else:
            print("Se ha creado el directorio: %s " % path_download)    
    else:
        path_download=str(os.path.join(Path.home(), "yt-dl"))    # LA CARPETA DONDE SE DESCARGAN
        try:
            os.mkdir(path_download)                                         # PRUEBA A CREAR EL PATH DE DESCARGA
        except OSError:
            print("La creación del directorio %s falló" % path_download)    # SI YA EXISTE SE EJECUTA ESTO
        else:
            print("Se ha creado el directorio: %s " % path_download)        # SI NO EXISTE SE CREA Y SE IMPRIME
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    path_download=str(os.path.join(Path.home(), "Downloads\\yt-dl"))    # LA CARPETA DONDE SE DESCARGAN
    try:
        os.mkdir(path_download)                                         # PRUEBA A CREAR EL PATH DE DESCARGA
    except OSError:
        print("La creación del directorio %s falló" % path_download)    # SI YA EXISTE SE EJECUTA ESTO
    else:
        print("Se ha creado el directorio: %s " % path_download)        # SI NO EXISTE SE CREA Y SE IMPRIME
else:
    print("ERROR. No se ha detectado un sistema operativo valido")
    exit
#Sub-Programas
def carpeta_pl(nombre):
    global path_download, path_download_pl
    path_download_pl=str(os.path.join(path_download, nombre))    # LA CARPETA DONDE SE DESCARGAN
    try:
        os.mkdir(path_download_pl)                                         # PRUEBA A CREAR EL PATH DE DESCARGA
    except OSError:
        print("La carpeta ya existe")    # SI YA EXISTE SE EJECUTA ESTO
    else:
        print("Se ha creado el directorio: %s " % path_download_pl)        # SI NO EXISTE SE CREA Y SE IMPRIME
    
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def save_url(url):
    # Importamos la variable global
    global yt
    # La guardamos de forma correcta
    yt=("'"+url+"'")

def save_url_pl(url):
    # Importamos la variable global
    global pl
    # La guardamos de forma correcta
    pl=(url)

def dl_video(link, is_pl,i):     # Descarga el video con mejor calidad
    x = datetime.datetime.now()   # GUARDA LA VARIABLE A LA HORA DE DESCARGAR
    x = str(x.strftime(" %Y-%m-%d %H-%M-%S"))
    

    if i!=0:
        i=str(i)
        name ="[" + i + "] " + str(link.title) + " " + x    # Pone la fecha, hora y posicion de la descarga
    else:
        name = str(link.title) + " " + x    # Pone la fecha y hora de descarga
    
    
    if not is_pl:
        global path_download
        try:
            output=link.streams.filter(file_extension='mp4').get_highest_resolution().download(path_download, name)
        except:
            print("Parece que ha ocurrido un error al descargar el video %s", link.title)
            remove(output)  # Borra el video erroneo
            print("Reiniciando descarga")
            # Volver a descargar
            try:
                link.streams.filter(file_extension='mp4').get_highest_resolution().download(path_download, name)
            except:
                print("Parece que el error se ha vuelto a repetir")
                print("Comprueba el link: %s", str(link))
    else:   # Si es una playlist lo guarda en una carpeta con el nombre de la playlist
        global path_download_pl
        try:
            output=link.streams.filter(file_extension='mp4').get_highest_resolution().download(path_download_pl, name)
        except:
            print("Parece que ha ocurrido un error al descargar el video %s", link.title)
            remove(output)  # Borra el video erroneo
            print("Reiniciando descarga")
            # Volver a descargar
            try:
                link.streams.filter(file_extension='mp4').get_highest_resolution().download(path_download_pl, name)
            except:
                print("Parece que el error se ha vuelto a repetir")
                print("Comprueba el link: %s", str(link))


def dl_audio(link, is_pl,i):     # Descarga el audio del video
    x = datetime.datetime.now()    # GUARDA LA VARIABLE A LA HORA DE DESCARGAR
    x = str(x.strftime(" %Y-%m-%d %H-%M-%S"))
    
    if i!=0:
        i=str(i)
        name ="[" + i + "]" + str(link.title) + " " + x    # Pone la fecha, hora y posicion de la descarga
    else:
        name = str(link.title) + " " + x    # Pone la fecha y hora de descarga
    
    if not is_pl:
        try:
            output=(link.streams.filter(only_audio=True).first().download(path_download, name)) # Descarga el audio con el nombre indicado en la linea de arriba y guarda la direccion de guardado en la variable ouput
        except:
            print("Parece que ha ocurrido un error al descargar el video %s", link.title)
            remove(output)  # Borra el video erroneo
            print("Reiniciando descarga")
            # Volver a descargar
            try:
                output=(link.streams.filter(only_audio=True).first().download(path_download, name))
            except:
                print("Parece que el error se ha vuelto a repetir")
                print("Comprueba el link: %s", str(link))
        # CONVIERTE EL ARCHIVO DE MP4 A MP3
        base, ext = os.path.splitext(output)    # Divide la ruta de guardado en lo que es la base, es decir, el path y el nombre del file y por otro lado la extension, en este caso, mp4
        if ext!="":
            new_file = base  + '.mp3'               # Sustituye la extension mp4 a mp3
            os.rename(output, new_file)             # Efectua el cambio de nombre
    else:
        global path_download_pl
        try:
            output=(link.streams.filter(only_audio=True).first().download(path_download_pl, name)) # Descarga el audio con el nombre indicado en la linea de arriba y guarda la direccion de guardado en la variable ouput
        except:
            print("Parece que ha ocurrido un error al descargar el video %s", link.title)
            remove(output)  # Borra el video erroneo
            print("Reiniciando descarga")
            # Volver a descargar
            try:
                output=(link.streams.filter(only_audio=True).first().download(path_download_pl, name))
            except:
                print("Parece que el error se ha vuelto a repetir")
                print("Comprueba el link: %s", str(link))
        # CONVIERTE EL ARCHIVO DE MP4 A MP3
        base, ext = os.path.splitext(output)    # Divide la ruta de guardado en lo que es la base, es decir, el path y el nombre del file y por otro lado la extension, en este caso, mp4
        if ext!="":
            new_file = base  + '.mp3'               # Sustituye la extension mp4 a mp3
            os.rename(output, new_file)             # Efectua el cambio de nombre


# Funciones principales
# LAS FUNCIONES DEL MAIN
def insert_url():
    print("Cual es la URL a descargar: ", end="")
    url=input()
    save_url(url)   # Guarda la URL en la variable global
    global yt   # Importa la variable que almacena la URL del video como srt
    print("Leyendo URL...")
    try:    # Comprueba que al realizar el polimorfismo no salte error
        yt_main=YouTube(yt)     # Hace un polimorfismo y cambia yt de srt a la clase YouTube
    except: # En caso de saltar se volvera al menu
        yt=''
        print("ERROR: LA URL INTRODUCIDA NO ES VALIDA")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    # Si no salta ningun error se leera el codigo debajo de este comentario.
    print("¿Es este el video que has seleccionado?")
    print(yt_main.title)    # Imprime el titulo del video
    print("[S/N]", end="")
    opcion=input()
    if opcion=='S' or opcion=='s':      # La URL ya se ha guardado y vuelves al menu principal
        borrarPantalla()
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    elif opcion=='N' or opcion=='n':    # En caso de que se hayan equivocado en la URL, borra la anterior y vuelve a ejecutar lo de introducir la URL
        borrarPantalla()
        yt=''   # Borra la URL introducida anteriormente
        print("Vuelve a introducir la URL")
        insert_url()
    else:       # En caso de introducir una opcion no contemplada vuelve al menu principal
        borrarPantalla()
        print("ERROR: Valor introducido erroneo")
        yt=''   # Borra la URL introducida anteriormente
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()

def mostrar_url():  # Muetra el titulo y la url del video
    global yt   # Importa la variable que almacena la URL del video como srt
    if yt!='':  # Comprueba que antes se haya introducido una URL
        print("Leyendo URL...")
        yt_main=YouTube(yt) # Hace el polimorfismo
        print("\t" + yt_main.title) # Imprime el titutlo
        print(yt)   # Imprime la URL
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal
    else:           # Si no se ha introducido la URL
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal

def v_dl():
    global yt   # Importa la variable que almacena la URL del video como srt
    if yt!='':  # Comprueba que antes se haya introducido una URL
        print("Leyendo URL...")
        yt_main=YouTube(yt) # Hace el polimorfismo
        print("Descargando video...")
        dl_video(yt_main, False, 0)   # Llama a la funcion encargada de decargar el video
        print("Video descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal
def a_dl():
    global yt   # Importa la variable que almacena la URL del video como srt
    if yt!='':  # Comprueba que antes se haya introducido una URL
        print("Leyendo URL...")
        yt_main=YouTube(yt) # Hace el polimorfismo
        print("Descargando audio...")
        dl_audio(yt_main, False, 0)   # Llama a la funcion encargada de decargar el audio
        print("Audio descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal 
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal  
    
def all_dl():
    global yt   # Importa la variable que almacena la URL del video como srt
    if yt!='':  # Comprueba que antes se haya introducido una URL
        print("Leyendo URL...")
        yt_main=YouTube(yt) # Hace el polimorfismo
        print("Descargando todo...")
        dl_audio(yt_main, False, 0)   # Llama a la funcion encargada de decargar el audio
        print("Audio descargado con exito")
        dl_video(yt_main, False, 0)   # Llama a la funcion encargada de decargar el video
        print("Video descargado con exito")        
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()  # Vuelve al menu principal












#=====================================================================================================================================================================================================================
                                                                                        # LAS FUNCIONES DEL MAIN2
def insert_url_pl():
    print("Cual es la URL a descargar: ", end="")
    url=input()
    save_url_pl(url)   # Guarda la URL en la variable global
    global pl   # Importa la variable que almacena la URL del video como srt
    print("Leyendo URL...")
    try:    # Comprueba que al realizar el polimorfismo no salte error
        pl_main=Playlist(pl)     # Hace un polimorfismo y cambia yt de srt a la clase YouTube
    except: # En caso de saltar se volvera al menu
        pl=''
        print("ERROR: LA URL INTRODUCIDA NO ES VALIDA")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    # Si no salta ningun error se leera el codigo debajo de este comentario.
    print("¿Es esta la playlist que has seleccionado?")
    print(pl_main.title())    # Imprime el titulo del video
    print("[S/N]", end="")
    opcion=input()
    if opcion=='S' or opcion=='s':      # La URL ya se ha guardado y vuelves al menu principal
        borrarPantalla()
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()
    elif opcion=='N' or opcion=='n':    # En caso de que se hayan equivocado en la URL, borra la anterior y vuelve a ejecutar lo de introducir la URL
        borrarPantalla()
        pl=''   # Borra la URL introducida anteriormente
        print("Vuelve a introducir la URL")
        insert_url_pl()
    else:       # En caso de introducir una opcion no contemplada vuelve al menu principal
        borrarPantalla()
        print("ERROR: Valor introducido erroneo")
        pl=''   # Borra la URL introducida anteriormente
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()

def mostrar_url_pl():
    global pl   # Importa la variable que almacena la URL del video como srt
    if pl!='':  # Comprueba que antes se haya introducido una URL
        print("Leyendo URL...")
        pl_main=Playlist(pl) # Hace el polimorfismo
        print("\t" + pl_main.title) # Imprime el titutlo
        print(pl)   # Imprime la URL
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal
    else:           # Si no se ha introducido la URL
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal

def v_dl_pl():
    global pl   # Importa la variable que almacena la URL del video como srt
    if pl!='':  # Comprueba que antes se haya introducido una URL
        i=1
        print("Leyendo URLs...")
        pl_main=Playlist(pl) # Hace el polimorfismo
        carpeta_pl(pl_main.title())
        print("Descargando videos...")
        for yt in pl_main:
            yt_main=YouTube(yt)
            dl_video(yt_main, True, i)   # Llama a la funcion encargada de decargar el video
            i+=1
        print("Videos descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal

def a_dl_pl():
    global pl   # Importa la variable que almacena la URL del video como srt
    if pl!='':  # Comprueba que antes se haya introducido una URL
        i=1
        print("Leyendo URLs...")
        pl_main=Playlist(pl) # Hace el polimorfismo
        carpeta_pl(pl_main.title())
        print("Descargando audios...")
        for yt in pl_main:
            yt_main=YouTube(yt)
            dl_audio(yt_main, True, i)   # Llama a la funcion encargada de decargar el audio
            i+=1
        print("Audios descargado con exito")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal 
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal  

def all_dl_pl():
    global pl   # Importa la variable que almacena la URL del video como srt
    if pl!='':  # Comprueba que antes se haya introducido una URL
        i=1
        print("Leyendo URLs...")
        pl_main=Playlist(pl) # Hace el polimorfismo
        carpeta_pl(pl_main.title())
        print("Descargando todo...")
        for yt in pl_main:
            yt_main=YouTube(yt)
            dl_audio(yt_main, True, i)   # Llama a la funcion encargada de decargar el audio
            dl_video(yt_main, True, i)   # Llama a la funcion encargada de decargar el video
            i+=1
        print("Videos y audios descargados con exito")        
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal
    else:
        print("ERROR: Introduce antes una URL")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()  # Vuelve al menu principal



















# ====================================================================================================================================================================================================================
# =====================================================================================Menu Principal=================================================================================================================
# ====================================================================================================================================================================================================================
def main2():
    f= open("title.txt","r", encoding="utf8")   # Using https://textfancy.com/
    print(f.read())
    print("\t\t\t\t\t by Xabierland")
    print("\n")
    print("\t\t\t\t\tMENU DE OPCIONES")
    print("\n")
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
    print("\t [7] Notas del parche.")
    print("\t [8] Proximamente.")
    print("\t [9] Creditos.")
    print("\t [0] Salir.")
    print("\n")
    print("Pagina 2")
    print("")
    print("Opcion", end=": ")
    option=input()

    # Arbol de opciones
    if option=='1':
        borrarPantalla()
        insert_url_pl()
    elif option=='2':
        borrarPantalla()
        mostrar_url_pl()
    elif option=='3':
        borrarPantalla()
        v_dl_pl()
    elif option=='4':
        borrarPantalla()
        a_dl_pl()
    elif option=='5':
        borrarPantalla()
        all_dl_pl()
    elif option=='6':
        borrarPantalla()
        borrarPantalla()
        main()
    elif option=='7':
        borrarPantalla()
        f= open("changelog.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()
    elif option=='8':
        borrarPantalla()
        f= open("proximamente.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()
    elif option=='9':
        borrarPantalla()
        f= open("creditos.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main2()
    elif option=='0':
        borrarPantalla()
        exit
    else:
        borrarPantalla()
        print("'"+ option + "'" + " no es una opcion valida del menu.")
        borrarPantalla()
        main2()

def main():
    f= open("title.txt","r", encoding="utf8")
    print(f.read())
    print("\t\t\t\t\t by Xabierland")
    print("\n")
    print("\t\t\t\t\tMENU DE OPCIONES")
    print("")
    print("\t [1] Introducir URL")
    print("\t [2] Mostrar URL")
    print("")
    print("\t [3] Descargar video de youtube.")
    print("\t [4] Descargar solo audio de youtube.")
    print("\t [5] Descargar tanto video como audio.")
    print("")
    print("\t [6] Sig.Pagina")
    print("")
    print("\t [7] Notas del parche.")
    print("\t [8] Proximamente.")
    print("\t [9] Creditos.")
    print("\t [0] Salir.")
    print("\n")
    print("Pagina 1")
    print("")
    print("Opcion", end=": ")
    
    option=input()
    # Arbol de opciones
    if option=='1':
        borrarPantalla()
        insert_url()
    elif option=='2':
        borrarPantalla()
        mostrar_url()
    elif option=='3':
        borrarPantalla()
        v_dl()
    elif option=='4':
        borrarPantalla()
        a_dl()
    elif option=='5':
        borrarPantalla()
        all_dl()
    elif option=='6':
        borrarPantalla()
        borrarPantalla()
        main2()
    elif option=='7':
        borrarPantalla()
        f= open("changelog.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    elif option=='8':
        borrarPantalla()
        f= open("proximamente.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    elif option=='9':
        borrarPantalla()
        f= open("creditos.txt","r")
        print(f.read())
        print("\n")
        print("Pulsa cualquier tecla para continuar")
        input()
        borrarPantalla()
        main()
    elif option=='0':
        borrarPantalla()
        exit
    else:
        borrarPantalla()
        print("'"+ option + "'" + " no es una opcion valida del menu.")
        borrarPantalla()
        main()

# DONDE EMPIEZA LA MAGIA
borrarPantalla()
main()