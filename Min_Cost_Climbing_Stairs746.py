class Solution:
    def smallest(nums,i,j) -> int:
        if nums[i]<nums[j]:
            return nums[i]
        else:
            return nums[j]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        if l<=2:
            return min(cost)
        i = 2
        while i<l:
            cost[i]+= Solution.smallest(cost,i-1,i-2)
            i+=1
        return Solution.smallest(cost,i-1,i-2)