# Importation des libraries
from matplotlib import pyplot as plt
import serial
import pygame as pgm

portserie = serial.Serial(
    port="COM5", baudrate=9600, timeout=1
)  # Ouverture du portserie
pgm.init()  # Initialisation de la fenetre

# Création du fichier csv
fichier = open("resultats/valeurs.csv", "w")
fichier.truncate()

# Variables utiles
TAILLE = (300, 0)  # Taille de la fenetre
(
    time,
    thermistance,
    potentiometreLineaire,
    capteurDistance,
    capteurPression,
    pressionSenKy052,
    temperatureSenKy052,
    distanceSenKy052,
) = ([], [], [], [], [], [], [], [])
compteur = 0
moy_temperature, moy_pression = 20, 101


# Fonction pour faire un graphique pour chaque grandeur
def graph(temps, grandeur, lab, nom):
    plt.figure(nom)
    plt.plot(temps, grandeur, label=lab)

    plt.legend()
    plt.grid(True)
    plt.show()


# Entête du fichier CSV
fichier.write(
    "Temps (en s);Temperature (en *C);Valeur du potentiometre lineaire;Distance (en m);Pression (en hPa);Pression du capteur SEN KY052(en hPa);Temperature du capteur SEN KY052(en *C);Distance du capteur SEN KY052(en m)\n"
)

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
        donnees_arduino = portserie.readline().decode("ascii")
        print(donnees_arduino)
        compteur += 1

        fragment = donnees_arduino.split(";")  # index des points virgules

        # mise à jour des listes
        time.append(compteur)
        thermistance.append(fragment[0])
        potentiometreLineaire.append(fragment[1])
        capteurDistance.append(fragment[2])
        capteurPression.append(fragment[3])
        pressionSenKy052.append(fragment[4])
        temperatureSenKy052.append(fragment[5])
        distanceSenKy052.append(fragment[6])

        # écriture sur le fichier csv
        fichier.write(
            f"{compteur};{thermistance[-1]};{potentiometreLineaire[-1]};{capteurDistance[-1]};{capteurPression[-1]};{pressionSenKy052[-1]};{temperatureSenKy052[-1]};{distanceSenKy052[-1]}\n"
        )


fichier.close()  # Fermeture du fichier
pgm.quit()  # Fermeture de la fenetre


# Création des graphiques
graph(time, thermistance, "Température (°C)", "Thermistance")
graph(time, potentiometreLineaire, "Potentiometre Lineaire", "Potentiometre linéaire")
graph(time, capteurDistance, "Distance (m)", "Capteur de distance")
graph(time, capteurPression, "Pression (hPa)", "Capteur de pression")
graph(time, pressionSenKy052, "Pression (hPa)", "Capteur de pression SEN-KY052")
graph(time, temperatureSenKy052, "Temperature (°C)", "Capteur de temperature SEN-KY052")
graph(time, distanceSenKy052, "Distance (m)", "Capteur de distance SEN-KY052")
