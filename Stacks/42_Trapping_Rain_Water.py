class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded = min(height[left], h) - height[mid]
                volume += width * bounded
            stack.append(i)
        return volume
