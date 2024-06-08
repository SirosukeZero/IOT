// -------------------------------------------
//
//  Poject: Lab1_accel
//  Group: G
//  Students: Jonas Skolnik en Ryoma Nonaka
//  Date:
//  ------------------------------------------
#include <Arduino_LSM6DS3.h>

void setup() {
  // initialize serial port and IMU and wait for port to open:
  Serial.begin(9600);
  IMU.begin();

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial) {}

}

void loop() {
  float x,y,z;
  IMU.readAcceleration(x,y,z);
  Serial.print(x);
  Serial.print(", ");
  Serial.print(y);
  Serial.print(", ");
  Serial.println(z);
  delay(100);
}
