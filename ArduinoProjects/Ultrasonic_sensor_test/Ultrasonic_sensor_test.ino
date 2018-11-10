const int trigPin = A1;
const int echoPin = A0;
long duration;
int distanceCm, distanceInch;

void setup() {
  Serial.begin(9600);
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
  delay(500);
}
