from typing import List
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    items = {}

    for idx, num in enumerate(nums):
      if num in items:
        return [items[num], idx]
      items[target - num] = idx
  
    return items

sol = Solution()
result = sol.twoSum([1, 2, 3, 4, 5, 6], 10)
print(result)