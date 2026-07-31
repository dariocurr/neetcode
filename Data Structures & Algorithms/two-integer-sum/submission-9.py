from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, num in enumerate(nums):
            compl = target - num
            if compl in indexes:
                return [indexes[compl], i]
            indexes[num] = i