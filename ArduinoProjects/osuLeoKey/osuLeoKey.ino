#include "Keyboard.h"

void setup(){
	pinMode(2, INPUT);
	pinMode(3, INPUT);
	Keyboard.begin();
}

void loop(){
	if(digitalRead(2)==HIGH){
		Keyboard.press('z');
	}
	else if(digitalRead(3)==HIGH){
		Keyboard.press('x');
	}
	else{
		Keyboard.releaseAll();
	}
}
