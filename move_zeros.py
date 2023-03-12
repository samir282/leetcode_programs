class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # c=0
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         nums.remove(i)
        #         c=c+1
        # for i in range(c):
        #     nums.insert(-1,0)

        i = 0
        while True:
            if 0 in nums:
                i += 1
                nums.remove(0)
                continue
            break
        for j in range(i):
            nums.append(0)

