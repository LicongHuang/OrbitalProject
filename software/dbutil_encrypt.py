import dbutil
import encryption
import usbutil
import subprocess



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
        command = "cat " + file
        output = subprocess.check_output(command, shell=True)
        #binfile = open(file, mode="rb").read()
        ciphertext = encryption.encryption2(key, output)

        encryption.makeEncryptedFile2(file, ciphertext)
        encryption.removeFile2(file)
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
    print("ID for key: ", ID)
    for file in files:
        if not file.endswith('.td'):
            continue
        command = "cat " + file
        output = subprocess.check_output(command, shell=True)
        #binfile = open(file, mode="rb").read()
        plaintext = encryption.decryption(key, output) #previously output is binfile
        encryption.makeDecryptedFile2(file, plaintext)
        encryption.removeFile2(file)
    print("Completed decryption")
    dbutil.deleteUSB(ID, dbutil.connect()) 
    #dbutil.disconnect(conn)

