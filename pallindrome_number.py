class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        value=1
        while num is not 0:
            r=num%10
            value*=10+r
            num //=10
        return value == x
