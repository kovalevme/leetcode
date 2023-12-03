class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for el in reversed(s.split(' ')):
            if len(el) > 0:
                return len(el)
