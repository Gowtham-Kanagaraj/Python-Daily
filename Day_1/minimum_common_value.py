class Solution:
    def get_common(self, num_1: list, num_2: list) -> int:
        s = set(num_2)
        num_1.sort()

        for x in num_1:
            if x in s:
                return x
        return -1


sol = Solution()
num_1 = [1, 2, 3]
num_2 = [2, 4]

result = sol.get_common(num_1, num_2)
print(result)
