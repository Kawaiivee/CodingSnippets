#include <SoftwareSerial.h>
SoftwareSerial BT(10, 11); 
// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND
void setup(){
  // set digital pin to control as an output
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  
  // set the data rate for the SoftwareSerial port
  BT.begin(9600);
  // Send initial message to other device
  BT.println("Type in: 'r', 'y', 'g', or 'c'");
}

char s; // stores incoming character from other device
void loop(){
  if (BT.available())
  // if text arrived in from BT serial
  {
    s=(BT.read());
    if (s=='r'){
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      BT.println("RED");
    }
    if (s=='y'){
      digitalWrite(5, LOW);
      digitalWrite(6, HIGH);
      digitalWrite(7, LOW);
      BT.println("YELLOW");
    }
    if (s=='g'){
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, HIGH);
      BT.println("GREEN");
    }
    if (s=='c'){
      BT.println("CYCLE");
      for(int i = 0; i < 3; i++){
        allOff();
        digitalWrite(7, HIGH);
        delay(500);
        allOff();
        digitalWrite(6, HIGH);
        delay(500);
        allOff();
        digitalWrite(5, HIGH);
        delay(500);
      }
    if (s=='g'){
      allOff();
      BT.println("GREEN");
    }
    }
  }
}

void allOff(){
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
}

void allOn(){
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
}

