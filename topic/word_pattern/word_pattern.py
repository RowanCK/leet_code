class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        exist_word = {}
        exist_pattern = {}

        for idx, c in enumerate(pattern):
            if c in exist_pattern and exist_pattern[c] != words[idx]:
                return False
            if words[idx] in exist_word and exist_word[words[idx]] != c:
                return False
            exist_pattern[c] = words[idx]
            exist_word[words[idx]] = c

        return True

class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return (len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))))
