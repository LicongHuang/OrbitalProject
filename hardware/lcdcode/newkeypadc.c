#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>


int rows[3] = {21,19,15};
int columns[4] = {18,16,10,8};
char KeyPad[3][4] = {{'1','2','3','4'},{'5','6','7','8'},{'9','0','#','*'}};

pinMode(rows[0], OUTPUT);
pinMode(rows[1], OUTPUT);
pinMode(rows[2], OUTPUT);

pinMode(columns[0], INPUT);
pinMode(columns[1], INPUT);
pinMode(columns[2], INPUT);
pinMode(columns[3], INPUT);

bool noPressOld = true;
bool noPress = true;


while(true) {
	noPress = true;
	int myRows;
	int myColumns;
	for(myRows = 0; myRows < 3; myRows + 1) {
		for(myColumns = 0; myColumns < 4; myColumns + 1) {
			digitalWrite(rows[myRows], 1);
			int butVal = digitalRead(columns[myColumns]);
			digitalWrite(rows[myRows], 0);
			if (butVal == 1) {
				char myChar = keyPad[myRows][myColumns];
				noPress = false;
			}
			if (butVal == 1 && noPress == false && noPressOld == true) {
				printf(myChar);
			}
		}
	}
	noPressOld = noPress;
	usleep(.1);
}

printf("good to go");


