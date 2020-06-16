import collections
import unittest


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_left(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
            return mid
        elif target <= nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_right(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid == (len(nums) - 1) or nums[mid + 1] != target):
            return mid
        elif nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


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

        # Similar to the one above but no 'if' statement needed
        freq3 = {}
        for n in nums:
            freq3[n] = freq3.get(n, 0) + 1

        self.assertEqual(freq, freq2)
        self.assertEqual(freq, freq3)

    def test_binary_search(self):
        nums = [1, 3, 4, 4, 4, 5, 7, 9]
        self.assertEqual(binary_search(nums, 3), 1)
        self.assertEqual(nums[binary_search(nums, 4)], 4)
        self.assertEqual(binary_search(nums, 9), 7)
        self.assertEqual(binary_search(nums, 1), 0)
        self.assertEqual(binary_search(nums, 6), -1)

    def test_leftmost_search(self):
        nums = [1, 3, 4, 4, 4, 5, 7, 9]
        self.assertEqual(binary_search_left(nums, 3), 1)
        self.assertEqual(binary_search_left(nums, 4), 2)
        self.assertEqual(binary_search_left(nums, 9), 7)
        self.assertEqual(binary_search_left(nums, 1), 0)
        self.assertEqual(binary_search_left(nums, 6), -1)

    def test_rightmost_search(self):
        nums = [1, 3, 4, 4, 4, 5, 7, 9]
        self.assertEqual(binary_search_right(nums, 3), 1)
        self.assertEqual(binary_search_right(nums, 4), 4)
        self.assertEqual(binary_search_right(nums, 9), 7)
        self.assertEqual(binary_search_right(nums, 1), 0)
        self.assertEqual(binary_search_right(nums, 6), -1)


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
