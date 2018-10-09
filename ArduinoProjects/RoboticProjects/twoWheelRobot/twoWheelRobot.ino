#include <AFMotor.h>
#include <SoftwareSerial.h>

AF_DCMotor LMOTOR(1);
AF_DCMotor RMOTOR(2);

SoftwareSerial BT(9,10);

void setup(){
	BT.begin(9600);
	Serial.begin(9600);
	Serial.println("BT Ready");

	LMOTOR.setSpeed(0);
	RMOTOR.setSpeed(0);

	LMOTOR.run(RELEASE);
	RMOTOR.run(RELEASE);	
}

char c;
void loop(){
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
    case 'L':
      left();
      break;
    case 'R':
      right();
      break;
    case 'S':
      stopped();
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
