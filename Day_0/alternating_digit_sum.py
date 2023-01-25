class Solution:
    def alternate_digit_sum(self, n: int) -> int :
        sign = 1
        total = 0
        for x in (str(n)):
            toatal += sign * int(x)
            sign *= -1
        return total