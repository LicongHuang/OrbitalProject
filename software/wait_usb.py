import pyudev
import subprocess
import dbutil
import usbutil
import os

def add_usb(usb_id):
    filepath = usbutil.getFileInMedia()
    usb_id = filepath.split('/')[-1]
    print(usb_id)
    dbutil.useKey(usb_id) # returns a key but not used
    print(f"{usb_id} device added")

def getIdentifier():
    osout = subprocess.check_output("lsblk -o MOUNTPOINT | grep -i '/media/orangepi/'", shell=True)
    a = osout.decode("utf-8")
    print(a)
    return a;

def check_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    os.system("sudo mkdir /media/orangepi/usb")
    
    # Check if USB is already mounted
    a = getIdentifier()
    mounted = os.system("sudo mount /dev/sda1 /media/orangepi/usb")
    if mounted == 0:
        add_usb(a)
        return
    
    # Wait for USB to be plugged in
    for device in iter(monitor.poll, None):
        if device.action == 'add':
            print('{} connected'.format(device))
            #Making a mounting point
            os.system("sudo mount /dev/sda1 /media/orangepi/usb")
            
            add_usb(a)
            return
        elif device.action == 'remove':
            print('{} disconnected'.format(device))

#def check_usb2():
#    while True:
#        try:
#            output = subprocess.check_output("lsblk -o MOUNTPOINT | grep -i '/media/orangepi/'", shell=True)
#            output = output.decode('utf-8')
#            print(output)
#            ret = subprocess.check_output("sudo umount {}".format(output), shell=True)
#            if output:
#                add_usb()
#                return
#    
#        except subprocess.CalledProcessError:
#            print("No USB device found")
#    
#    #finally:
#    #    check_usb()




if __name__ == "__main__":
    check_usb()
