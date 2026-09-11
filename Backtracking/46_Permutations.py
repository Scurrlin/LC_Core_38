class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: return res.append(path)
            for i in range(len(nums)): 
                backtrack(
                    nums[:i] + nums[i + 1:],
                    path + [nums[i]]) 
        res = [] 
        backtrack(nums, []) 
        return res
