class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        list=[]
        start= 0
        end = 0
        max=0
        for char in s:
            if char not in list:
                start+=1
                list.append(char)
                if (len(list))>max:
                    max= len(list)
                print(max)
            else:
                del list[:list.index(char)+1]
                list.append(char)
        return max