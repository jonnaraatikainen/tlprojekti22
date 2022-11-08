#include "messaging.h"
#include "accelerator.h"
const int GNDPin2 = A4;  // laitteen maa-napa
const int VccPin2 = A0;  // Käyttöjännite
float ax = 0.0;  // x-kanavan kiihtyvyysarvo SI-muodossa (m/s^2)
float ay = 0.0;
float az = 0.0;
int SisaanTunniste = 0;
int indeksi = 0;

void setup()
{
  Serial.begin(19200);
  // Kiihtvyys-anturin napojen määrittely:
  pinMode(VccPin2, OUTPUT);     // Kiihtyvyysanturin käyttöjännite Vcc
  pinMode(GNDPin2, OUTPUT);     // Kiihtyvyysanturin GND

  // Asetetaan syöttöjännite (5V UNO-BOARDILLA, 3.3V Genuino 101:llä) ja maa-arvot (0V):
  digitalWrite(VccPin2, HIGH);
  delayMicroseconds(2);
  digitalWrite(GNDPin2, LOW);
  delayMicroseconds(2);

  while (Serial.available() != 0)
  {
    // Odotellaan että yhteys käynnistyy jos tässä sattuu olemaan viivettä. 0 tarkoittaa että yhteys on.
  }
}

void loop()
{
  Accelerator Aobject;
  Messaging Mobject;
  Serial.println("Give number how many measurements");
  int NumberOfMeasurements = 0;
  while (NumberOfMeasurements == 0)
  {
    if (Serial.available() > 0)
    {
      NumberOfMeasurements = Serial.parseInt();
    }
  }
 

  for (int M = 0; M < NumberOfMeasurements; M++)
  {
    Aobject.makeMeasurement();
    Measurement m = Aobject.getMeasurement();
    Aobject.printMeasurement();
   
    uint8_t id = M;
    uint8_t flags = 0xff;
    Mobject.createMessage(m);
    if (Mobject.sendMessage(id, flags))
    {
      Serial.println("Successfull transmission");
    }
    else
    {
      Serial.println("Transmission fails");
    }
    if (Mobject.receiveACK())
    {
      Serial.println("Receiver got message, going to next measurement");
    }
    else
    {
      Serial.println("Reciver did not get the message. Need to resend it");
      //M--;  // Let's just revind for loop
    }
  } // end of for
}   // end of loop
