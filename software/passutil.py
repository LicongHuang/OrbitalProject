import os


def check_password_file():
    if os.path.exists(".password"):
        return True
    else:
        return False

def set_password():
    if check_password_file():
        print("Password already set")
        return
    password = input("Enter password: ")
    
    reenter = input("Re-enter password: ")

    if password != reenter:
        print("Passwords do not match")
        return set_password()

    infile = open(".password", "w")
    infile.write(password)
    infile.close()

def get_password():
    infile = open(".password", "r")
    password = infile.read()
    infile.close()
    return password

def check_password():
    password = input("Enter password: ")
    if password == get_password():
        return True
    else:
        return False





