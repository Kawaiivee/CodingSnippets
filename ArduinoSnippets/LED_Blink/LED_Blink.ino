void setup() {
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(12, INPUT);
}

char c;
void loop(){
  if(Serial.available()){
    c = Serial.read();
    if(c == '1'){
      ping();
      c = '0';
    }
    else if(c == '0'){
      digitalWrite(11, LOW);
      delay(5000);
    }
  }
}

void ping(){
  delay(6000);
  digitalWrite(11, HIGH);
  delay(200);
  digitalWrite(11, LOW);
  delay(200);
  digitalWrite(11, HIGH);
  delay(200);
  digitalWrite(11, LOW);
  delay(200);
  digitalWrite(11, HIGH);
  delay(200);
  digitalWrite(11, LOW);
  delay(200);
}
