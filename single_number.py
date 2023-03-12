class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        list_dict = {}
        for num in nums:
            if list_dict.__contains__(num):
                list_dict[num]+=1
            else:
                list_dict[num] = 1
        for key, value in list_dict.items():
            if value == 1:
                return key