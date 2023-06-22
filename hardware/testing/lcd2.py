import OPi.GPIO as GPIO
import time

# Define GPIO pin constants for I2C communication
SDA_PIN = 3 #GPIO2
SCL_PIN = 5 #GPIO3

# Define I2C address of the LCD
LCD_I2C_ADDR =0x27

# Define LCD constants
LCD_WIDTH = 16
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

#Define LCD commands
LCD_CMD = 0x08
LCD_CHR = 0x0C

# Define timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def i2c_init():
	GPIO.setboard(GPIO.ZERO)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(SDA_PIN, GPIO.OUT)
	GPIO.setup(SCL_PIN, GPIO.OUT)

def i2c_start():
	GPIO.output(SDA_PIN, GPIO.LOW)
	time.sleep(E_DELAY)
	GPIO.output(SCL_PIN, GPIO.LOW)

def i2c_stop():
	GPIO.output(SCL_PIN, GPIO.LOW)
	time.sleep(E_DELAY)
	GPIO.output(SDA_PIN, GPIO.LOW)
	GPIO.output(SCL_PIN, GPIO.HIGH)
	GPIO.output(SDA_PIN, GPIO.HIGH)
	time.sleep(E_DELAY)

def i2c_write_byte(bits):
	for i in range(8):
		GPIO.output(SDA_PIN, bits & 0x80)
		bits = bits << 1
		GPIO.output(SCL_PIN, GPIO.HIGH)
		time.sleep(E_DELAY)
		GPIO.output(SCL_PIN, GPIO.LOW)
		time.sleep(E_DELAY)

def lcd_byte(bits, mode):
	i2c_start()
	i2c_write_byte(LCD_I2C_ADDR << 1)
	i2c_write_byte(bits | mode)
	i2c_write_byte(bits & ~mode)
	i2c_stop()

def lcd_init():
	lcd_byte(0x33, False) # 110011 Initialise
	lcd_byte(0x32, False) # 110010 Initialise
	lcd_byte(0x06, False) # 000110 Cursor move direction
	lcd_byte(0x0C, False) # 001100 Display On, Cursor Off, Blink Off
	lcd_byte(0x28, False) # 101000 Data length, number of lines,font size
	lcd_byte(0x01, False) # 000001 Clear display
	time.sleep(E_DELAY)

def lcd_string(message, line):
	message = message.ljust(LCD_WIDTH, " ")
	lcd_byte(line, False)

	for i in range(LCD_WIDTH):
		lcd_byte(ord(message[i]), True)

# Initialise I2C communication
i2c_init()

# Initialise LCD
lcd_init()

# Print a message on the LCD
lcd_string("Hello, world!", LCD_LINE_1)
lcd_string("LCD Tutorial", LCD_LINE_2)

# Cleanup GPIO
GPIO.cleanup()
