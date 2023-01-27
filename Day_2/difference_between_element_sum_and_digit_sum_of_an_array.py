class Solution:
    def difference_of_sum(self, nums: list) -> int:
        s = sum(nums)
        t = 0
        for x in nums:
            while x > 0:
                t += x % 10
                x //= 10
        return abs(s - t)


sol = Solution()
nums = [1, 15, 6, 3]


result = sol.difference_of_sum(nums)
print(result)
