import os
import encryption
from os.path import join, getsize
# This is a function to get the file from the USB
# state: 1 for getting the file from the USB


def fileWalk(path):
    filesList = []
    for root, dirs, files in os.walk(path):
        print(root)
        print(files)
        for file in files:
            filesList.append(os.path.join(root, file))
    return filesList

# Will implement the function later when on the hardware
# should find the usb from the usb ports
def getUSBFilePath():
    # temp filefath
    return "/media/orangepi2/"

def getUSBID():
    return ""


def getFiles():
    filepath = getUSBFilePath()
    return fileWalk(filepath)

if __name__ == "__main__":
    print(getFiles())
