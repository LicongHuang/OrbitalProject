import nacl.secret


def test():
    key = open("code.pass", mode="rb").read()[:32]


    cipher = nacl.secret.SecretBox(key)

    plaintext = b"Hello world"

    ciphertext = cipher.encrypt(plaintext)

    print(plaintext)

    print(ciphertext)

    print(cipher.decrypt(ciphertext))


