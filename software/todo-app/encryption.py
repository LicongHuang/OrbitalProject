import nacl.secret
import os
import PoC

def test():
    key = open("code.pass", mode="rb").read()[:32]


    cipher = nacl.secret.SecretBox(key)

    plaintext = open("tut01qns.pdf", mode="rb").read()

    ciphertext = cipher.encrypt(plaintext)

    #print(plaintext)

    #print(ciphertext)

    #print(cipher.decrypt(ciphertext))

    print(plaintext == cipher.decrypt(ciphertext))


def getKey():
    os.system("head -1 /dev/urandom | base64 > code.pass")
    key = open("code.pass", mode="rb").read()[:32]
    return key

def encryption(file):
    key = PoC.genKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = file
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decryption(file):
    # file is a filename
    key = getKey()
    cipher = nacl.secret.SecretBox(key)
    plaintext = cipher.decrypt(file)
    return plaintext 
