#include <Servo.h>

Servo servo;
static int opened = 90;
static int closed = 0;

void setup(){
  Serial.begin(9600);
  servo.attach(8);
  pinMode(13, INPUT);
  pinMode(12, INPUT);
  servo.write(closed);
}

void loop(){
  if (digitalRead(13)){
  servo.write(opened);
  }
  else if(digitalRead(12)){
    servo.write(closed);
  }
}
