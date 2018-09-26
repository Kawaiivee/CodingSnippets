#include <Adafruit_MotorShield.h>

//creates motor shield object and motors
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *leftMotor = AFMS.getMotor(3);
Adafruit_DCMotor *rightMotor = AFMS.getMotor(4);
void setup() {
  AFMS.begin();

  //TEST DANCE
  //Do A Little Dance
  leftMotor->setSpeed(255);
  leftMotor->run(BACKWARD);
  delay(250);
  leftMotor->run(FORWARD);
  delay(250);
  leftMotor->run(RELEASE);
  
  //Make A Little Noise
  rightMotor->setSpeed(255);
  rightMotor->run(BACKWARD);
  delay(250);
  rightMotor->run(FORWARD);
  delay(250);
  rightMotor->run(RELEASE);
}

char command = ' ';
void loop() {
  leftMotor->run(FORWARD);
  rightMotor->run(FORWARD);
}
