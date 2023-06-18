import os
import dbutil

# Get default USB list on startup
cmd = 'lsusb > usb_default_list.txt'
res = os.system(cmd)

infile = open('usb_default_list.txt', 'r')

for line in infile:
    usb_id = line.split(' ')
    usb_id = usb_id[1] + usb_id[5]
    print(line)
    dbutil.insertKey(usb_id, 'default', dbutil.connect())
infile.close()

