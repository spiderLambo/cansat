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
const int led = 5;

// Variables utiles
float thermistance;
float potentiometreLineaire;
float capteurDistance = 0;
float capteurPression;
float pressionSenKy052;
float temperatureSenKy052;
float distanceSenKy052;
int angleTourn = 180;    // angle que le servomoteur tourne
int deltaltitude;
int atterissage;  //pour savoir si le CanSat a attérit
Servo myservo;  //creation d'un objet pour controller le servomoteur (voir bibliothèque Servo.h)

void setup() {
  // initalistaion des pins
  pinMode(pinCapteurDistance, INPUT);
  digitalWrite(led, HIGH) ; //allumage led
  pinMode(pinThermistance, INPUT);
  digitalWrite(pinThermistance, HIGH);
  
  myservo.attach(pinServomoteur);  // attacher le servomoteur au pin 4 pour l'oject servo
  myservo.write(0); 

  Serial.begin(9600); // Ouverture du moniteur série

if (!bmp.begin()) { // a garder sinon capteur SenSy052 ne fonctionne pas 
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring!"));
    while (1);
  }  
  
int16_t capteurDistance = (pulseIn(pinCapteurDistance, HIGH) - 1000) * 4;
while (capteurDistance < 0){
  digitalWrite(led, LOW) ;
  delay(500);
  digitalWrite(led, HIGH) ;
  delay(500);
  capteurDistance = (pulseIn(pinCapteurDistance, HIGH) - 1000) * 4;
}
  
}

void loop() {

  // Récupératon des données par les capteurs
  thermistance = 135 + (analogRead(pinThermistance)*-0.417);
  potentiometreLineaire = -analogRead(pinPotentiometreLineaire)*0.0703+29,6;
  int16_t capteurDistance = (pulseIn(pinCapteurDistance, HIGH) - 1000) * 4;
  capteurPression = (((analogRead(pinCapteurPression) * (5.1 / 1023.0))/5)+ 0.095)/0.0009;
  pressionSenKy052 =  bmp.readPressure()*pow(10,-2)+10;
  temperatureSenKy052 = bmp.readTemperature(); 
  distanceSenKy052 = bmp.readAltitude(1013.25); // this should be adjusted to your local forcase


  // Affichage des données dans le moniteur série
  // Temperature (en *C);Valeur du potentiometre lineaire;Distance (en m);Pression (en hPa);Pression du capteur SEN KY052(en kPa);Temperature du capteur SEN KY052(en *C);Distance du capteur SEN KY052(en m)
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
  Serial.println(distanceSenKy052);

  delay(1000); // Toutes les secondes

// activation de servomoteur
  deltaltitude = bmp.readAltitude(1013.25) - 86;  //mettre l'altidude du sol sur lequel on doit atterir
 if (deltaltitude  < 5) {
  atterissage = atterissage+1;
 }
 if (atterissage == 15) {
  myservo.write(angleTourn);              // tell servo to go to position in variable 'post
  atterissage = -500;
 }
}
