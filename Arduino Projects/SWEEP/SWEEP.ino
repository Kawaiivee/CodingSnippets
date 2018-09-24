#include <Servo.h>
 
Servo servo;
 
int pos = 0;  // Stores the position (angle) of the servo. Range is [0, 180].
int speed = 0;
int count = 0;

void setup() 
{ 
  Serial.begin(9600);
  servo.attach(10);  // Attaches the servo on pin 10 to the servo object.
  servo.write(0);  // Resets the position.
} 

void loop(){
  if(speed == 0 && count <= 0 && Serial.available()){
    
    servo.write(pos);
    
    speed = Serial.parseInt();
    Serial.print("Speed is ");
    Serial.println(speed, DEC);
    
    count = Serial.parseInt();
    Serial.print("Initial Count is ");
    Serial.println(count, DEC);
    
    delay(200);
    }

    else if(speed != 0 && count > 0){
    
  for (pos <= 0; pos <= 179; pos += speed){
    servo.write(pos);
    delay(15);
  }
  
  for (pos >= 180; pos >= 1; pos -= speed){
    servo.write(pos);
    delay(15);
  }
  
    count = count - 1;
    //STOP AFTER COUNT IS ZERO
    if(count <= 0){
      speed = 0;
      pos = 0;
    }
    Serial.print("Current count is ");
    Serial.println(count, DEC);
    }
}

