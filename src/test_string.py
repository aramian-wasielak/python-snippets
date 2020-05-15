import unittest


class TestStringMethods(unittest.TestCase):

    def test_all(self):

        # How to reverse a string
        s = 'abcdefghijk'

        # Calling 'reversed' returns a reverse iterator
        s2 = ''.join(reversed(s))
        s3 = s[::-1]
        self.assertEqual(s2, s3)

        # Converting characters to their relative alphabet
        self.assertEqual((ord('c') - ord('a')), 3-1)

        # Converting from an ASCI character and back to a character
        self.assertEqual(chr(ord('a')), 'a')


if __name__ == '__main__':
    unittest.main()
