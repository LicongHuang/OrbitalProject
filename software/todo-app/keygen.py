import os

def genKey():

    command = "head -1 /dev/random > key.key"
    os.system(command)

    random_line = open('key.key',mode='rb').read()[:32]

    return random_line
