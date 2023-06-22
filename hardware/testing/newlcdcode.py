from gpiozero import CharLCD
from time import sleep

# Initialise LCD
lcd = CharLCD('PCF8574', 0x27)

# Clear the LCD screen 
lcd.clear

# Print a message on the LCD
lcd.write_string("Hello, World!")
lcd.cursor_pos = (1,0)
lcd.write_string("LCD Tutorial")

#Wait for a few seconds
sleep(5)

# Clear the LCD screen
lcd.clear()
