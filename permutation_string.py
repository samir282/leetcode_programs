class Solution:

    def prime_product(string:str, alphabate_dict: dict):
        product=1
        for char in string:
            product = product * alphabate_dict[char]
        return product

    def checkInclusion(self, s1: str, s2: str) -> bool:

        alphabate_dict = {'a' : 2, 'b' : 3, 'c': 5, 'd' : 7, 'e' : 11, 'f': 13, 'g' : 17, 'h' : 19, 'i' : 23, 'j' : 29, 'k' : 31, 'l' : 37, 'm' : 41, 'n' : 43, 'o' : 47, 'p' : 53, 'q' : 59, 'r' :61 , 's' : 67, 't' : 71, 'u': 73, 'v' : 79, 'w' : 83, 'x' : 89, 'y' : 97, 'z' : 101}
        s1_product = Solution.prime_product(s1,alphabate_dict)

        # print(s1_product)

        i= 0
        l2= len(s2)
        l1= len(s1)

        while i < l2-l1+1:
            str= s2[i:i+l1]
            i+=1
            s2_product = Solution.prime_product(str, alphabate_dict)
            if(s1_product == s2_product):
                return True

        return False