#include <Servo.h>

Servo servo9;
Servo servo10;

static int pos9 = 0;
static int pos10 = 0;

void setup(){
  Serial.begin(9600);
  servo9.attach(9);
  servo10.attach(10);
  servo9.write(0);
  servo10.write(0);
}

void loop(){
  if(Serial.available()){
  pos9 = Serial.parseInt();
  Serial.print("Position s9 is ");
  Serial.println(pos9, DEC);

  pos10 = 180 - pos9;
  Serial.print("Position s10 is ");
  Serial.println(pos10, DEC);

    if(pos10 > 180 || pos10 < 0 || pos9 > 180 || pos9 < 0){
      Serial.println("\nValues must be between 0 and 180\n\n:Moving to (0, 0):");
      pos9 = 0;
      pos10 = 0;
      loop();
    }
  servo9.write(pos9);
  delay(500);
  servo10.write(pos10);
  delay(1000);
  }
}
