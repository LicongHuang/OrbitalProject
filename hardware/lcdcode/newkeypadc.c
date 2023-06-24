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

const char* txt[] = {
	"Password?"
};

int main() {
	wiringPiSetupPhys();
	
	int i2c_dev;
	lcd lcd0;
	//0x27 is the address of the i2c device
	i2c_dev = open_i2c(I2C_FILE_NAME, 0x27);
	if (i2c_dev <0) {
		printf("Errore: %d\n", i2c_dev);
		return 1;
	}
	lcd_init(&lcd0, i2c_dev);
	lcd_clear(&lcd0);
	lcd_print(&lcd0, txt[0], strlen(txt[0]), 0);

	int rows[3] = {21,19,15};
	int columns[4] = {18,16,10,8};
	//char keyPad[3][4] = {{'1','2','3','4'},{'5','6','7','8'},{'9','0','#','*'}};
	char keyPad[] = {"1234567890#"};

	pinMode(rows[0], OUTPUT);
	pinMode(rows[1], OUTPUT);
	pinMode(rows[2], OUTPUT);

	pinMode(columns[0], INPUT);
	pinMode(columns[1], INPUT);
	pinMode(columns[2], INPUT);
	pinMode(columns[3], INPUT);

	pullUpDnControl(columns[0], PUD_UP);
	pullUpDnControl(columns[1], PUD_UP);
	pullUpDnControl(columns[2], PUD_UP);
	pullUpDnControl(columns[3], PUD_UP);


	bool noPressOld = true;
	bool noPress = true;
	bool* noPressOldPtr = &noPressOld;
	bool* noPressPtr = &noPress;

	char buffer[16] = {""};

	//printf("%s"," begin");

	while(strlen(buffer) < 6) {
		*noPressPtr = true;
		int myRows;
		int myColumns;
		char myChar;
		int butVal;
		for(myRows = 0; myRows < 3; myRows++) {
			for(myColumns = 0; myColumns < 4; myColumns++) {
				digitalWrite(rows[myRows], HIGH);
				butVal = digitalRead(columns[myColumns]);
				digitalWrite(rows[myRows], LOW);

				if (butVal == 1) {
					myChar = keyPad[((myRows + 1)*(myColumns + 1) -1)];
					*noPressPtr = false;
				}
				//printf("%c", noPress);

				if (butVal == 1 && *noPressPtr == false && *noPressOldPtr == true) {
					printf("%c", myChar);
					//if (strlen(buffer) == 16) {
					//	return 0;
					//}
					strcat(buffer, &myChar);
					//lcd_print(&lcd0, buffer, 1, 1);
					//lcd_print(&lcd0, myChar, strlen(myChar), 1);
				}
			}
			//noPressOld = noPress;
			//usleep(200000);
		}
		*noPressOldPtr = noPress;
		usleep(2000);
	}
	lcd_print(&lcd0, buffer, strlen(buffer), 1);
	usleep(2000);
	close_i2c(i2c_dev);
	//wiringPiCleanup();
	printf("%s", "good to go");

}
