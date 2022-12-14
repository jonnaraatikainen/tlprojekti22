#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
   Serial.println("Accelerator created!");
}


Accelerator::~Accelerator()
{
   Serial.println("Accelerator deleted!");
}

void Accelerator::makeMeasurement()
{
  m.x = analogRead(xPin);
  m.y = analogRead(yPin);
  m.z = analogRead(zPin);

  //m.x = 258;
  //m.y = 259;
  //m.z = 260;

}
void Accelerator::printMeasurement()
{
      Serial.println(m.x);
      Serial.println(m.y);
      Serial.println(m.z);
}

Measurement Accelerator::getMeasurement()
{
  return m;
}
