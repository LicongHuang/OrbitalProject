import OPi.GPIO as GPIO
from time import sleep
GPIO.setboard(GPIO.H616)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

try:
	while True:
		GPIO.output(12,1)
		sleep(0.2)
		GPIO.output(12,0)
		sleep(0.2)

except KeyboardInterrupt:
	sleep(.2)
	GPIO.cleanup()
	print('GPIO good to go')
