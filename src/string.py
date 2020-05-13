
def test_string():
    # multiple ways to reverse a string
    s = 'abcdefghijk'
    s.reverse()
    t = reversed(s)
    t = s[::-1]

    assert