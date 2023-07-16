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

import sys
sys.path.append('/home/orangepi/OrbitalProject')
import software.lcd_stuff.lcd_display as lcd


def authenticate():
    return authentication.auth();

def poc():
    try:
        wait_usb.check_usb2()

        lcd.en_or_de();
        print("Encrypt or decrypt files? (1/2): ")
        
        next_action = newkeypadcode.keypadInput()
        
        lcd.next_in();
        print("Next input:", next_action)            
        
        if next_action == '1':
            dbutil_encrypt.encryptFiles()
            print("Encrypting files complete")
            lcd.en_com();
        
        elif next_action == '2':
            dbutil_encrypt.decryptFiles()
            print("Decrypting files complete")
            lcd.de_com();
        
        else:
            print("Invalid input")
            lcd.invalid_in();
        
        output = subprocess.check_output("lsblk -o MOUNTPOINT | grep -i '/media/orangepi/'", shell=True)
        output = output.decode('utf-8')
        print("End")
        ret = subprocess.check_output("sudo umount {}".format(output), shell=True)

    except KeyboardInterrupt:
        print("Exiting...")
        lcd.exit_c();
        sys.exit(1)

    except Exception as e:
        print(e)

        #sys.exit(1)
    




def main():
    while True:
        if authenticate():
            print("Successful authentication")
            lcd.auth_display();
            poc();

        else:
            print("Authentication failed")
            lcd.auth_fail();

if __name__ == '__main__':
    main();