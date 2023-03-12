class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        # print(nums)
        last = len(nums)-1
        max = nums[last]
        print(max)
        # print(largetst)
        for i in range(last-1,-1,-1):
            total=sum(nums[0:i+1])
            print(total)
            if total<max:
                return False
            print(total)
            if total == max:
                return True
            if total>max:
                last-=1
                max=max+nums[last]
        return False
