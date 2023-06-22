from periphery import I2C

# I2C bus number 
I2C_BUS = 1

def scan_i2c_address(i2c_bus, address):
	try:
		with I2C("/dev/i2c-{}".format(i2c_bus)) as i2c:
			i2c.transfer(address, [])
		return True
	except IOError:
		return False

def find_lcd_address():
	for address in range(0x03, 0x7F):
		if scan_i2c_address(I2C_BUS, address):
			return address
	return None

# Find the I2C address of the LCD screen
lcd_address = find_lcd_address()

if lcd_address is not None:
	print("LCD screen found at address: 0x{:02X}".format(lcd_address))
else:
	print("LCD screen not found.")

