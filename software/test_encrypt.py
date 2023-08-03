# Author: Huang Licong
# test file
import dbutil
import encryption

# This is the initialisation test for encryption
if __name__ == "__main__":
    filepath = './usb_test/some.txt'
    ID = 'usb_test'
    key = dbutil.useKey(ID)
    file = open(filepath, 'rb')
    output = file.read()
    ciphertext = encryption.encryption2(key, output)
    file.close()
    encryption.makeEncryptedFile(filepath, ciphertext)
    defile = open(filepath+'.td', 'rb')
    ciphertext = defile.read()
    plaintext = encryption.decryption2(key, ciphertext)
    encryption.makeDecryptedFile(filepath+'.td', plaintext)
    print("Encryption complete")

