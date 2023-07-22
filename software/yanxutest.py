#import os
#import encryption
import sys
#import dbutil
#import usbutil
import dbutil_encrypt
import authentication
import wait_usb
import newkeypadcode
import subprocess
import time
#import sys
#sys.path.append('/home/orangepi/OrbitalProject')
#import software.lcd_stuff.lcd_display as lcd

def poc():
    try:
        print("write something")
        message1 = newkeypadcode.keypadInput()
        newkeypadcode.resetKeypad()
        print("again1")
        time.sleep(1)
        #newkeypadcode.startKeypad()
        message2 = newkeypadcode.keypadInput()
        newkeypadcode.resetKeypad()
        print("again2")
        time.sleep(1)
        #newkeypadcode.startKeypad()
        message3 = newkeypadcode.keypadInput()
        print("message1 is:")
        newkeypadcode.resetKeypad()
        print(message1)
        print("message2 is:")
        print(message2)
        print("message3 is:")
        print(message3)

    except KeyboardInterrupt:
        print("Exiting...")
        lcd.exit_c();
        sys.exit(1)

    except Exception as e:
        print(e)

        #sys.exit(1)
    


def main():
    poc()

if __name__ == '__main__':
    main();
