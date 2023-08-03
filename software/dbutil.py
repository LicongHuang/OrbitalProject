# Author: Huang Licong
# DB utility code base
import keygen
import sqlite3



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
    print(f" New key, {usb_id} inserted")
    conn.commit()   

def deleteUSB(usb_id, conn):
    c = conn.cursor()
    c.execute("DELETE FROM passcode WHERE usb_id = ?", (usb_id,))
    print(f"Successfully deleted {usb_id}")
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
    conn.close()
    return result
    
def useKey(usb_id):
    conn = connect()
    # if the usb is in the database, get the key
    if checkUSB(usb_id):
        key = getKey(usb_id, conn)[0]
    else:
        key = keygen.genKey()
        insertKey(usb_id, key, conn)

    conn.close()
    key = key + b'0'*(32 - len(key));
    return key

