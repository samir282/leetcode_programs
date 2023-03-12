class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for char in s:
            print(ord(char))
            string+= str(ord(char) - 96)
        digit_sum = int(string)
        for i in range(1,k+1):
            number = digit_sum
            digit_sum = 0
            while number > 0:
                digit = number % 10
                digit_sum += digit
                number //= 10
        return digit_sum