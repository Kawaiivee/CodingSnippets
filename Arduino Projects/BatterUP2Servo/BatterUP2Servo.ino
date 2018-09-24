#include <Servo.h>

Servo servo9;
Servo servo10;

int speed = 2;
int buttonState = 0;
int movementState = 0;//0 means decrease 1 means increase

static int pos9 = 0;
static int pos10 = 0;

void setup(){
  Serial.begin(9600);
  servo9.attach(9);
  servo10.attach(10);
  servo9.write(0);
  servo10.write(0);

  //BUTTON ON PIN 2
  pinMode(2, INPUT);
  
}

void loop(){
 //READ BUTTON IN PIN 2 PUSH
 buttonState = digitalRead(2);

 if(buttonState == LOW){
    //Not pushed? Return to origin
    servo9.write(0);
    servo10.write(0);
    }

    else if(buttonState == HIGH){
      servo9.write(150);
      servo10.write(150);
    }
}
