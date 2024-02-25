// Importation des librairies
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

const int BMP_SCK = 13;
const int BMP_MISO = 12;
const int BMP_MOSI = 11;
const int BMP_CS = 10;

Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);


// Définition des pins
const int pinDist = 3;


// Variables utiles
float thermistance;
float potentiometreLineaire;
float capteurDistance;
float capteurPression;
float pressionSenKy052;
float temperatureSenKy052;
int continuer = 1;

void setup() {
  // initalistaion des pins
  pinMode(pinDist, INPUT);

  Serial.begin(9600); // Ouverture du moniteur série

  // code géré par la librairie
  Serial.println(F("BMP280 test"));

  if (!bmp.begin()) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
    while (1);
  }
}

void loop() {
  while(Serial.available()) {
    data = Serial.read();

    switch(data) {
      case 's':
        stopData();
      case 'o':
        servomoteur();
    }

    codePrincipal();
  }
}

void codePrincipal(){
  // Récupératon des données par les capteurs
  thermistance = 68.8 - (0.0865*analogRead(A0));
  potentiometreLineaire = analogRead(A1);
  capteurDistance = digitalRead(pinDist);
  capteurPression = analogRead(A2);
  pressionSenKy052 = bmp.readPressure();
  temperatureSenKy052 = bmp.readTemperature();


  // Affichage des données dans le moniteur série
  // Temperature (en *C);Valeur du potentiometre lineaire;Distance (en m);Pression (en kPa);Pression du capteur SEN KY052(en kPa);Temperature du capteur SEN KY052(en *C);continuer
  Serial.print(thermistance);
  Serial.print(";");
  Serial.print(potentiometreLineaire);
  Serial.print(";");
  Serial.print(capteurDistance);
  Serial.print(";");
  Serial.print(capteurPression);
  Serial.print(";");
  Serial.print(pressionSenKy052);
  Serial.print(";");
  Serial.print(temperatureSenKy052);
  Serial.print(";");
  Serial.println(continuer);

  delay(1000); // Toutes les secondes
}

void stopData(){
  continuer = 0;
}

void servomoteur(){
  // code du servomoteur ici
}
