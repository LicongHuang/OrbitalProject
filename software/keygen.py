import os

def genKey():

    command = "head -1 /dev/random > key.key"
    os.system(command)
    infile = open('key.key',mode='rb')
    random_line = infile.read()[:32]
    os.system("rm key.key")
    infile.close() 
    return random_line
