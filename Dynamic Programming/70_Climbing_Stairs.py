class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one, two = 2, 1
        for _ in range(3, n + 1):
            current = one + two
            two = one
            one = current
        return one