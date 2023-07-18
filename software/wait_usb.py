import pyudev
import subprocess
import dbutil
import usbutil
import os

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
        osout = os.system("lsblk -o MOUNTPOINT | grep -i '/media/orangepi/'")
        if osout == 0:
            add_usb()
            return
        if device.action == 'add':
            print('{} connected'.format(device))
            #Making a mounting point
            os.system("sudo mkdir /media/orangepi/{}".format(device.sys_name))
            os.system("sudo mount /dev/sda /media/orangepi/{}".format(device.sys_name))
            
            add_usb()
            return
        elif device.action == 'remove':
            print('{} disconnected'.format(device))

def check_usb2():
    while True:
        try:
            output = subprocess.check_output("lsblk -o MOUNTPOINT | grep -i '/media/orangepi/'", shell=True)
            output = output.decode('utf-8')
            print(output)
            ret = subprocess.check_output("sudo umount {}".format(output), shell=True)
            if output:
                add_usb()
                return
    
        except subprocess.CalledProcessError:
            print("No USB device found")
    
    #finally:
    #    check_usb()




if __name__ == "__main__":
    check_usb()
