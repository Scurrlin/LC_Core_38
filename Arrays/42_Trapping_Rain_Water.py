class Solution:
    def trap(self, height: List[int]) -> int:
        h, volume = height, 0
        l, r = 0, len(h) - 1
        leftMax, rightMax = h[l], h[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, h[l])
                volume += leftMax - h[l]
            else:
                r -= 1
                rightMax = max(rightMax, h[r])
                volume += rightMax - h[r]
        return volume