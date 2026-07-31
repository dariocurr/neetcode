from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            compl = target - num
            if indexes[compl]:
                return [indexes[compl][0], i]
            else:
                indexes[num].append(i)