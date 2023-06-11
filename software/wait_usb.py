import pyudev
import os
import dbutil


def add_usb():
    os.system("lsusb > usb_list.txt")

    with open("usb_list.txt", "r") as f:
        for line in f:
            usb_id = line.split()
            usb_id = usb_id[1] + usb_id[5]
            dbutil.useKey(usb_id) # returns a key but not used
            

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
