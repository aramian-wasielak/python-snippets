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

    def test_binary_search(self):
        nums = [1, 3, 4, 5, 7, 9]
        left = 0
        right = len(nums)

    def test_leftmost_search(self):
        pass


if __name__ == "__main__":
    unittest.main()
    """
    Ability to rewrite a number of strings at the same time is useful.
            S = list(S)
        
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i: i+len(x)] == list(x):
                S[i: i+len(x)] = list(y)
            
        return ''.join(S)

    """
