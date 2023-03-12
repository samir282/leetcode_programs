class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs, key=len)
        strs.pop(shortest_string)
        char_index = 0
        prefix_str= ""
        flag = 1
        while char_index < len(shortest_string):
            for string in strs:
                if shortest_string[char_index] != string[char_index]:
                    flag = 0
            if flag == 1:
                prefix_str+=shortest_string[char_index]
            else:
                return prefix_str
            char_index+=1
        return prefix_str


