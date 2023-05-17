import os
import sys
import sqlite3


command = "head -1 /dev/random > code.pass"
os.system(command)

random_line = open('code.pass').readline()

conn = sqlite3.connect('passcode.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO passcode VALUES (pass)", (random_line))

conn.commit()
conn.close()



