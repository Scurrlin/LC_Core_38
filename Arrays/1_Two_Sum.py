class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num2 = target - num 
            if num2 in seen:
                return [seen[num2], i]
            seen[num] = i