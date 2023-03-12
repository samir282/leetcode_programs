class Solution:
    def reverse(self, x: int) -> int:
        # reverse_num = 0
        if x < 0:
            num = x*(-1)
        else:
            num = x

        str_num = str(num)
        reverse_str = str_num[::-1]
        print(reverse_str)
        # while num>0:
        #     rem = num % 10
        #     reverse_num = reverse_num*10+rem
        #     num//=10
        #     print(reverse_num)
        reverse_num = int(reverse_str)
        if reverse_num > 2**(31) - 1:
            return 0
        if x < 0:
            return reverse_num*(-1)
        else:
            return reverse_num
