class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    items = {}

    for idx, num in enumerate(nums):
      if num in items:
        return [items[num], idx]
      items[target - num] = idx

    return items
