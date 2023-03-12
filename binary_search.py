class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # return -1
        len = len(nums)
        start = 0
        end = len
        while start<end:
            mid = (start+end)/2
            if nums[mid] == target :
                return mid
            if target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return -1
