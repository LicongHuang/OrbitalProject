import sqlite3

def getKey(usb_id, conn):

    #TODO : TRY-CATCH
    #conn = sqlite3.connect('passcode.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passcode WHERE usb_id = ?", (usb_id,))
    row = c.fetchone()
    #conn.close()

    # Row could be None
    return row

def insertKey(usb_id, key, conn):
    #TODO : TRY-CATCH 
    #conn = sqlite3.connect('passcode.db')
    c = conn.cursor()
    c.execute("INSERT INTO passcode VALUES (?, ?)", (usb_id, key))
    conn.commit()
    #conn.close()


def checkUSB(usb_id):
    conn = sqlite3.connect('passcode.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passcode WHERE usb_id = ?", (usb_id,))
    row = c.fetchone()

    # Ew if-else in 2023 ? disgusting

    if row is None:
        insertKey(usb_id, "0", conn)
    else:
        getKey(usb_id, conn)

    conn.close()
    



