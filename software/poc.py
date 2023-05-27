#import os
#import encryption
import sys
#import dbutil
#import usbutil
import dbutil_encrypt
# This is the main file for the proof of concept


if __name__ == '__main__':
    todo = sys.argv[1]
    if todo == 'e':
        dbutil_encrypt.encryptFiles()
        print("Encrypting files complete")
    elif todo == 'd':
        dbutil_encrypt.decryptFiles()
        print("Decrypting files complete")


