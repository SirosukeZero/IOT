// -------------------------------------------
//
//  Poject: Lab1_task1
//  Group: G
//  Students: Jonas Skolnik en Ryoma Nonaka
//  Date:
//  ------------------------------------------

#include <Arduino_LSM6DS3.h>

#define OFF 0
#define ON 1
#define LED_ON "on"
#define LED_OFF "off"
#define LED_STATUS "status"
#define LED_BLINK "blink"

String status = LED_OFF;

// put your setup code here
void setup() {

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  // initialize serial port and wait for port to open:
  Serial.begin(9600);

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial) {}

  // init digital IO pins
  digitalWrite(LED_BUILTIN, LOW);

}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();

    // BLINK
    if (msg == LED_BLINK) {
      status = LED_BLINK;
      while (true) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
        delay(1000);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
        if (Serial.available() > 0) {
          msg = Serial.readString();

          if(msg == LED_STATUS){
             Serial.println(status);
          }else if (msg != LED_STATUS) {
            break;
          }
        }
      }
    }
    // ON
    if (msg == LED_ON) {
      digitalWrite(LED_BUILTIN, HIGH);
      status = LED_ON;
    }
    // OFF
    if (msg == LED_OFF) {
      digitalWrite(LED_BUILTIN, LOW);
      status = LED_OFF;
    }
    // STATUS
    if(msg == LED_STATUS){
      Serial.println(status);
    }
     
  }
}
