from smbus import SMBus

# I2C bus number
I2C_BUS = 3

# LCD address
LCD_ADDRESS = 0x27

# LCD dimensions
LCD_WIDTH = 16
LCD_ROWS = 2

# LCD commands
LCD_CLEAR_DISPLAY = 0x01
LCD_RETURN_HOME = 0x02
LCD_DISPLAY_ON = 0x0C
LCD_CURSOR_OFF = 0x0C

# LCD line addresses
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# Function to send command to LCD
def lcd_command(cmd):
	bus.write_byte(LCD_ADDRESS, cmd)

# Function to initialise the LCD
def lcd_init():
	lcd_command(0x33)
	lcd_command(0x32)
	lcd_command(0x06)
	lcd_command(0x0C)
	lcd_command(0x28)
	lcd_command(0x01)

# Function to clear the LCD display
def lcd_clear():
	lcd_command(LCD_CLEAR_DISPLAY)

# Function to set the cursor position
def lcd_set_cursor(line, pos):
	if line == 1:
		lcd_command(LCD_LINE_1 + pos)
	elif line == 2:
		lcd_command(LCD_LINE_2 + pos)

# Function to display text on the LCD
def lcd_print(message):
	for char in message:
		bus.write_byte_data(LCD_ADDRESS, 0x40, ord(char))

# Initialise the SMBus
bus = SMBus(I2C_BUS)

# Initialise the LCD
lcd_init()

# Clear the display
lcd_clear()

# Display a message
lcd_set_cursor(1,0)
lcd_print("LOW")

lcd_set_cursor(2,0)
lcd_print("HI")

# Close the SMBus
bus.close()

