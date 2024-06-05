// -------------------------------------------
//
//  Poject: Lab1_task1
//  Group: G
//  Students: Jonas Skolnik en Ryoma Nonaka
//  Date:
//  ------------------------------------------

#define OFF 0
#define ON 1

String status = "off";

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


// put your main code here
void loop() {
  
  if (Serial.available() > 0) {
    String msg = Serial.readString();

    if (msg == "blink") {
      status = "blink";
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

          if(msg == "status"){
             Serial.println(status);
          }else if (msg != "blink") {
            break;
          }
        }
      }
    }

    if (msg == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
      status = "on";
    }

    if (msg == "off") {
      digitalWrite(LED_BUILTIN, LOW);
      status = "off";
    }

    if(msg == "status"){
      Serial.println(status);
    }
     
  }
}
