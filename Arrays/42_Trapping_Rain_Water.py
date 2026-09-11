class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        volume = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                volume += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                volume += rightMax - height[r]
        return volume
