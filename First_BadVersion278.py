class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n

        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid):
                flag = mid
                right = mid-1
            else:
                left = mid+1
        return flag