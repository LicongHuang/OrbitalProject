//@@author ChinYanXu-reused
//Reused from https://www.youtube.com/watch?v=0sD9J8iu8RQ&t=1205s youtube tutorial by Paul McWhorter
//With changes to layout of code and functionality. 
//Also original code is in python this code is in C
//documentation by me

#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include "i2c.h"
#include "lcd.h"
#include <string.h>

#define I2C_FILE_NAME "/dev/i2c-3"

//@@author ChinYanXu-reused
//Reused from Wargio liblcm1602 library for the 1602 LCD Screen with I2C backpack
//https://github.com/wargio/liblcm1602
//copied the code for initialising the LCD Screen

const char* txt[] = {
	"Password##?"
};

int keypad() {

	wiringPiSetupPhys();
	int i2c_dev;
	lcd lcd0;
	//0x27 is the address of the i2c device
	i2c_dev = open_i2c(I2C_FILE_NAME, 0x27);
	if (i2c_dev <0) {
		printf("Errore: %d\n", i2c_dev);
		return -1;
	}
	lcd_init(&lcd0, i2c_dev);
	lcd_clear(&lcd0);
	lcd_print(&lcd0, txt[0], strlen(txt[0]), 0);
	//@@author

	int rows[3] = {21,19,15}; // array to store the pins on the orange pi zero 2 that controls the rows
	int columns[4] = {18,16,10,8}; // array to store the pins on the orange pi zero 2 that controls the columns
	char keyPad[3][4] = {{'1','2','3','4'},{'5','6','7','8'},{'9','0','#','*'}}; // array to store the keystrokes used

	pinMode(rows[0], OUTPUT); //setting rows as output
	pinMode(rows[1], OUTPUT); //setting rows as output
	pinMode(rows[2], OUTPUT); //setting rows as output

	pinMode(columns[0], INPUT); //setting rows as input
	pinMode(columns[1], INPUT); //setting rows as input
	pinMode(columns[2], INPUT); //setting rows as input
	pinMode(columns[3], INPUT); //setting rows as input

	pullUpDnControl(columns[0], PUD_UP); //pinMode input need to set the resistor to pull up or down
	pullUpDnControl(columns[1], PUD_UP); //pinMode input need to set the resistor to pull up or down
	pullUpDnControl(columns[2], PUD_UP); //pinMode input need to set the resistor to pull up or down
	pullUpDnControl(columns[3], PUD_UP); //pinMode input need to set the resistor to pull up or down


	bool noPressOld = true;
	bool noPress = true;

	char buffer[7] = "";
	char myChar;
	int butVal;
	int bufferCount = 0;
	int password;
	
	//loop through all the rows then columns.
    	//If the signal is detected , check the active column and row to deduce the keystroke
    	//Based on the keystroke determine the action
    	//Word is the string used to store the keystrokes
    	//If keystroke is '*', delete the entire word
    	//If keystroke is '#' return the word
   	//If its not '#' or '*' concatenate the keystroke to word
    	//noPress and noPressOld are boolean variables used to keep track if the user pressed and held the keystroke to prevent spamming

	while(bufferCount < 6) {
		noPress = true;
		for(int myRows = 0; myRows < 3; myRows++) {
			for(int myColumns = 0; myColumns < 4; myColumns++) {
				digitalWrite(rows[myRows], HIGH);
				butVal = digitalRead(columns[myColumns]);
				digitalWrite(rows[myRows], LOW);

				if (butVal == 1) {
					myChar = keyPad[myRows][myColumns];	
					noPress = false;
					if (noPress == false && noPressOld == true) {
						if (myChar == '#') {
							buffer[bufferCount - 1] = ' ';
							bufferCount--;
							lcd_print(&lcd0, buffer, strlen(buffer), 1);
							printf("%s\n", buffer);
						}
						else if (myChar == '*') {
							password = atoi(buffer);
							printf("%i", password);
							usleep(2000);
							close_i2c(i2c_dev);
							printf("%s", "good to go");
							if (bufferCount == 0 && buffer[bufferCount] == ' ') {
								return 0;
							}
							return password;
						}
						else {							
							buffer[bufferCount] = myChar;
							lcd_print(&lcd0, buffer, strlen(buffer), 1);
							printf("%s\n", buffer);
							bufferCount++;
						}
					}
				}
			}
		}
		noPressOld = noPress;
		usleep(2000);
	}
	password = atoi(buffer);
	printf("%i", password);
	usleep(2000);
	close_i2c(i2c_dev);
	printf("%s", "good to go");
	return password;

}


int main() {
	int password2;
	password2 = keypad();
	printf("%i", password2);
}

//@@author
