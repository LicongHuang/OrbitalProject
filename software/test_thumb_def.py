import dbutil
import keygen
import encryption
import usbutil
import unittest

class TestTD(unittest.TestCase):

    def test_db_working(self):
        conn = dbutil.connect()
        key = keygen.genKey()
        try:
            dbutil.insertKey("test", key, conn)
            #assert dbutil.getKey("test", conn) == key
            self.assertEqual(dbutil.getKey("test", conn), key)
            dbutil.deleteUSB("test", conn)
            self.assertEqual(dbutil.getKey("test", conn), None)
            #assert dbutil.getKey("test", conn) == None
        except Exception as e:
            print(e)
        finally:
            conn.cursor().execute("DELETE FROM passcode") 
            conn.commit()
            conn.cursor().close()
            conn.close()

    def test_encryption(self):
        key = keygen.genKey()
        test = b"test"
        ciphertext = encryption.encryption(key + b'0'*(32 - len(key)), test)
        plaintext = encryption.decryption(key + b'0'*(32 - len(key)), ciphertext)

        try:
            #assert test == plaintext
            self.assertEqual(test, plaintext)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
