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

int motorTimer = 100;
char c;
char lastc;

//found android 'Arduino Bluetooth Controller app' that sends a char on release of a button
void loop(){
	if(BT.available()){
		if(c = BT.read()){
			lastc = c;
			selector(c);
		}
		else{
			selector(c);
		}
		BT.println(c);
		Serial.println(c);
	}
}

void selector(char choice){
	if(choice=='F'){
		forward();
	}
	if(choice=='B'){
		backward();
	}
	if(choice=='L'){
		left();
	}
	if(choice=='R'){
		right();
	}
	if(choice=='O'){
		stopped();
	}
	else{
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
        //delay(motorTimer);
}

void backward(){
	LMOTOR.run(b);
	RMOTOR.run(b);
	LMOTOR.setSpeed(200);
	RMOTOR.setSpeed(200);
	//delay(motorTimer);
}

void left(){
	LMOTOR.run(b);
	RMOTOR.run(f);
	LMOTOR.setSpeed(127);
	RMOTOR.setSpeed(127);
	//delay(motorTimer);
}

void right(){
	LMOTOR.run(f);
	RMOTOR.run(b);
	LMOTOR.setSpeed(127);
	RMOTOR.setSpeed(127);
	//delay(motorTimer);
}

void stopped(){
	LMOTOR.run(RELEASE);
	RMOTOR.run(RELEASE);
	LMOTOR.setSpeed(0);
	RMOTOR.setSpeed(0);
}
