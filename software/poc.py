#import os
#import encryption
import sys
#import dbutil
#import usbutil
import dbutil_encrypt
import authentication
import wait_usb
import newkeypadcode
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

    except KeyboardInterrupt:
        print("Exiting...")
        lcd.exit_c();
        sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)

#    todo = sys.argv[1]
#    if todo == 'e':
#        dbutil_encrypt.encryptFiles()
#        print("Encrypting files complete")
#    elif todo == 'd':
#        dbutil_encrypt.decryptFiles()
#        print("Decrypting files complete")


if __name__ == '__main__':
    while True:
        if authentication():
            print("Successful authentication")
            lcd.auth_display();
            poc();

        else:
            print("Authentication failed")
            lcd.auth_fail();