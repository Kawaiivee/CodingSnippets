#include <Servo.h>

Servo servo9;
Servo servo10;

int speed = 2;
int buttonState = 0;

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
    pos9 = 0;
    pos10 = 0;
    servo9.write(pos9);
    servo10.write(pos10);
    }

    else if(buttonState == HIGH){
    
  for (pos9 <= 1; pos9 <= 179; pos9 += speed){
    servo9.write(pos9);
    pos10 = 180 - pos9;
    servo10.write(pos10);
    delay(15);
  }
  
  for (pos9 >= 179; pos9 >= 1; pos9 -= speed){
    servo9.write(pos9);
    pos10 = 180 - pos9;
    servo10.write(pos10);
    delay(15);
  }
    }
}
