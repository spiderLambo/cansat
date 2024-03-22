// Importation des librairies
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <Servo.h>

#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11
#define BMP_CS 10

Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);

// Définition des pins
const float pinThermistance = A0;
const float pinPotentiometreLineaire = A1;
const int pinServomoteur = 4;
const uint8_t pinCapteurDistance = 3;
const float pinCapteurPression = A2;

// Variables utiles
float thermistance;
float potentiometreLineaire;
float capteurDistance;
float capteurPression;
float pressionSenKy052;
float temperatureSenKy052;
float distanceSenKy052;
int angleTourn;    // angle que le servomoteur tourne

Servo myservo;  //creation d'un objet pour controller le servomoteur (voir bibliothèque Servo.h)

void setup() {
  // initalistaion des pins
  pinMode(pinCapteurDistance, INPUT);
  
  myservo.attach(pinServomoteur);  // attacher le servomoteur au pin 4 pour l'oject servo
  int angleTour = 90;    // angle que le servomoteur tourne

  Serial.begin(9600); // Ouverture du moniteur série

  if (!bmp.begin()) { // a garder sinon capteur SenSy052 ne fonctionne pas 
  Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
  while (1);
  }

}

void loop() {
 
  // Récupératon des données par les capteurs
  thermistance = - 68.8 + (0.0865*analogRead(pinThermistance));
  potentiometreLineaire = analogRead(pinPotentiometreLineaire);
  capteurDistance = (pulseIn(pinCapteurDistance, HIGH) - 1000) * 2;
  capteurPression = (analogRead(pinCapteurPression)* (5.0 / 1023.0) + 0.04845) / 0.0456;
  pressionSenKy052 = bmp.readPressure();
  temperatureSenKy052 = bmp.readTemperature();
  distanceSenKy052 = bmp.readAltitude(1013.25); // this should be adjusted to your local forcase


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
  Serial.print(distanceSenKy052);
  Serial.println(";");

  delay(1000); // Toutes les secondes
}


void servomoteur(){
    myservo.write(angleTourn);              // tell servo to go to position in variable 'post
  }
