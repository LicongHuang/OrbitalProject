import os


def set_password():
    if os.path.exists(".password"):
        print("Password already set!")
        return
    print("Setting password...")
    password = input("Enter password: ")
    
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





