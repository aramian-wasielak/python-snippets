import collections
import unittest


class TestArrayMethods(unittest.TestCase):

    def test_all(self):
        """
        Test array related snippets
        """

        # TODO: graph = collections.defaultdict(set)

        nums = [1, 2, 3, 4, 4, 4, 2, 1, 1]

        # Fastest (from coding perspective)
        freq = collections.Counter(nums)
        print(freq)

        # Traditional approach for computing frequency
        freq2 = {}
        for n in nums:
            if n not in freq2:
                freq2[n] = 0
            freq2[n] += 1

        # Simillar to the one above but no 'if' statement needed
        freq3 = {}
        for n in nums:
            freq3[n] = freq3.get(n, 0) + 1

        self.assertEqual(freq, freq2)
        self.assertEqual(freq, freq3)


if __name__ == '__main__':
    unittest.main()
