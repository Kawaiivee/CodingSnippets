#include <AFMotor.h>
#include <SoftwareSerial.h>
#include <Servo.h>

AF_DCMotor LMOTOR(1);
AF_DCMotor RMOTOR(2);
Servo servo;

SoftwareSerial BT(A0,A2);

void setup(){
  BT.begin(9600);
  Serial.begin(9600);
  Serial.println("BT Ready");

  servo.attach(10);
  RMOTOR.setSpeed(0);
  LMOTOR.setSpeed(0);
  LMOTOR.run(RELEASE);
  RMOTOR.run(RELEASE);  
}

char c;
void loop(){
  Serial.println(servo.read());
  if(BT.available()){
    c = BT.read();
    selector(c);
  }
  BT.println(c);
  Serial.println(c);
}

void selector(char choice){
  switch(choice){
    case 'F':
      forward();
      break;
    case 'B':
      backward();
      break;
    case 'R':
      right();
      break;
    case 'L':
      left();
      break;
    case 'S':
      stopped();
      break;
    case 'X':
      servo.attach(10);
      servo.write(5);
      delay(200);
      servo.detach();
      break;
    case 'Y':
      servo.attach(10);
      servo.write(175);
      delay(200);
      servo.detach();
      break;
    default:
      stopped();
      break;
  }
}

char f = FORWARD;
char b = BACKWARD;
void forward(){
  LMOTOR.run(f);
  RMOTOR.run(f);
  LMOTOR.setSpeed(200);
  RMOTOR.setSpeed(200);
}

void backward(){
  LMOTOR.run(b);
  RMOTOR.run(b);
  LMOTOR.setSpeed(200);
  RMOTOR.setSpeed(200);
}

void left(){
  LMOTOR.run(b);
  RMOTOR.run(f);
  LMOTOR.setSpeed(127);
  RMOTOR.setSpeed(127);
}

void right(){
  LMOTOR.run(f);
  RMOTOR.run(b);
  LMOTOR.setSpeed(127);
  RMOTOR.setSpeed(127);
}

void stopped(){
  LMOTOR.run(RELEASE);
  RMOTOR.run(RELEASE);
  LMOTOR.setSpeed(0);
  RMOTOR.setSpeed(0);
}
