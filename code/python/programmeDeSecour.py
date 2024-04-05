# Importation des libraries
from matplotlib import pyplot as plt


# Création du fichier csv
fichier = open("resultats/valeurs.csv", "w")
fichier.truncate()

moniteur_serie = open("code/python/secour.txt", "r")

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
# moy_temperature, moy_pression = 20, 101


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


# Récuperation de toutes les données
for ligne in moniteur_serie.readlines():
    compteur += 1

    fragment = ligne.split(";")  # index des points virgules
    
    # interpretation des nan
    if 'nan' in fragment:
        fragment = [(element if element != 'nan' else 0) for element in fragment]

    # mise à jour des listes
    time.append(compteur)
    thermistance.append(fragment[0])
    potentiometreLineaire.append(fragment[1])
    capteurDistance.append(fragment[2])
    capteurPression.append(fragment[3])
    pressionSenKy052.append(fragment[4])
    temperatureSenKy052.append(fragment[5])
    distanceSenKy052.append(fragment[6])
    
    # Conversion en entier
    thermistance = [float(element) for element in thermistance]
    potentiometreLineaire = [float(element) for element in potentiometreLineaire]
    capteurDistance = [float(element) for element in capteurDistance]
    capteurPression = [float(element) for element in capteurPression]
    temperatureSenKy052 = [float(element) for element in temperatureSenKy052]
    pressionSenKy052 = [float(element) for element in pressionSenKy052]
    distanceSenKy052 = [float(element) for element in distanceSenKy052]

    # écriture sur le fichier csv
    fichier.write(
        f"{compteur};{thermistance[-1]};{potentiometreLineaire[-1]};{capteurDistance[-1]};{capteurPression[-1]};{pressionSenKy052[-1]};{temperatureSenKy052[-1]};{distanceSenKy052[-1]}\n"
    )


# Fermeture du fichier
moniteur_serie.close()
fichier.close()


# Création des graphiques
graph(time, thermistance, "Température (°C)", "Thermistance")
graph(time, potentiometreLineaire, "Potentiometre Lineaire", "Potentiometre linéaire")
graph(time, capteurDistance, "Distance (m)", "Capteur de distance")
graph(time, capteurPression, "Pression (kPa)", "Capteur de pression")
graph(time, pressionSenKy052, "Pression (kPa)", "Capteur de pression SEN-KY052")
graph(time, temperatureSenKy052, "Temperature (°C)", "Capteur de temperature SEN-KY052")
graph(time, distanceSenKy052, "Distance (m)", "Capteur de distance SEN-KY052")
