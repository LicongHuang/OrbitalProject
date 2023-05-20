import nacl.secret
import os
import poc

def test():
    key = getKey()


    cipher = nacl.secret.SecretBox(key)

    plaintext = open("usb_test/tut01qns.pdf", mode="rb").read()

    ciphertext = cipher.encrypt(plaintext)

    #print(plaintext)

    #print(ciphertext)

    #print(cipher.decrypt(ciphertext))

    print(plaintext == cipher.decrypt(ciphertext))


def getKey():
    os.system("head -1 /dev/urandom | base64 > code.pass")
    key = open("key.key", mode="rb").read()[:32]
    return key

def encryption(file):
    key = poc.genKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = file
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def getFromUSB(state):
    # state
    if state == 1:
        print(list(os.scandir("./usb_test")))

def makefile(filename, ciphertext):
    f = open(f"{filename}.td", mode="wb")
    f.write(filename) 
    f.close()


def decryption(file):
    # file is a filename
    key = getKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = cipher.decrypt(file)
    return plaintext 
