#include <WiFi.h>;

WiFiServer server(80); //Initialize the server on Port 80
String E32IP;
void setup() {
  WiFi.mode(WIFI_AP); //Our ESP8266-12E is an AccessPoint 
  WiFi.softAP("TestPoint", "12345678"); // Provide the (SSID, password); . 
  server.begin(); // Start the HTTP Server
  
  Serial.begin(115200); //Start communication between the ESP8266-12E and the monitor window
  IPAddress HTTPS_ServerIP= WiFi.softAPIP(); // Obtain the IP of the Server 
  Serial.print("Server IP is: "); // Print the IP to the monitor window 
  Serial.println(HTTPS_ServerIP);
  E32IP = (String) HTTPS_ServerIP;
}

void loop(){
  WiFiClient client = server.available();
  if (!client) { 
  return; 
  } 
  //Looking under the hood 
  Serial.println("Somebody has connected :)");

  //Read what the browser has sent into a String class and print the request to the monitor
  String request = client.readString(); 
  Serial.println(request);
  //Looking under the hood 
  Serial.println(request);
  if(request.length() > 14){
    Serial.println("WE GOT INPUT!");
    digitalWrite(2, HIGH);
    delay(2000);
    digitalWrite(2,LOW);
  }
  delay(50);
}
