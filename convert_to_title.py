class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        str = ""
        while columnNumber>0:
            reminder = columnNumber % 26
            char = chr(reminder + 64)
            str = char + str
            columnNumber/=26