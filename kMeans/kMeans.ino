#include "accelerator.h"
#include "keskipisteet.h"

//1=oikeinpäin
//2=yy alaspäin
//3=äx alaspäin
//4=zeta alaspäin



void setup() {
  Serial.begin(19200);
  const int GNDPin2 = A4;  // laitteen maa-napa
  const int VccPin2 = A0;  // Käyttöjännite
  // Kiihtvyys-anturin napojen määrittely:
  pinMode(VccPin2, OUTPUT);  // Kiihtyvyysanturin käyttöjännite Vcc
  pinMode(GNDPin2, OUTPUT);  // Kiihtyvyysanturin GND

  // Asetetaan syöttöjännite (5V UNO-BOARDILLA, 3.3V Genuino 101:llä) ja maa-arvot (0V):
  digitalWrite(VccPin2, HIGH);
  delayMicroseconds(2);
  digitalWrite(GNDPin2, LOW);
  delayMicroseconds(2);

  while (Serial.available() != 0) {
    // Odotellaan että yhteys käynnistyy jos tässä sattuu olemaan viivettä. 0 tarkoittaa että yhteys on.
  }
}

void loop() {
  Accelerator Aobject;
  uint8_t flags = 0;
  Serial.println("Give rotation");
  while (flags == 0) {
    if (Serial.available() > 0) {
      flags = Serial.parseInt();
    }
  }
  Serial.println("Give number how many measurements");
  int NumberOfMeasurements = 0;
  while (NumberOfMeasurements == 0) {
    if (Serial.available() > 0) {
      NumberOfMeasurements = Serial.parseInt();
    }
  }
int flagi = 0;


  for (int M = 0; M < NumberOfMeasurements;) {
    Aobject.makeMeasurement();
    Measurement m = Aobject.getMeasurement();
    float minvalue = 500;
    float dist;

    for (int i = 0; i < 4;){

      dist = abs(sqrt(pow((w[i][0] - m.x), 2) + pow((w[i][1] - m.y), 2) + pow((w[i][2] - m.z), 2)));

        if (dist < minvalue) {
        minvalue = dist;
        flagi = w[i][3];
      }
      i++;
    }
    Serial.print(flags);
    Serial.print(",");
    Serial.println(flagi);


    M++;
  
}  // end of for
}// end of loop
