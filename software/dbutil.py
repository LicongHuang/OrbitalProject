# Author: Huang Licong
import keygen
import sqlite3
import logging

# This gets the key from the database
# usb_id: The id of the usb
# conn: The connection to the database
def getKey(usb_id, conn):

    #TODO : TRY-CATCH
    c = conn.cursor()
    c.execute("SELECT pass FROM passcode WHERE usb_id = ?", (usb_id,))
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

def deleteUSB(usb_id, conn):
    c = conn.cursor()
    c.execute("DELETE FROM passcode WHERE usb_id = ?", (usb_id,))
    conn.commit()

def connect():
    conn = sqlite3.connect('passcode.db')
    return conn

def disconnect(conn):
    conn.close()

# This checks if the usb is in the database
# if so, it does nothing
# if not, it inserts the usb into the database
# usb_id: The id of the usb
def checkUSB(usb_id):
    conn = connect()
    row = getKey(usb_id, conn)
    # Ew if-else in 2023 ? disgusting
    result = False
    if not row is None:
       result = True 
        #row = keygen.genKey()
        #insertKey(usb_id, row, conn)
        #logging.info("Inserted new key for usb_id: " + usb_id)
    conn.close()
    return result
    
def useKey(usb_id):
    conn = connect()
    # if the usb is in the database, get the key
    if checkUSB(usb_id):
        key = getKey(usb_id, conn)
        #deleteUSB(usb_id, conn)
        logging.info("Deleted key for usb_id: " + usb_id)
    else:
        key = keygen.genKey()
        insertKey(usb_id, key, conn)
        logging.info("Inserted new key for usb_id: " + usb_id)

    conn.close()
    return key

