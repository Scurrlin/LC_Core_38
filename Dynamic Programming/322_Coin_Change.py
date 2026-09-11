class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = amount
        dp = [a + 1] * (a + 1)
        dp[0] = 0

        for c in coins:
            for i in range(c, a + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[a] if dp[a] != a + 1 else -1