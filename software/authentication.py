import passutil

def auth():
    if passutil.check_password_file():
        user_input = input("Enter password: ")
        if user_input == passutil.get_password():
            print("Password accepted")
            #pass control to something else
            return True
        else:
            print("Invalid password")
    
    else:
        print("Password not set yet")
        passutil.set_password()
        print("Password set")
        #pass control to something else
        return auth
    return False

if __name__ == "__main__":
    auth()
