#code from https://www.youtube.com/watch?v=0sD9J8iu8RQ&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=36
#documentation by me

import Ppi.GPIO as GPIO //replace this with wiringOP
from time import sleep // not sure how to replace this for orange pi
// GPIO.setmode(GPIO.BOARD) //basically choose how pin numbering system, you can choose between BCM and BOARD
rows[11,13,15,29] //pins connected to the rows of the keypad
columns[31,33,35,37] //pins connected to the columns of the keypad
keyPad[[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]//keypad 

GPIO.setup(rows[0],GPIO.OUT) //basically pinMode
GPIO.setup(rows[1],GPIO.OUT) //basically pinMode
GPIO.setup(rows[2],GPIO.OUT) //basically pinMode
GPIO.setup(rows[3],GPIO.OUT) //basically pinMode

GPIO.setup(columns[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) //basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) //basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) //basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) //basically pinMode input need to set the resistor to pull up or down

try:
//loop through all the rows then columns. If the signal is 
	while True:
		for myRow in [0,1,2,3]:
			for myColumn in [0,1,2,3]: 
				GPIO.output(rows[myRow],GPIO.HIGH)
				butVal=GPIO.input(columns[myColumn])
				GPIO.output(rows[myRow],GPIO.LOW)
				if butVal ==1:
					myChar=keyPad[myRow][myColumn]
					noPress=False
				if butVal==1 and noPress==False and noPressOld==True
					print(myChar) //can change this to send to another file instead of just printing it
			noPressOld=noPress
			sleep(.2)

except KeyboardInterrupt:
	sleep(.2)
	GPIO.cleanup()
	print('GPIO Good to Go')