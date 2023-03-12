class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_list = []
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)
                flag = 0
                for j in range(index+1, len(nums2)):
                    if nums2[j] > i:
                        final_list.append(nums2[j])
                        flag = 1
                        break
                if flag == 0:
                    final_list.append(-1)
        return final_list
