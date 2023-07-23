import sys
import dbutil_encrypt
import authentication
import wait_usb
import newkeypadcode
import subprocess

import sys

def poc():
    try:
        print("write something")
        message1 = newkeypadcode.keypadInput()
        print("again1")
        message2 = newkeypadcode.keypadInput()
        print("again2")
        message3 = newkeypadcode.keypadInput()
        print("message1 is:")
        print(message1)
        print("message2 is:")
        print(message2)
        print("message3 is:")
        print(message3)

    except KeyboardInterrupt:
        print("Exiting...")
        lcd.exit_c()
        sys.exit(1)

    except Exception as e:
        print(e)
        # sys.exit(1)

def main():
    poc()


if __name__ == '__main__':
    main();
