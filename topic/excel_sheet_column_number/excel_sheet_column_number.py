class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for char in columnTitle:
            number = number * 26 + (ord(char) - ord('A') + 1)
        return number
