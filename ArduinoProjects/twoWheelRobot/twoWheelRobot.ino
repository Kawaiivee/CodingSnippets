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

//HOLDING THE BUTTON DOWN KIND OF WORKS. THIS IS A NAIVE POLLING SYSTEM 
//BECAUSE WE CHECK IF THERE IS A NEW SIGNAL READ...
//THIS CAUSES AN ISSUE WHERE WE CAN ONLY POLL 'AFTER' THE MOTOR RUNS
//THE ACTUAL FIX WOULD BE TO HAVE THE BT CONTROLLER BE ABLE TO HAVE AND F and f state for 'PRESSED' AND 'released' respectively
//THE OTHER FIX WOULD BE TO HAVE SOME KIND OF TIME-POLLING SYSTEM TO CHECK FOR NEW INPUTS...THIS WAS HARD TO IMPLEMENT
//AND THE DELAY() FUNCTIONS NECESSARY DIDN'T HELP.
//BELOW IS THE BEST I COULD COME UP WITH
//
//change motorTimer to smaller numbers for better polling change to larger numbers for larger movements...such a damn trade-off 
void loop(){
	if(BT.available()){
		if(c = BT.read()){
			lastc = c;
			selector(c);
		}
		else if(lastc==c){
			c = 'S';
			selector(lastc);
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
	if(choice=='S'){
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
}
