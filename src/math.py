
def add_strings(s1, s2, base):
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

    return ans
