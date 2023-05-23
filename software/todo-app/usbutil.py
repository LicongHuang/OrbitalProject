import os
import encryption

# This is a function to get the file from the USB
# state: 1 for getting the file from the USB

def getFilesUSB(filepath):
    # TODO get the USB file actually working and read the list of the folder
    ls = list(os.scandir(filepath))
    ls = [entry.name for entry in ls]
    print(ls)
    return ls


# Will implement the function later when on the hardware
# should find the usb from the usb ports
def getUSBFilePath():
    # temp filefath
    return "./usb_test"

def getUSBID():
    return "1"


def getFiles():
    filepath = getUSBFilePath()
    return getFilesUSB(filepath)

