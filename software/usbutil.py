# Author: Huang Licong
# USB utility code base
import os
import encryption
from os.path import join, getsize
import subprocess
# This is a function to get the file from the USB

# state: 1 for getting the file from the USB

# Gets all files
def fileWalk(path):
    filesList = []

    for root, dirs, files in os.walk(path):
        print(root)
        print(files)
        for file in files:
            filesList.append(os.path.join(root, file))
    return filesList

# Get alls files v2
def fileWalk2(path):
    #infile = open("filelist.txt", "w")
    # fileWalk2("/media/orangepi/'CYX PROJECT'")
    # fileWalk2('/media/orangepi/"CYX PROJECT"')
    #print("Path: ", path)
    command = f"ls -R {path}"
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    output = output.decode("utf-8")
    formatted = formatingFileList(output)
    print(formatted)
    print("Format finish")
    return formatted

# Formats file path into terminal legal version
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
    
# Formats files into a list
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
                continue #<- does werid stuff if we try to get it working
                
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
        output = subprocess.check_output('ls /media/orangepi/usb', shell=True)
        print("Waiting for USB device...")
        output = output.decode("utf-8").split('\n')
        for out in output:
            if out == 'usb':
                pass
        outter = out
    return "/media/orangepi/usb/'{}'".format(outter)

    
# Get some file path
def getFiles():
    filepath = getUSBFilePath()
    filepath = "/media/orangepi/usb"
    return fileWalk2(filepath)

# Get the filepath for the USB mount
def getFileInMedia():
    files = subprocess.check_output("lsblk -o MOUNTPOINT | grep -i /media/orangepi/", shell=True)
    filepaths = files.decode('utf-8');
    print("The file path is " , filepaths)
    filepaths = filepaths.split('\n')
    for filepath in filepaths:
        if not "usb" in filepath and "/" in filepath:
            print(filepath)
            return filepath
    

if __name__ == "__main__":
    #print(getFiles())
    print(getFileInMedia())
