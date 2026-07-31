from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = defaultdict(lambda: 0)
        for num in nums:
            counters[num] += 1
        buckets = [[] for _ in nums]
        for key, value in counters.items():
            buckets[value - 1].append(key)
        result = []
        index = len(nums) - 1
        while index > -1:
            for num in buckets[index]:
                result.append(num)
                if len(result) == k:
                    return result
            index -= 1
            
        




        