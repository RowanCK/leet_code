from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen.add(substring)

        return list(repeated)

# Bitmask
def findRepeatedDnaSequences2(s: str) -> list[str]:
    encode = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    count = {}
    ans = []

    mask = (1 << 20) - 1
    code = 0

    for i, ch in enumerate(s):
        code = ((code << 2) | encode[ch]) & mask

        if i < 9:
            continue

        if count.get(code, 0) == 1:
            ans.append(s[i-9:i+1])

        count[code] = count.get(code, 0) + 1

    return ans
