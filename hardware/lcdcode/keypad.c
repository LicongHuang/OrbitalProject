#include <stdio.h>
#include <wiringPi.h>

//Define the keypad pins


int rows[3] = {21, 19, 15};
int columns[4] = {18, 16, 10, 8};

// Define the keypad layout
char KeyPad[3][4] = {
	{'1','2','3','4'},
	{'5','6','7','8'},
	{'9','0','#','*'}
};

//Function to initialise the keypad pins
void initialiseKeyPad() {
	int i;
	for (i = 0; i < 3; i++) {
		pinMode(rows[i], OUTPUT);
		digitalWrite(rows[i], HIGH);
	}
	for (i = 0; i < 4; i++) {
		pinMode(columns[i], INPUT);
		pullUpDnControl(columns[i], PUD_UP);
	}
}

// Function to get the key pressed on the keypad
char getKey() {
	int i, j;
	char key = '\0';
	for (i = 0; i < 3; i++) {
		digitalWrite(rows[i], LOW);
		for (j = 0;  j < 4; j++) {
			if (digitalRead(columns[j]) == LOW) {
				key = KeyPad[i][j];
				while (digitalRead(columns[j] == LOW)) {
					delay(10);
				}
			}
		}
		digitalWrite(rows[i], HIGH);
	}
	return key;
}

int main() {
	wiringPiSetupPhys();
	//if (wiringPiSetup() == -1) {
	//	printf("Unable to initialise WiringPi library. \n");
	//	return 1;
	//}
	initialiseKeyPad();
	while(1) {
		char key = getKey();
		if (key != '\0') {
			printf("Key pressed: %c\n", key);
		}
	}

	return 0;
}

