#include <SoftwareSerial.h>
#include <Servo.h>

//At analog A5
Servo servo;

// connect BT module TX to D10
// connect BT module RX to D11
SoftwareSerial BT(10, 11); 

void setup(){
  Serial.begin(9600);
  servo.attach(2);
  BT.begin(9600);
  BT.println("1 = on: 2 = off");
  servo.write(0);
}

char c; // stores incoming character from other device
void loop(){
  if (BT.available()){
    c=(BT.read());
    if(c=='1'){
      BT.println("ON");
      servo.write(180);
      delay(1000);
    }
    if(c=='0'){
      BT.println("OFF");
      servo.write(0);
      delay(1000);
    }
    }
}
