import OPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

try:
	GPIO.output(12,GPIO.HIGH)
	sleep(5)
	GPIO.output(12,GPIO.LOW)
	sleep(1)

except KeyboardInterrupt:
	sleep(.2)
	GPIO.cleanup()
	print('GPIO good to go')
