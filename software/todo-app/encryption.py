# Maintainer: Huang Licong
import nacl.secret
import os
import poc


# This is just an example and a test
def test():

    key = getKey()

    cipher = nacl.secret.SecretBox(key)

    plaintext = open("usb_test/tut01qns.pdf", mode="rb").read()

    ciphertext = cipher.encrypt(plaintext)

    #print(plaintext)

    #print(ciphertext)

    #print(cipher.decrypt(ciphertext))

    print(plaintext == cipher.decrypt(ciphertext))

    print(encryption(plaintext) == ciphertext)
    print(decryption(ciphertext) == plaintext)

# This gets the first line from /dev/random and base64 encodes it
# Then it gets the first 32 bytes of the key
# This is the key used for encryption
def getKey():
    os.system("head -1 /dev/urandom | base64 > code.pass")
    key = open("key.key", mode="rb").read()[:32]
    return key

# This is the encryption function
# file: the file to be encrypted
def encryption(file):
    key = poc.genKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = file
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# This is a function to get the file from the USB
# state: 1 for getting the file from the USB

def getFromUSB(state):
    # TODO get the USB file actually working and read the list of the folder
    if state == 1:
        print(list(os.scandir("./usb_test")))


# This is a function to make the file
# filename: the name of the file
# ciphertext: the ciphertext of the file
def makefile(filename, ciphertext):
    # TODO make the function actually working
    f = open(f"{filename}.td", mode="wb")
    f.write(filename) 
    f.close()

# This is a function to decrypt the file
# file: the file to be decrypted
def decryption(file):
    key = getKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = cipher.decrypt(file)
    return plaintext 
