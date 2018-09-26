#include <AFMotor.h>
#include <SoftwareSerial.h>

AF_DCMotor LMOTOR(1);
AF_DCMotor RMOTOR(2);

SoftwareSerial BT(9,10);

void setup(){
	BT.begin(9600);
	Serial.println("BT Ready");

	LMOTOR.setSpeed(0);
	RMOTOR.setSpeed(0);

	LMOTOR.run(RELEASE);
	RMOTOR.run(RELEASE);

	
}

int motorTimer = 100;
int delayTimer = 0;
char c;

void loop(){
	if(BT.available()){
		c = BT.read();
		BT.println(c);
		Serial.println(c);
		selector();
	}
}

void selector(){
	if(c=='F'){
		forward();
	}
	if(c=='B'){
		backward();
	}
	if(c=='L'){
		left();
	}
	if(c=='R'){
		right();
	}
	if(c=='S'){
		stopped();
	}
}

char f = FORWARD;
char b = BACKWARD;
void forward(){
	LMOTOR.run(f);
	RMOTOR.run(f);
	LMOTOR.setSpeed(200);
	RMOTOR.setSpeed(200);
	delay(motorTimer);
}

void backward(){
	LMOTOR.run(b);
	RMOTOR.run(b);
	LMOTOR.setSpeed(200);
	RMOTOR.setSpeed(200);
	delay(motorTimer);
}

void left(){
	LMOTOR.run(b);
	RMOTOR.run(f);
	LMOTOR.setSpeed(127);
	RMOTOR.setSpeed(127);
	delay(motorTimer);
}

void right(){
	LMOTOR.run(f);
	RMOTOR.run(b);
	LMOTOR.setSpeed(127);
	RMOTOR.setSpeed(127);
	delay(motorTimer);
}

void stopped(){
	LMOTOR.run(RELEASE);
	RMOTOR.run(RELEASE);
	LMOTOR.setSpeed(0);
	RMOTOR.setSpeed(0);
	delay(motorTimer);
}
