import smbus2
from smbus2 import SMBus
from time import sleep 

# Define I2C address of the LCD 
LCD_I2C_ADDR = 0x27

#Define LCD constants
LCD_WIDTH = 16
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

#Define LCD commands 
LCD_CMD = 0x08
LCD_CHR = 0x0C

def lcd_init():

	#open I2C communication
	bus = smbus2.SMBus(1)

	# Send initialisation commands
	bus.write_byte(LCD_I2C_ADDR, 0x33)
	bus.write_byte(LCD_I2C_ADDR, 0x32)
	bus.write_byte(LCD_I2C_ADDR, 0x06)
	bus.write_byte(LCD_I2C_ADDR, 0x0C)
	bus.write_byte(LCD_I2C_ADDR, 0x28)
	bus.write_byte(LCD_I2C_ADDR, 0x01)
	sleep(0.05)

def lcd_byte(cmd, mode):
	# Converts command to 4-bit mode 
	bits_high = mode | (cmd & 0xF0) | LCD_CMD
	bits_low = mode | ((cmd << 4) & 0xF0) | LCD_CMD

	# OPen I2C communication
	bus = smbus2.SMBus(1)

	# Send high bits 
	bus.write_byte(LCD_I2C_ADDR, bits_high)
	sleep(0.0001)
	bus.write_byte(LCD_I2C_ADDR, bits_high | 0x04)
	sleep(0.0001)
	bus.write_byte(LCD_I2C_ADDR, bits_high)
	sleep(0.0001)

	# Send low bits
	bus.write_byte(LCD_I2C_ADDR, bits_low)
	sleep(0.0001)
	bus.write_byte(LCD_I2C_ADDR, bits_low | 0x04)
	sleep(0.0001)
	bus.write_byte(LCD_I2C_ADDR, bits_low)
	sleep(0.0001)

def lcd_string(message, line):
	# Set the line address
	lcd_byte(line, LCD_CMD)

	# Convert message to bytes and send each character 
	message_bytes = [ord(ch) for ch in message.ljust(LCD_WIDTH, " ")]
	for byte in message_bytes:
		lcd_byte(byte, LCD_CHR)

# Initialise LCD
lcd_init()

# Print a message on the LCD
lcd_string("Hello, World!", LCD_LINE_1) 
lcd_string("LCD Tutorial", LCD_LINE_2)






	
