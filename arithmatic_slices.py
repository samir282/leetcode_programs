class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        if length<3:
            return 0
        counter = 0
        for i in range(0,length-2,1):
            for j in range(i+1,length-1,1):
                if nums[j-1]-nums[j] == nums[j]- nums[j+1]:
                    counter+=1
                else:
                    break
        return counter