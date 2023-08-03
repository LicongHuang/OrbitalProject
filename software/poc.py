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

import sys
sys.path.append('/home/orangepi/OrbitalProject/software')
import lcd_stuff.lcd_display as lcd


def authenticate():
    return authentication.auth();

def poc():
    try:
        wait_usb.check_usb()

        lcd.en_or_de();
        print("Encrypt or decrypt files? (1/2): ")
        time.sleep(1)
        next_action = newkeypadcode.keypadInput()
        
        #lcd.next_in();
        print("Next input:", next_action)            
        
        if next_action == '1':
            lcd.encrypting()
            dbutil_encrypt.encryptFiles()
            time.sleep(1)
            print("Encrypting files complete")
            lcd.en_com();
            time.sleep(1)

        
        elif next_action == '2':
            lcd.decrypting()
            dbutil_encrypt.decryptFiles()
            time.sleep(1)
            print("Decrypting files complete")
            lcd.de_com();
            time.sleep(1)

        
        else:
            print("Invalid input")
            lcd.invalid_in();
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
        lcd.exit_c();
        sys.exit(1)
        time.sleep(1)

    except Exception as e:
        print(e)
        #sys.exit(1)
    finally: 
        ret = subprocess.check_output("sudo umount /dev/sda1", shell=True)



def main():
    while True:
        print("Starting Program Up")
        lcd.insertpass()
        time.sleep(1)
        if authenticate():
            print("Successful authentication")
            lcd.auth_display();
            time.sleep(1)
            poc();
            time.sleep(1);

        else:
            print("Authentication failed")
            lcd.auth_fail();
            time.sleep(1);

if __name__ == '__main__':
    main();
