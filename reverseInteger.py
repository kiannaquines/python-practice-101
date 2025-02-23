class Solution:
    def reverse(self, x:int) -> int:
        sign = -1 if x < 0 else 1
        reversedInteger = int(str(abs(x))[::-1]) * sign
        return reversedInteger

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-233))
print(solution.reverse(-1233))