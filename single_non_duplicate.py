class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        first = 0
        last = len(nums)-1
        if last == 0:
            return nums[0]
        while first<=last:
            if nums[first] != nums[first+1]:
                return nums[first]
            else:
                first+= 2

            if nums[last]!= nums[last-1]:
                return nums[last]
            else:
                last-=2