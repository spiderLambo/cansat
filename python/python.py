# Importation des libraries
from matplotlib import pyplot as plt
import serial
import pygame as pgm

portserie = serial.Serial(
    port="COM4", baudrate=9600, timeout=1
)  # Ouverture du portserie
pgm.init()  # Initialisation de la fenetre

# Création du fichier csv
fichier = open("valeurs.csv", "w")
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
    "Temps (en s);Temperature (en *C);Valeur du potentiometre lineaire;Distance (en m);Pression (en kPa);Pression du capteur SEN KY052(en kPa);Temperature du capteur SEN KY052(en *C);Distance du capteur SEN KY052(en m)\n"
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

        # messages d'erreur
        # moy_temperature = (temperatureSenKy052[-1] + thermistance[-1]) / 2
        # if moy_temperature < 0 or moy_temperature > 85:
        #     print(
        #         "Erreur 1.1 : capteurs hors du seuil de fonctionnement car la température est de",
        #         moy_temperature,
        #     )
        # if moy_temperature < -19 or moy_temperature > 70:
        #     print(
        #         "Erreur 1.2 : antenne hors du seuil de fonctionnement car la température est de",
        #         moy_temperature,
        #     )
        # moy_pression = (capteurPression[-1] + pressionSenKy052[-1]) / 2
        # if moy_pression < 30 or moy_pression > 110:
        #     print(
        #         "Erreur 2.1 : capteur BMP280 KY052 hors du seuil de fonctionnement car la pression est de",
        #         moy_pression,
        #     )
        # if moy_pression < 15 or moy_pression > 115:
        #     print(
        #         "Erreur 2.2 : capteur MPX4115 hors du seuil de fonctionnement car la pression est de",
        #         moy_pression,
        #     )


fichier.close()  # Fermeture du fichier
pgm.quit()  # Fermeture de la fenetre


# Création des graphiques
graph(time, thermistance, "Température (°C)", "Thermistance")
graph(time, potentiometreLineaire, "Potentiometre Lineaire", "Potentiometre linéaire")
graph(time, capteurDistance, "Distance (m)", "Capteur de distance")
graph(time, capteurPression, "Pression (kPa)", "Capteur de pression")
graph(time, pressionSenKy052, "Pression (kPa)", "Capteur de pression SEN-KY052")
graph(time, temperatureSenKy052, "Temperature (°C)", "Capteur de temperature SEN-KY052")
graph(time, distanceSenKy052, "Distance (m)", "Capteur de distance SEN-KY052")
