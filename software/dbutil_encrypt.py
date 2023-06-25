import dbutil
import encryption
import usbutil
import shutil



def encryptFiles():
    #conn = dbutil.connect()
    #ID = usbutil.getUSBID()
    filepath = usbutil.getUSBFilePath() + '/'
    ID = filepath.split('/')[-2]
    files = usbutil.getFiles()
    key = dbutil.useKey(ID)
    print('From encryptFiles: ')
    print(files)
    for file in files:
        if file.endswith('.td'):
            continue
        newfile = "~/OrbitalProject/software/usb_test" + file.split('/')[-1]
        shutil.copy(file, newfile)
        binfile = open(newfile, mode="rb").read()
        ciphertext = encryption.encryption(key, binfile)
        encryption.makeEncryptedFile(file, ciphertext)
        encryption.removeFile(file)
        encryption.removeFile(file)
    print("Completed encryption")
    #dbutil.disconnect(conn)
    
def decryptFiles():
    #conn = dbutil.connect()
    #ID = usbutil.getUSBID()
    filepath = usbutil.getUSBFilePath() + '/'
    ID = filepath.split('/')[-2]
    files = usbutil.getFiles()
    key = dbutil.useKey(ID)
    print(files)
    for file in files:
        if not file.endswith('.td'):
            continue
        binfile = open(file, mode="rb").read()
        plaintext = encryption.decryption(key, binfile)
        encryption.makeDecryptedFile(file, plaintext)
        encryption.removeFile(file)
    print("Completed decryption")
    dbutil.deleteUSB(ID, dbutil.connect()) 
    #dbutil.disconnect(conn)

