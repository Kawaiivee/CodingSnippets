#include <Servo.h>

#define servoPin 8
Servo myServo;
int pos = 0;
int rangeMin = 0;
int rangeMax = 180;

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo.write(0);
}

void loop() {
  for(pos = rangeMin; pos < rangeMax; pos++){
    myServo.write(pos);
    Serial.println(myServo.read());
    delay(2);
  }

  for(pos = rangeMax; pos > rangeMin; pos--){
    myServo.write(pos);
    Serial.println(myServo.read());
    delay(2);
  }
}
