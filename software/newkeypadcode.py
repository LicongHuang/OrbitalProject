#@@author ChinYanXu-reused
#Reused from https://www.youtube.com/watch?v=0sD9J8iu8RQ&t=1205s youtube tutorial by Paul McWhorter
#With changes to layout of code and functionality
#documentation by me

import OPi.GPIO as GPIO #replaced from Ppi.GPIO as GPIO
from time import sleep # enable us to set delay
GPIO.setwarnings(False)
GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD) #choose how pin numbering system, you can choose between BCM and BOARD
rows = [21,19,15] #pins connected to the rows of the keypad, changed numbering to fit orange pi zero 2
columns = [18,16,10,8] #pins connected to the columns of the keypad, changed numbering to fit orange pi zero 2
keyPad = [[1,2,3,4],[5,6,7,8],[9,0,'#','*']] #keypad


GPIO.setup(rows[0],GPIO.OUT) #pinMode
GPIO.setup(rows[1],GPIO.OUT) #pinMode
GPIO.setup(rows[2],GPIO.OUT) #pinMode

GPIO.setup(columns[0],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[1],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[2],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #pinMode input need to set the resistor to pull up or down
GPIO.setup(columns[3],GPIO.IN,pull_up_down=GPIO.PUD_OFF) #pinMode input need to set the resistor to pull up or down

def keypadInput():
    noPressOld=True
    noPress=True
    word = ""
    myChar = ""
    bufferCount = 0
    try:
    #loop through all the rows then columns. 
    #If the signal is detected , check the active column and row to deduce the keystroke
    #Based on the keystroke determine the action
    #Word is the string used to store the keystrokes
    #If keystroke is '*', delete the entire word
    #If keystroke is '#' return the word
    #If its not '#' or '*' concatenate the keystroke to word
    #noPress and noPressOld are boolean variables used to keep track if the user pressed and held the keystroke to prevent spamming 
        while bufferCount < 9:
            noPress=True
            for myRow in [0,1,2]:
                for myColumn in [0,1,2,3]:
                    GPIO.output(rows[myRow],GPIO.HIGH)
                    butVal=GPIO.input(columns[myColumn])
                    GPIO.output(rows[myRow],GPIO.LOW)
                    if butVal==1:
                        myChar=keyPad[myRow][myColumn]
                        noPress=False

                        if noPress == False and noPressOld == True:
                            if myChar == '*':
                                word = ''
                                bufferCount = 0
                                print("word is deleted")
                            elif myChar == '#':
                                print(word);
                                sleep(0.1)
                                return str(word);
                            else:
                                print(myChar)
                                word += str(myChar)
                                bufferCount += 1
                                print(word)
            noPressOld=noPress
            sleep(0.1)
        #print(word)
        sleep(0.1)
        return word

    except KeyboardInterrupt:
        sleep(.1)
        GPIO.cleanup()
        print('GPIO Good to Go')


def main():
    keypadInput()

if __name__ == "__main__":
    main()
#@@author
