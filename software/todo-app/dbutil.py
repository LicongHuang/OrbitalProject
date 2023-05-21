# Author: Huang Licong

import sqlite3
import logging

# This gets the key from the database
# usb_id: The id of the usb
# conn: The connection to the database
def getKey(usb_id, conn):

    #TODO : TRY-CATCH
    c = conn.cursor()
    c.execute("SELECT * FROM passcode WHERE usb_id = ?", (usb_id,))
    row = c.fetchone()

    # Row could be None
    return row

# This inserts the key into the database
# usb_id: The id of the usb
# key: The key to be inserted
# conn: The connection to the database
def insertKey(usb_id, key, conn):
    #TODO : TRY-CATCH 
    c = conn.cursor()
    c.execute("INSERT INTO passcode VALUES (?, ?)", (usb_id, key))
    conn.commit()


# This checks if the usb is in the database
# if so, it does nothing
# if not, it inserts the usb into the database
# usb_id: The id of the usb
def checkUSB(usb_id):
    conn = sqlite3.connect('passcode.db')
    row = getKey(usb_id, conn)
    # Ew if-else in 2023 ? disgusting

    if row is None:
        insertKey(usb_id, "0", conn)
        logging.info("Inserted new key for usb_id: " + usb_id)
    else:
        logging.info("Found key for usb_id")

    conn.close()
    



