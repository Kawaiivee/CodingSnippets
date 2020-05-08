#include <Keyboard.h>

void setup(){
	Serial.begin(9600);
	Keyboard.begin();
	pinMode(2, INPUT);
}

void loop() {
	if(digitalRead(2)==HIGH){
		combo();
	}
}

void combo(){
	button(0xD7, .25);
	button('a', .2);
	button('s', .3);
	button('d', .35);
	button('z', .2);
	button(0xDA, .4);
	button('a', .2);
	button('s', .3);
	button('d', .35);
	button('z', .1);
	Keyboard.releaseAll();
}

//delay of holding button or 0 delay to just do it
void button(char c, double d){
	//Serial.println(c);
	if(d > 0){
		Keyboard.press(c);
		delay(d*1000);
		Keyboard.release(c);
	}
	else{
		Keyboard.press(c);
		Keyboard.release(c);
	}
}
