#import os
#import encryption
import sqlite3
import dbutil
import usbutil
import keygen
import dbutil_encrypt
# This is the main file for the proof of concept

def poc():

    random_line = keygen.genKey()
    conn = sqlite3.connect('passcode.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO passcode (usb_id, pass) VALUES (?, ?)", ("1",random_line,))

    conn.commit()
    conn.close()


def checkInDatabase(usb_id):
    inUSB = dbutil.checkUSB(usb_id)


if __name__ == '__main__':
    print("getFromUSB")
    files = usbutil.getFiles()
    print("encryptFiles")
    dbutil_encrypt.encryptFiles()
    print("decryptFiles")
    dbutil_encrypt.decryptFiles()
    #print("checkUSB")
    #dbutil.checkUSB("1")
#    print("checkInDatabase")
#    checkInDatabase("1")
    #print("encryption.test")
    #encryption.test()
