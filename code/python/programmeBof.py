# Importation des libraries
from pynput.mouse import Controller as mouseC
from pynput.mouse import Button
from pynput.keyboard import Key, Controller
import pygame as pgm
from time import sleep

pgm.init()  # Initialisation de la fenetre
kb = Controller()
ms = mouseC()

# Variables utiles
TAILLE = (300, 0)  # Taille de la fenetre
POSITION_FENETRE = (0, 0)
POSITION_FICHIER = (0, 0)
POSITION_TEXTE = (0, 0)
compteur = 0


def copier(keyboard):
    keyboard.press(Key.shift)
    keyboard.press(Key.down)
    keyboard.release(Key.shift)
    keyboard.release(Key.down)

    keyboard.press(Key.ctrl)
    keyboard.press("c")
    keyboard.release(Key.ctrl)
    keyboard.release("c")


def coller(keyboard):
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release(Key.ctrl)
    keyboard.release("v")


def changer_fenetre(valA, valB, valC, mouse):
    mouse.move(valA[0], valA[1])
    mouse.press(Button.left)
    mouse.release(Button.left)

    mouse.move(valB[0], valB[1])
    mouse.press(Button.left)
    mouse.release(Button.left)

    mouse.move(valC[0], valC[1])
    mouse.press(Button.left)
    mouse.release(Button.left)


# Lancement de la fenetre
screen = pgm.display.set_mode(TAILLE)
run = True


# Récuperation de toutes les données
while run:
    for event in pgm.event.get():
        # Sortir de la boucle
        if event.type == pgm.QUIT or (
            event.type == pgm.KEYDOWN and event.key == pgm.K_s
        ):
            run = False

        # vraiables à changer à chaque tour de la boucle
        copier(kb)
        changer_fenetre(POSITION_TEXTE, POSITION_FENETRE, POSITION_FICHIER, ms)
        coller(kb)
        changer_fenetre(POSITION_FICHIER, POSITION_FENETRE, POSITION_TEXTE, ms)

        compteur += 1

        sleep(1)

pgm.quit()  # Fermeture de la fenetre