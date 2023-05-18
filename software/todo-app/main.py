import os
import encryption
import sqlite3

def main():
    command = "head -1 /dev/random > code.pass"
    os.system(command)

    random_line = open('code.pass',mode='rb').read()

    conn = sqlite3.connect('passcode.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO passcode (usb_id, pass) VALUES (?, ?)", ("1",random_line,))

    conn.commit()
    conn.close()


def check(usb_id):
    conn = sqlite3.connect('passcode.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT {usb_id} FROM passcode")
    passcode = cursor.fetchone()

    conn.close()
    return passcode == None


if __name__ == '__main__':
    main()
    check("1")
    encryption.test()
