# Maintainer: Huang Licong
import nacl.secret
import os
#import keygen
import dbutil

#Encryption method is salsa20

# This gets the first line from /dev/random and base64 encodes it
# Then it gets the first 32 bytes of the key
# This is the key used for encryption
def getKey(id):
    #os.system("head -1 /dev/urandom | base64 > code.pass")
    conn = dbutil.connect() 
    #key = open("key.key", mode="rb").read()[:32]
    key = dbutil.getKey(id, conn)
    conn.close()
    return key

# This is the encryption function
# file: the file to be encrypted
def encryption(key, file):
    cipher = nacl.secret.SecretBox(key)
    plaintext = file
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# This is a function to decrypt the file
# file: the file to be decrypted
def decryption(key, file):
    cipher = nacl.secret.SecretBox(key)
    plaintext = cipher.decrypt(file)
    return plaintext 

# This is a function to make the file
# filename: the name of the file
# ciphertext: the ciphertext of the file
def makeEncryptedFile(filename, ciphertext):
    # to consider: filename should not end with .td
    # TODO make the function actually working
    filepath = f"{filename}"
    f = open(filepath + ".td", mode="wb")
    f.write(ciphertext) 
    f.close()

def makeEncryptedFile2(filename, ciphertext):
    filepath = f"{filename}"
    filepath = '/home/orangepi/'+ "'" + filepath.split('/')[-1] + "'"
    makefile = open(filepath + ".td", mode="wb")
    makefile.write(ciphertext)
    makefile.close()
    os.system(f"sudo mv {filepath}.td {filename}.td")

def makeDecryptedFile(filename, plaintext):
    # TODO make the function actually working
    #filename should always end with .td
    # something will check for .td and pass it into makeDecryptedFile
    filepath = f"{filename[:-3]}"
    f = open(filepath, mode="wb")
    f.write(plaintext) 
    f.close()

def makeDecryptedFile2(filename, plaintext):
    filepath = f"{filename[:-3]}"
    filepath = '/home/orangepi/'+ "'" +filepath.split('/')[-1] + "'"
    makefile = open(filepath, mode="wb")
    makefile.write(plaintext)
    makefile.close()
    os.system(f"sudo mv {filepath} {filename[:-3]}")

def removeFile(filename):
    # TODO make the function actually working
    if os.path.exists(filename):
        os.remove(filename)
        print("The file was removed")
    else:
        print("The file does not exist")
    
def removeFile2(filename):
    if os.path.exists(filename):
        os.system('rm ' + filename)
        print("The file was removed")
    else:
        print("The file does not exist")


