# Importation des libraries
from matplotlib import pyplot as plt
import serial

portserie = serial.Serial(
    port="COM4", baudrate=9600, timeout=1
)  # Ouverture du portserie

# Création du fichier csv
fichier = open("valeurs.csv", "w")
fichier.truncate()

# Variables utiles
(
    temps,
    thermistance,
    potentiometreLineaire,
    capteurDistance,
    capteurPression,
    pressionSenKy052,
    temperatureSenKy052,
) = ([], [], [], [], [], [], [])
continuer = True
compteur = 0


def point_virgules(chaine_de_caracteres):
    indices_point_virgules = []
    for i in range(len(donne)):
        if ord(donne[i]) == 59:
            indices_point_virgules.append(j)
    return indices_point_virgules


# Entête du fichier CSV
fichier.write(
    "Temps (en s);Temperature (en *C);Valeur du potentiometre lineaire;Distance (en m);Pression (en kPa);Pression du capteur SEN KY052(en kPa);Temperature du capteur SEN KY052(en *C)\n"
)

# Récuperation de toutes les données
while continuer:
    # vraiables à changer à chaque tour de la boucle
    donnees_arduino = portserie.readline().decode("ascii")
    compteur += 1

    # index des points virgules
    lpv = point_virgules(donnees_arduino)

    # mise à jour des listes
    temps.append(compteur)
    thermistance.append(donnees_arduino[: lpv[0]])
    potentiometreLineaire.append(donnees_arduino[lpv[0] + 1 : lpv[1]])
    capteurDistance.append(donnees_arduino[lpv[1] + 1 : lpv[2]])
    capteurPression.append(donnees_arduino[lpv[2] + 1 : lpv[3]])
    pressionSenKy052.append(donnees_arduino[lpv[3] + 1 : lpv[4]])
    temperatureSenKy052.append(donnees_arduino[lpv[4] + 1 : lpv[5]])
    continuer = bool(int(donne[lpv[5] + 1 :]))

    # écriture sur le fichier csv
    fichier.write(
        f"{compteur};{thermistance[-1]};{potentiometreLineaire[-1]};{capteurDistance[-1]};{capteurPression[-1]};{pressionSenKy052[-1]};{temperatureSenKy052[-1]}\n"
    )


fichier.close()  # Fermeture du fichier

# plt.plot(time, distance, label="Distance")

# plt.legend()
# plt.grid(True)
# plt.show()
