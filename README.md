# LeetCode Core 38

This repository contains answers to the 38 LeetCode questions that will teach you the platform's core DSA problem-solving patterns.

<details>
<summary><strong>Arrays</strong></summary>

<dl>
<dd>

<details>
<summary><small>1. Two Sum</small></summary>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num2 = target - num 
            if num2 in seen:
                return [seen[num2], i]
            seen[num] = i
```

</details>

</dd>

<dd>

<details>
<summary><small>121. Best Time to Buy and Sell Stock</small></summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        best = 0
        
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                best = max(best, p - minPrice)
        return best
```

</details>

</dd>

<dd>

<details>
<summary><small>49. Group Anagrams</small></summary>

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())
```

</details>

</dd>

<dd>

<details>
<summary><small>238. Product of Array Except Self</small></summary>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
            
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
```

</details>

</dd>

<dd>

<details>
<summary><small>128. Longest Consecutive Sequence</small></summary>

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```

</details>

</dd>

<dd>

<details>
<summary><small>11. Container With Most Water</small></summary>

```python
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
```

</details>

</dd>

<dd>

<details>
<summary><small>15. 3Sum</small></summary>

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>56. Merge Intervals</small></summary>

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```

</details>

</dd>

<dd>

<details>
<summary><small>39. Combination Sum</small></summary>

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)
            
        dfs(0, [], 0)
        return res
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Strings</strong></summary>

<dl>
<dd>

<details>
<summary><small>3. Longest Substring Without Repeating Characters</small></summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>424. Longest Repeating Character Replacement</small></summary>

```python
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
```

</details>

</dd>

<dd>

<details>
<summary><small>76. Minimum Window Substring</small></summary>

```python
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        need, missing = Counter(t), len(t)
        l = start = end = 0
        
        for r, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while l < r and need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1
                if end == 0 or r - l <= end - start:
                    start, end = l, r
                need[s[l]] += 1
                missing += 1
                l += 1

        return s[start:end]
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Linked Lists</strong></summary>

<dl>
<dd>

<details>
<summary><small>206. Reverse Linked List</small></summary>

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
```

</details>

</dd>

<dd>

<details>
<summary><small>21. Merge Two Sorted Lists</small></summary>

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next
```

</details>

</dd>

<dd>

<details>
<summary><small>141. Linked List Cycle</small></summary>

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Stacks</strong></summary>

<dl>
<dd>

<details>
<summary><small>20. Valid Parentheses</small></summary>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return not stack
```

</details>

</dd>

<dd>

<details>
<summary><small>155. Min Stack</small></summary>

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

</details>

</dd>

<dd>

<details>
<summary><small>42. Trapping Rain Water</small></summary>

```python
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
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Binary Search</strong></summary>

<dl>
<dd>

<details>
<summary><small>33. Search in Rotated Sorted Array</small></summary>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
```

</details>

</dd>

<dd>

<details>
<summary><small>875. Koko Eating Bananas</small></summary>

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>981. Time Based Key-Value Store</small></summary>

```python
class TimeMap:
    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keys.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Binary Trees</strong></summary>

<dl>
<dd>

<details>
<summary><small>102. Binary Tree Level Order Traversal</small></summary>

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>543. Diameter of Binary Tree</small></summary>

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>236. Lowest Common Ancestor of a Binary Tree</small></summary>

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
```

</details>

</dd>

<dd>

<details>
<summary><small>297. Serialize and Deserialize Binary Tree</small></summary>

```python
class Codec:
    def serialize(self, root):
        vals = []
        
        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)
    

    def deserialize(self, data):
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node        
        return dfs()
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Graphs</strong></summary>

<dl>
<dd>

<details>
<summary><small>200. Number of Islands</small></summary>

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(row, col):
            if not (0 <= row < rows 
                and 0 <= col < cols
                and grid[row][col] == '1'):
                return
            
            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
        
        return islands
```

</details>

</dd>

<dd>

<details>
<summary><small>133. Clone Graph</small></summary>

```python
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        newGraph = {}

        def dfs(node):
            if node in newGraph:
                return newGraph[node]

            copy = Node(node.val)
            newGraph[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node) if node else None
```

</details>

</dd>

<dd>

<details>
<summary><small>207. Course Schedule</small></summary>

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, p in prerequisites:
            preMap[course].append(p)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
```

</details>

</dd>

<dd>

<details>
<summary><small>994. Rotting Oranges</small></summary>

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:      
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        fresh, rotten = 0, deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        mins = 0

        while rotten and fresh > 0:
            rottenCount = len(rotten)
            for _ in range(rottenCount):
                rottenRow, rottenCol = rotten.popleft()

                for directionRow, directionCol in directions:
                    neighborRow = rottenRow + directionRow
                    neighborCol = rottenCol + directionCol

                    if (0 <= neighborRow < rows
                        and 0 <= neighborCol < cols
                        and grid[neighborRow][neighborCol] == 1):
                        grid[neighborRow][neighborCol] = 2
                        rotten.append((neighborRow, neighborCol))
                        fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1
```

</details>

</dd>

<dd>

<details>
<summary><small>542. 01 Matrix</small></summary>

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dir = (-1, 1), (1, 1)

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bot = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bot + 1, right + 1)
        return mat
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Dynamic Programming</strong></summary>

<dl>
<dd>

<details>
<summary><small>53. Maximum Subarray</small></summary>

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>198. House Robber</small></summary>

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
```

</details>

</dd>

<dd>

<details>
<summary><small>322. Coin Change</small></summary>

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minC = [float('inf')] * (amount + 1)
        minC[0] = 0

        for coin in coins:
            for amount in range(1, amount + 1):
                if coin <= amount:
                    minC[amount] = min(
                        minC[amount],
                        1 + minC[amount - coin])

        if minC[amount] == float('inf'):
            return -1
        else:
            return minC[amount]
```

</details>

</dd>

<dd>

<details>
<summary><small>62. Unique Paths</small></summary>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Heap</strong></summary>

<dl>
<dd>

<details>
<summary><small>973. K Closest Points to Origin</small></summary>

```python
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x, y) for (dist, x, y) in heap]
```

</details>

</dd>

<dd>

<details>
<summary><small>295. Find Median from Data Stream</small></summary>

```python
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
```

</details>

</dd>

</dl>

</details>

<details>
<summary><strong>Recursion</strong></summary>

<dl>
<dd>

<details>
<summary><small>78. Subsets</small></summary>

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(i):
            res.append(path.copy())
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()

        dfs(0)
        return res
```

</details>

</dd>

<dd>

<details>
<summary><small>46. Permutations</small></summary>

```python
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
```

</details>

</dd>

</dl>

</details>
