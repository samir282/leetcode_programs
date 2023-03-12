from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) is 0:
            return list(digits)

        phone_dict = {'2':"abc" , '3':"def" , '4':"ghi" , '5':"jkl" , '6':"mno" , '7':"pqrs" , '8':"tuv" , '9':"wxyz"}

        if len(digits)==1:
            return list(phone_dict[digits])

        digit_string = []
        for digit in digits:
            digit_string.append(phone_dict[digit])

        combinations = list(product(*digit_string)) #combination is a list of tuples

        #converting into string of list
        combination_list = []
        for combination in combinations:
            combination_list.append("".join(combination))
            
        return combination_list
