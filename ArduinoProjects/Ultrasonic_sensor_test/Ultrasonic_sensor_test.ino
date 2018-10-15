const int trigPin = A4;
const int echoPin = A5;
long duration;
int distanceCm, distanceInch;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void ping(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  
  distanceCm= duration*0.034/2;
  distanceInch = duration*0.0133/2;
}

void loop() {
  ping();
  Serial.print("cm distance: ");
  Serial.print(distanceCm);
  Serial.print("inch distance");
  Serial.println(distanceInch);
}
