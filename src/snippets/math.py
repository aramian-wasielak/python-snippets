import unittest


class TestMathMetods(unittest.TestCase):
    # TODO:
    #  - intersection of sets: a[i].intersection(b[j]):
    #  - caching/memoizing: functools.lru_cache
    #  - combinantions itertools.permutations
    #  - random.randint(a, b)

    def test_add_strings(self):
        s1 = "1234"
        s2 = "111"
        test_ans = "1345"

        base = 10
        n1 = len(s1)
        n2 = len(s2)

        change = 0
        i = 0
        ans = ""
        while (0 < change) or (i < n1) or (i < n2):
            if i < n1:
                change += int(s1[n1 - i - 1])

            if i < n2:
                change += int(s2[n2 - i - 1])

            ans = str(change % base) + ans
            change = change // base
            i += 1

        self.assertEqual(test_ans, ans)


if __name__ == "__main__":
    unittest.main()
