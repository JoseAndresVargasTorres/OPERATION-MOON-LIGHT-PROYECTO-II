#Operation moon light
from QuickSort import *
import pygame, sys, random, vlc
from pygame import mixer
from pygame.locals import*

# Inicio el juego.
pygame.init()


# Defino el control de audio del juego, esta es una función de pygame que permite establecer las frecuencias, canales,
# profundidad de bits y el buffer del audio que vamos a reproducir, los valores los están asignado por defecto.
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#De una vez pongo a correr la mùsica principal y la voy parando cada vez que entra a un nivel
menu_principal = vlc.MediaPlayer("canciones\pantallainicio.mp3")

nivel_1= vlc.MediaPlayer("canciones/nivel1.mp3")
nivel_2= vlc.MediaPlayer("canciones/nivel2.mp3")
nivel_3 = vlc.MediaPlayer("canciones/nivel3.mp3")
#José Andrés Configuró los sonidos

# Cargo los efectos de sonido a una variable y les reducí el sonido a un volumen agradable.
explosion1_efecto = pygame.mixer.Sound(f"efectos\explosion2.mp3")
explosion1_efecto.set_volume(0.25)
explosion2_efecto = pygame.mixer.Sound(f"efectos\explosion2.mp3")
explosion2_efecto.set_volume(0.25)
contacto_efecto = pygame.mixer.Sound(f"efectos\contacto1.mp3")
contacto_efecto.set_volume(0.25)
contacto2_efecto = pygame.mixer.Sound(f"efectos\contacto2.mp3")
contacto2_efecto.set_volume(0.25)
def colision(x):
    pared_efecto = pygame.mixer.Sound(f"efectos\p" + str(x) + ".wav")
    pared_efecto.set_volume(0.16)
    pared_efecto.play()


# Defino la velocidad de actualizacion de la ventana, pygame.time.Clock() me crea una especie de objeto o reloj que limita los cuadros por segundo de actualización de la ventana al numero que se le ingrese.
# Mi variable fps significa fotogramas por segundo y luego va ser la encargada de limitar el anteriormente mencionado Clock a 60 fotogramas por segundo.
actualizacion = pygame.time.Clock()
fps = 60
niveles = False


# Defino la ventana, creo un ancho y un alto para luego crear una variable llamada ventana, la cual con la función pygame.display.set_mode se convierte en una ventana de pygame
ventana_ancho = 600
ventana_alto = 800
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
# Con pygame.display.set_caption le asigno un nombre a la barra superior de la ventana anteriormente creada.
pygame.display.set_caption("Operation Moon Light")


# A las siguientes variables les asigné una imagen la cual luego voy a estar utilizando para pintar el fondo de las diferentes pantallas.
fondo = pygame.image.load("img\pondo.jpg")
fondo_complementaria = pygame.image.load("img\pondo_comp.jpg")
fondo_puntajes = pygame.image.load("img\pondo_punt.jpg")


# Las siguientes variables corresponden a textos en forma de imagen que luego estaré utilizando para pintarlas de en pantalla de manera que queden como títulos.
titulo = pygame.image.load("img\ditulos\ditulo.png")
titulo_comp = pygame.image.load("img\ditulos\dituloi.png")
titulo_punt = pygame.image.load("img\ditulos\ditulop.png")


# En las siguientes variables defino unas fuentes que luego voy a utilizar. La variable pygame.font.Font hace referencia a retornar una fuente de letra con un tamaño asignable.
fuente_base = pygame.font.Font(None, 32)
fuente20 = pygame.font.SysFont("Rockwell", 20)
fuente30 = pygame.font.SysFont("Constantia", 30)
fuente40 = pygame.font.SysFont("Rockwell", 40)


# Estas funciones son las que se encargan de pintar el fondo y los titulos una vez que la funcion sea llamada.
def dibujar_fondo_p(x):
    fondolvl = pygame.image.load("img/pondos/principal/frame_" + str(x) + "_delay-0.04s.gif")
    ventana.blit(fondolvl, (0,0))
def dibujar_fondo2():
    ventana.blit(fondo_complementaria, (0,0))
def dibujar_fondo3():
    ventana.blit(fondo_puntajes, (0,0))
def dibujar_titulo():
    ventana.blit(titulo, (ventana_ancho/2 - 128, 10))
def dibujar_titulo_comp():
    ventana.blit(titulo_comp, (ventana_ancho/2 - 150, 20))
def dibujar_titulo_punt():
    ventana.blit(titulo_punt, (ventana_ancho/2 - 122, 20))
def dibujar_lvl1(x):
    fondolvl = pygame.image.load("img/pondos/pondolvl1/" + str(x) + ".gif")
    ventana.blit(fondolvl, (0,0))
def dibujar_lvl2(x):
    fondolvl = pygame.image.load("img/pondos/pondolvl2/frame_" + str(x) + "_delay-0.03s.gif")
    ventana.blit(fondolvl, (0,0))
def dibujar_lvl3(x):
    fondolvl = pygame.image.load("img/pondos/pondolvl3/frame_" + str(x) + "_delay-0.04s.gif")
    ventana.blit(fondolvl, (0,0))


# A las siguiente variables les asigne un color el cual hace referencia al nombre de la variable.
rojo = (255, 0, 0)
verde = (0, 255, 0)
blanco = (255, 255, 255)
amarillo_verde = (150, 255, 0)
amarillo = (255, 220, 0)
rojo_amarillento = (255, 120, 0)

