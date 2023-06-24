import OPi.GPIO as GPIO

try:
	import OPi.GPIO as GPIO
	print("library installed successfully")

except ImportError:
	print("error")
