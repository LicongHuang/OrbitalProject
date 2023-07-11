#import os
#import encryption
import sys
#import dbutil
#import usbutil
import dbutil_encrypt
import authentication
import wait_usb
import newkeypadcode
# This is the main file for the proof of concept


if __name__ == '__main__':
    try:
        if authentication.auth():
            print("Authentication successful")
            wait_usb.check_usb2()

            print("Encrypt or decrypt files? (1/2): ")
            next_action = newkeypadcode.keypadInput()
            print("Next input:", next_action)            
            if next_action == '1':
                dbutil_encrypt.encryptFiles()
                print("Encrypting files complete")
            
            elif next_action == '2':
                dbutil_encrypt.decryptFiles()
                print("Decrypting files complete")
            
            else:
                print("Invalid input")
        else:
            print("Authentication failed")
            sys.exit(1)

    except KeyboardInterrupt:
        print("Exiting...")
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


