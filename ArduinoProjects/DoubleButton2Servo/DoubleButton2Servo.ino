#include <Servo.h>

Servo servo9;
Servo servo10;

int speed = 2;
int buttonState2 = 0;
int buttonState4 = 0;
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
 //READ BUTTON IN PIN 2 & 4 PUSH
 buttonState2 = digitalRead(2);
 buttonState4 = digitalRead(4);

 if(buttonState2 == LOW){
    //Not pushed? Return to origin
    servo9.write(0);
    }

    else if(buttonState2 == HIGH){
      servo9.write(180);
    }
    
 if(buttonState4 == LOW){
    //Not pushed? Return to origin
    servo10.write(0);
    }

    else if(buttonState4 == HIGH){
      servo10.write(180);
    }
}    
