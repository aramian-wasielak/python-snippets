import unittest


class TestStringMethods(unittest.TestCase):

    def test_window(self):
        """
        Processing a string while maintaining a moving window of characters.
        """
        s = "abcdeg"
        win_size = 3

        ns = len(s)
        win_start = 0
        windows = []
        for i in range(ns):
            # Process a new char
            win_end = i

            if i >= win_size:
                # Remove a character from the window
                win_start += 1

            # Process the current window once the window is of the right size
            if i >= win_size - 1:
                windows.append(s[win_start: win_end + 1])

        correct_windows = ["abc", "bcd", "cde", "deg"]
        self.assertEqual(correct_windows, windows)

    def test_reverse(self):

        # How to reverse a string
        s = 'abcdefghijk'

        # Calling 'reversed' returns a reverse iterator
        s2 = ''.join(reversed(s))
        s3 = s[::-1]
        self.assertEqual(s2, s3)

        # Converting characters to their relative alphabet
        self.assertEqual((ord('c') - ord('a')), 3 - 1)

        # Converting from an ASCI character and back to a character
        self.assertEqual(chr(ord('a')), 'a')


if __name__ == '__main__':
    unittest.main()
