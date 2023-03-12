class Solution:
    def sum_digits(n:int) -> int:
        total=0
        while n>0:
            r=n%10
            total+=r
            n//=10
        return total
    def countLargestGroup(self, n: int) -> int:
        my_dict= dict()
        for num in range(1,n+1):
            sum = Solution.sum_digits(num) 
            if sum in my_dict:
                my_dict[sum]+=1
            else:
                my_dict.setdefault(sum,1)
        print(my_dict)
        max_value = max(my_dict.values())
        count = 0
        for value in my_dict.values():
            if value == max_value:
                count += 1
        return count

