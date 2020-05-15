import collections
import unittest


class TestStringMethods(unittest.TestCase):

    def test_all(self):
        nums = [1, 2, 3, 4, 4, 4, 2, 1, 1]
        freq = collections.Counter(nums)
        print(freq)

        # Traditional approach for counting frequency
        freq2 = {}
        for n in nums:
            if n not in freq2:
                freq2[n] = 0
            freq2[n] += 1

        freq3 = {}
        for n in nums:
            freq3[n] = freq3.get(n, 0) + 1

        self.assertEqual(freq, freq2)
        self.assertEqual(freq, freq3)


if __name__ == '__main__':
    unittest.main()
