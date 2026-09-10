class Solution:
    def maxArea(self, height: List[int]) -> int:
        h, maxArea = height, 0
        l, r = 0, len(h) - 1

        while l < r:
            if h[l] < h[r]:
                area = h[l] * (r - l)
                l += 1
            else:
                area = h[r] * (r - l)
                r -= 1
            maxArea = max(maxArea, area)
        return maxArea