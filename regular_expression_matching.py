class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        char_frequency = {}
        for char in s:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        for c in p:
            if char_frequency.__contains__(c) or c== '.' or c== '*':
                x=1
            else:
                return False
        return True
