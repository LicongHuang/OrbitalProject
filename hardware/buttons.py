#code adapted from https://www.youtube.com/watch?v=0sD9J8iu8RQ&list=PLGs0VKk2DiYxdMjCJmcP6jt4Yw6OHK85O&index=36
#documentation by me

import OPi.GPIO as GPIO #replaced from Ppi.GPIO as GPIO
from time import sleep # not sure how too replace this for orange pi

GPIO.setmode(GPIO.BOARD) #basically choose how pin numbering system, you can choose between BCM and BOARD
outputs = [21,19,15,13] #pins connected to the rows of the keypad, changed numbering to fit orange pi
inputs = [11,7,5,3] #pins connected to the columns of the keypad, changed numbering to fit orange pi
##keyPad = [[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']] #keypad 


GPIO.setup(outputs[0],GPIO.OUT) #basically pinMode
GPIO.setup(outputs[1],GPIO.OUT) #basically pinMode
GPIO.setup(outputs[2],GPIO.OUT) #basically pinMode
GPIO.setup(outputs[3],GPIO.OUT) #basically pinMode

GPIO.setup(inputs[0],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(inputs[1],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(inputs[2],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #basically pinMode input need to set the resistor to pull up or down
GPIO.setup(inputs[3],GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #basically pinMode input need to set the resistor to pull up or down

try:
##polling for signal from the buttons)
  
	while True:
    for myInputs in [0,1,2,3]:
      GPIO.output(inputs[myInputs],GPIO.HIGH)
    if GPIO.input(inputs[0]) == 1:
      print(1)
    if GPIO.input(inputs[1]) == 1:
      print(2)
    if GPIO.input(inputs[2]) == 1:
      print(3)
    if GPIO.input(inputs[3]) == 1:
      print(4)	

except KeyboardInterrupt:
	sleep(.2)
	GPIO.cleanup()
	print('GPIO Good to Go')
