from ctypes import *
import os

print(os.path.abspath('./kp.so'))

myFunct = CDLL(os.path.abspath('./kp.so'))
myFunct.display_lcd.argtypes = [c_char_p]
py_string = "Hello World"
c_string = c_char_p(py_string.encode('utf-8'))

myFunct.display_lcd(c_string)





