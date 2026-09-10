class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1 
        currMin = float("inf")
        n = nums

        while start < end :
            m = start + (end - start)//2
            currMin = min(currMin, n[m])
            if n[m] > n[end]:
                start = m + 1
            else:
                end = m - 1
        return min(currMin, n[start])