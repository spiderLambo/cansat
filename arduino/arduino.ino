// Importation des librairies
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <Servo.h>

Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);


// Définition des pins
const float pinThermistance = A0;
const float pinPotentiometreLineaire = A1;
const int pinServomoteur = 4;
const int pinCapteurDistance = 3;
const float pinCapteurPression = A2;


// Variables utiles
float thermistance;
float potentiometreLineaire;
float capteurDistance;
float capteurPression;
float pressionSenKy052;
float temperatureSenKy052;
int continuer = 1;
int data;
int pos;

Servo myservo;  // create servo object to control a servo

void setup() {
  // initalistaion des pins
  pinMode(pinCapteurDistance, INPUT);
  
  myservo.attach(pinServomoteur);  // attaches the servo on pin 4 to the servo object
  int pos = 0;    // variable to store the servo position

  Serial.begin(9600); // Ouverture du moniteur série

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
  thermistance = 68.8 - (0.0865*analogRead(pinThermistance));
  potentiometreLineaire = analogRead(pinPotentiometreLineaire);
  capteurDistance = digitalRead(pinCapteurDistance);
  capteurPression = analogRead(pinCapteurPression);
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
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
