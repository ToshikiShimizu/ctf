import unittest

class TestCipher(unittest.TestCase):
    def test_cipher(self):
        self.assertEqual(cipher('abc',3),'def')
        self.assertEqual(cipher('ABC',3),'DEF')
        self.assertEqual(cipher('aA_{}',1),'bB_{}')
        self.assertEqual(cipher('zZ',1),'aA')

def cipher(text, n):
    result = ''
    for c in text:
        if c.isupper():
            result += chr((ord(c) + n - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) + n - 97) % 26 + 97)
        else:
            result += c
    return result

if __name__ == '__main__':
    unittest.main()