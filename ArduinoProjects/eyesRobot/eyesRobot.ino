#include <Servo.h>
#include <AFMotor.h>

//Vars for Servo and Motors
Servo eyes;

AF_DCMotor lm(1);
AF_DCMotor rm(2);

//Vars for sensor
const int trigPin = A1;
const int echoPin = A0;
long duration;
int distanceCm, distanceInch;

void setup() {
  Serial.begin(9600);
  eyes.attach(10);
  Serial.println("Eyes attached!");

  lm.setSpeed(0);
  rm.setSpeed(0);

  lm.run(FORWARD);
  rm.run(FORWARD);
  Serial.println("Motors ready!");

  //Sensor pinout
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.println("Sensor Ready");
}

double leftDist;
double midDist;
double rightDist;
double wallDist = 35;     //threshold for detecting 'in front of me'

double trigger;           //value to trigger lookAll-think-act
int brain[] = {0, 0, 0};  //logic based on wall distances
String thought = "";

int qTime = 265;          //time for left and right turns to be 90 degrees
int fTime = 250;          //time for moving forward
int bTime = 50;           //time for moving backward            --maybe i shouldn't hard code these

void loop() {
  meander();
  trigger = scanDistance();
  scanDistance();
  if(trigger < wallDist){
    lookAll();
    think();
    act();
  }
}

void meander(){
  lm.run(FORWARD);
  rm.run(FORWARD);
  lm.setSpeed(100);
  rm.setSpeed(0);
  delay(bTime);
  lm.run(FORWARD);
  rm.run(FORWARD);
  lm.setSpeed(0);
  rm.setSpeed(100);
  delay(bTime);
}

void think() {
  if (!brain[0] && !brain[1] && !brain[2]) {    //000 no walls around me
    thought = "000";
  }
  else if (!brain[0] && !brain[1] && brain[2]) { //001 wall on right
    thought = "001";
  }
  else if (!brain[0] && brain[1] && !brain[2]) { //010 wall on left
    thought = "010";
  }
  else if (!brain[0] && brain[1] && brain[2]) { //011
    thought = "011";
  }
  else if (brain[0] && !brain[1] && !brain[2]) { //100 wall in front
    thought = "100";
  }
  else if (brain[0] && !brain[1] && brain[2]) { //101
    thought = "101";
  }
  else if (brain[0] && brain[1] && !brain[2]) { //110
    thought = "110";
  }
  else if (brain[0] && brain[1] && brain[2]) {  //111 walls all around me! (should go back)
    thought = "111";
  }
  else {                                        //I didn't account for this >.<
    eyes.write(0);                              //shakes head in confusion
    eyes.write(180);
    eyes.write(0);
    eyes.write(180);
    eyes.write(0);
    eyes.write(180);
    eyes.write(0);
    exit(0);
  }
}

void act() {
  if (thought.equals("000")) {
    fd();
    delay(fTime);
    sp();
  }
  else if (thought.equals("001")) {
    fd();
    delay(fTime);
    sp();
  }
  else if (thought.equals("010")) {
    fd();
    delay(fTime);
    sp();
  }
  else if (thought.equals("011")) {
    fd();
    delay(fTime);
    sp();
  }
  else if (thought.equals("100")) {
    bd();
    delay(bTime);
    rt();                         //we should at least make this better since it has a choice
    delay(qTime);
    sp();
  }
  else if (thought.equals("101")) {
    bd();
    delay(bTime);
    lt();
    delay(qTime);
    sp();
  }
  else if (thought.equals("110")) {
    bd();
    delay(bTime);
    rt();
    delay(qTime);
    sp();
  }
  else if (thought.equals("111")) {
    bd();
    delay(bTime);
    sp();
    lt();
    delay(qTime);
    delay(qTime);
    sp();
  }
  else {                                        //I didn't account for this >.<
    eyes.write(45);                              //shakes head in confusion
    eyes.write(135);
    eyes.write(45);
    eyes.write(135);
    eyes.write(45);
    eyes.write(135);
    eyes.write(45);
    exit(0);
  }
}

void lookAll() {
  sp();
  lookForward();
  lookLeft();
  lookRight();
  lookForward();
}

void lookRight() {
  //Look right
  eyes.write(0);
  delay(500);
  rightDist = scanDistance();
  if (rightDist < wallDist) {
    brain[2] = 1;             //wall to the right
  } else {
    brain[2] = 0;             //no wall to the right
  }
  Serial.println(rightDist);
  delay(1000);
}
void lookLeft() {
  //Look left
  eyes.write(180);
  delay(500);
  leftDist = scanDistance();
  if (leftDist < wallDist) {
    brain[1] = 1;             //wall to the left
  } else {
    brain[1] = 0;             //no wall to the left
  }
  Serial.println(leftDist);
  delay(1000);
}
void lookForward() {
  //Look forward!
  eyes.write(90);
  delay(500);
  midDist = scanDistance();
  if (midDist < wallDist) {
    brain[0] = 1;             //wall in front
  } else {
    brain[0] = 0;             //no wall in front
  }
  Serial.println(midDist);
  delay(1000);
}

double scanDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);

  return duration * 0.034 / 2;  //inches vs cm
  //return duration*0.0133/2;
}

int f = FORWARD;
int b = BACKWARD;

void fd() {
  lm.run(f);
  rm.run(f);
  lm.setSpeed(150);
  rm.setSpeed(150);
}

void bd() {
  lm.run(b);
  rm.run(b);
  lm.setSpeed(150);
  rm.setSpeed(150);
}

void lt() {
  lm.run(b);
  rm.run(f);
  lm.setSpeed(150);
  rm.setSpeed(150);
}

void rt() {
  lm.run(f);
  rm.run(b);
  lm.setSpeed(150);
  rm.setSpeed(150);
}

void sp() {
  lm.setSpeed(0);
  rm.setSpeed(0);
}
