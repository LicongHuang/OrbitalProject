import pyudev
import os
import dbutil
import usbutil

def add_usb():
    filepath = usbutil.getUSBFilePath()
    usb_id = filepath.split('/')[2]
    dbutil.useKey(usb_id) # returns a key but not used
    print("USB device added")

def check_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            print('{} connected'.format(device))
            add_usb()
            return
        elif device.action == 'remove':
            print('{} disconnected'.format(device))



if __name__ == "__main__":
    while True:
        check_usb()
