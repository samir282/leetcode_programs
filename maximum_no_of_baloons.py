class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bal = "baloon"
        if len(text) < len(bal):
            return 0
        for char in text:
            if char not in bal:
                index = text.index(char)
                text = text[:index] + text[index+1:]
        print(text)
        text_dict = {}
        for char in text:
            if char not in text_dict:
                text_dict[char] = 1
            else:
                text_dict[char]+=1
        min_value = min(text_dict.values())
        print(min_value)
        print(text_dict['l'])
        print(text_dict['o'])
        if  text_dict['l'] >= 2*min_value and text_dict['o'] >= 2*min_value:
            return min_value
        if text_dict['l']<text_dict['o']:
            return text_dict['l']//2
        else:
            return text_dict['o']//2
