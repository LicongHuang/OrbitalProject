import os
import encryption
from os.path import join, getsize
import subprocess
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

def fileWalk2(path):
    #infile = open("filelist.txt", "w")
    # fileWalk2("/media/orangepi/'CYX PROJECT'")
    # fileWalk2('/media/orangepi/"CYX PROJECT"')
    print("Path: ", path)
    command = f"ls -R {path}"
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    output = output.decode("utf-8")
    formatted = formatingFileList(output)
    #print(formatted)
    return formatted

def formatFileSpaces(w):
    f = w.split('/')
    w = ''
    for i in f:
        if i == '':
            continue
        if ' ' in i:
            w += '/' + "'" + i + "'"
        else:
            w += '/' + i
    return w
    

def formatingFileList(out):
    folders = out.split('\n\n')
    filepaths = []

    for i in range(len(folders)):
        f0 = folders[i].split('\n')
        filepath = ""
        for f in f0:

            if ":" in f:
                filepath = formatFileSpaces(f[:-1])

            if "." not in f:
                continue

            if " " in f:
                filepaths.append(filepath + "/" + '"' + f + '"')
            else:
                filepaths.append(filepath + "/" + f)

    print(filepaths)
    return filepaths

# Will implement the function later when on the hardware
# should find the usb from the usb ports
def getUSBFilePath():
    # temp filefatih
    output = ""
    while output == "":
        output = subprocess.check_output('ls /media/orangepi/', shell=True)
        print("Waiting for USB device...")
        output = output.decode("utf-8").strip() 
    return "/media/orangepi/usb"

    

def getFiles():
    filepath = getUSBFilePath()
    filepath = "/media/orangepi/usb"
    return fileWalk2(filepath)

if __name__ == "__main__":
    print(getFiles())
