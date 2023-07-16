#code adapted from https://www.youtube.com/watch?v=0sD9J8iu8RQ&t=1205s
#documentation by me

import OPi.GPIO as GPIO #replaced from Ppi.GPIO as GPIO
from time import sleep # not sure how too replace this for orange pi
GPIO.setwarnings(False)
GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD) #basically choose how pin numbering system, you can choose between BCM and BOARD
rows = [21,19,15] #pins connected to the rows of the keypad, changed numbering to fit orange pi
columns = [18,16,10,8] #pins connected to the columns of the keypad, changed numbering to fit orange pi
keyPad = [[1,2,3,4],[5,6,7,8],[9,0,'#','*']] #keypad


GPIO.setup(rows[0],GPIO.OUT) #basically pinMode
GPIO.setup(rows[1],GPIO.OUT) #basically pinMode
GPIO.setup(rows[2],GPIO.OUT) #basically pinMode

GPIO.setup(columns[0],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[1],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[2],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[3],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #basically pinMode input need to set the resistor to pull up or down

def keypadInput():
    noPressOld=True
    noPress=True
    word = ""
    myChar = ""
    try:
    #loop through all the rows then columns. If the signal is detected , check the active column and row to deduct the keystroke and print out the keystroke
        while True:
            noPress=True
            for myRow in [0,1,2]:
                for myColumn in [0,1,2,3]:
                    GPIO.output(rows[myRow],GPIO.HIGH)
                    butVal=GPIO.input(columns[myColumn])
                    GPIO.output(rows[myRow],GPIO.LOW)
                    if butVal==1:
                        myChar=keyPad[myRow][myColumn]
                        #print(myChar)
                        noPress=False
                    
                    if myChar == '#':
                        print("Returning the word:", str(word));
                        return str(word);

                    if butVal==1 and noPress==False and noPressOld==True: #check if the button is pressed the first time. to prevent spamming
                        #myChar=keyPad[myRow][myColumn]
                        print(myChar) #can change this to send to another file instead of just printing it
                        word += str(myChar);
                        #noPress=True
            noPressOld=noPress
            sleep(.1)

    except KeyboardInterrupt:
        sleep(.2)
        GPIO.cleanup()
        print('GPIO Good to Go')
