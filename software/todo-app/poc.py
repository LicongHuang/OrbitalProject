import os
import encryption
import sqlite3
import dbutil

def poc():

    random_line = genKey()
    conn = sqlite3.connect('passcode.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO passcode (usb_id, pass) VALUES (?, ?)", ("1",random_line,))

    conn.commit()
    conn.close()

def genKey():

    command = "head -1 /dev/random > key.key"
    os.system(command)

    random_line = open('key.key',mode='rb').read()[:32]

    return random_line



def checkInDatabase(usb_id):
    conn = sqlite3.connect('passcode.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT {usb_id} FROM passcode")
    passcode = cursor.fetchone()

    conn.close()
    return passcode == None


if __name__ == '__main__':
    poc()
    dbutil.checkUSB("1")
    #checkInDatabase("1")
    encryption.test()
