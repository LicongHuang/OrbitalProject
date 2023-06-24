import os
import newkeypadcode

def check_password_file():
    if os.path.exists(".password"):
        return True
    else:
        return False

def set_password():
    if check_password_file():
        print("Password already set")
        return
    print("Enter password: ")

    password = newkeypadcode.keypadInput()
    print("Reenter password: ")
    reenter = newkeypadcode.keypadInput()

    if password != reenter:
        print("Passwords do not match")
        return set_password()
    
    if password == None:
        password = ""

    infile = open(".password", "w")
    infile.write(password)
    infile.close()

def get_password():
    infile = open(".password", "r")
    password = infile.read()
    infile.close()
    return password

def check_password():
    print("Enter password to login: ")
    password = newkeypadcode.keypadInput()
    if password == get_password():
        return True
    else:
        return False





