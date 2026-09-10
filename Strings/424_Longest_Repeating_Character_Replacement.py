class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, maxFreq = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])
            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
        return (r - l + 1)