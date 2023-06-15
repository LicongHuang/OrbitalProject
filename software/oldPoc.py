import dbutil_encrypt
import sys

if __name__ == '__main__':
    dbutil_encrypt.encryptFiles()
    print('Encrypting files...')
    dbutil_encrypt.decryptFiles()
    print('Decrypting files...')
