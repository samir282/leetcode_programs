class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        odd_dict = {}
        odd_max = 0
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char]+=1
        print(char_dict)

        result = 0
        for key, value in char_dict.items():
            # print(key)
            if value%2 == 0:
                result+= value
            else:
                odd_dict[key] = value
                if value>odd_max:
                    odd_max = value
        print(result)
        if odd_max == 0:
            return result
        # print(odd_max)
        
        for key, value in odd_dict.items():
            if value==1:
                pass
            else:
                result+= value-1
        result+=1
        # print(odd_dict)
        return result
