class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split(" ")
        print(list)
        final_list= []
        for str in list :
            final_list.append(str[::-1])
        single_string = " ".join(final_list)
        return single_string