#import os
#import encryption
import sys
#import dbutil
#import usbutil
import dbutil_encrypt
import authentication
import wait_usb
# This is the main file for the proof of concept


if __name__ == '__main__':
    if authentication.auth():
        print("Authentication successful")
        wait_usb.check_usb()

        next_action = input("Encrypt or decrypt files? (e/d): ")
        
        if next_action == 'e':
            dbutil_encrypt.encryptFiles()
            print("Encrypting files complete")
        
        elif next_action == 'd':
            dbutil_encrypt.decryptFiles()
            print("Decrypting files complete")
        
        else:
            print("Invalid input")
    else:
        print("Authentication failed")
        sys.exit(1)

#    todo = sys.argv[1]
#    if todo == 'e':
#        dbutil_encrypt.encryptFiles()
#        print("Encrypting files complete")
#    elif todo == 'd':
#        dbutil_encrypt.decryptFiles()
#        print("Decrypting files complete")


