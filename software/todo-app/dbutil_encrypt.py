import dbutil
import encryption
import usbutil



def encryptFiles():
    #conn = dbutil.connect()
    ID = usbutil.getUSBID()
    filepath = usbutil.getUSBFilePath() + '/'
    files = usbutil.getFiles()
    key = dbutil.useKey(ID)
    print(len(key))

    for file in files:
        binfile = open(filepath + file, mode="rb").read()
        ciphertext = encryption.encryption(key, binfile)
        encryption.makeEncryptedFile(filepath + file, ciphertext)
        encryption.removeFile(filepath + file)
    print("Completed encryption")
    #dbutil.disconnect(conn)
    
def decryptFiles():
    #conn = dbutil.connect()
    ID = usbutil.getUSBID()
    filepath = usbutil.getUSBFilePath() + '/'
    files = usbutil.getFiles()
    key = dbutil.useKey(ID)[0]
    print(type(key))

    for file in files:
        binfile = open(filepath + file, mode="rb").read()
        plaintext = encryption.decryption(key, binfile)
        encryption.makeDecryptedFile(filepath + file, plaintext)
        encryption.removeFile(filepath + file)
    print("Completed decryption")
    #dbutil.disconnect(conn)

