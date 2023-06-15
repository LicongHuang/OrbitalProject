import dbutil
import encryption
import usbutil



def encryptFiles():
    #conn = dbutil.connect()
    ID = usbutil.getUSBID()
    filepath = usbutil.getUSBFilePath() + '/'
    files = usbutil.getFiles()
    key = dbutil.useKey(ID)

    for file in files:
        if file.endswith('.td'):
            continue
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
    key = dbutil.useKey(ID)

    for file in files:
        if not file.endswith('.td'):
            continue
        binfile = open(filepath + file, mode="rb").read()
        plaintext = encryption.decryption(key, binfile)
        encryption.makeDecryptedFile(filepath + file, plaintext)
        encryption.removeFile(filepath + file)
    print("Completed decryption")
    #dbutil.disconnect(conn)
