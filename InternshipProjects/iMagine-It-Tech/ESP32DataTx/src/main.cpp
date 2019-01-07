#include <Arduino.h>
#include <WiFi.h>
#include <WebSocketsServer.h>
//***BE SURE TO HAVE THE ESP32 LIBRARY, AND THE 'websockets' LIBRARY FROM ARDUINO INSTALLED!
//SSID Credentials
const char* ssid = "mHub_Guest";
const char* pass = "mhubchicago";

//Initialize Web Socket Server
WebSocketsServer webSocket = WebSocketsServer(80);

//user made handler for web socket events
void webSocketEventHandler(uint8_t num, WStype_t type, uint8_t * data, size_t length){
    //use switch-case to filter different type of events
    switch(type){
        //client disconnected
        case WStype_DISCONNECTED:
            Serial.printf("[%u] has disconnected.", num);
            break;

        //new client connected
        case WStype_CONNECTED:
        {
            IPAddress ipaddr = webSocket.remoteIP(num);
            Serial.printf("[%u] has connected with IP Address ", num);
            Serial.println(ipaddr.toString());
        }
        break;

        //echo back to the client with num 'num' the given data
        case WStype_TEXT:
            Serial.printf("[%u] Text: %s\n", num, data);
            webSocket.sendTXT(num, data);
            break;

        //different cases of events that can happen through web socketing
        case WStype_BIN:
        case WStype_ERROR:
        case WStype_FRAGMENT_TEXT_START:
        case WStype_FRAGMENT_BIN_START:
        case WStype_FRAGMENT:
        case WStype_FRAGMENT_FIN:
        default:
            break;
    }
}

void setup(){
    //Initialize Serial Object for debugging on serial monitor
    Serial.begin(115200);
    Serial.println("Attempting to connect to the SSID...");
    WiFi.begin(ssid, pass);

    //keep polling until we connect
    while(WiFi.status() != WL_CONNECTED){
        delay(500);
        Serial.print(".");
    }

    //IF WE GET TO THIS POINT IN THE CODE, WE HAVE OFFICIALLY CONNECTED TO WiFi!
    Serial.println("Connected to the SSID!");
    Serial.print("ESP32 IP Address is: ");
    Serial.println(WiFi.localIP());

    webSocket.begin();
    webSocket.onEvent(webSocketEventHandler);
}

//Keep Checking The Websocket for the life of the program
void loop(){
    webSocket.loop();
}
