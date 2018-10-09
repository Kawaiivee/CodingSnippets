int t;
void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 100; i <=  500; i = i + 50){
      digitalWrite(11, HIGH);
      delay(i);
      digitalWrite(11, LOW);
      delay(i);
  }

  for(int i = 500; i >=  0; i = i - 50){
      digitalWrite(11, HIGH);
      delay(i);
      digitalWrite(11, LOW);
      delay(i);
  }
}
