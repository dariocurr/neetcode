class Solution:

    # 2 3 4 5 10 20
    # O(nlogn)
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     nums = sorted(set(nums))
    #     max_counter = -1
    #     counter = 1
    #     start = nums[0]
    #     for i in range(len(nums)):
    #         if nums[i] == start + counter:
    #             counter += 1
    #         else:
    #             start = nums[i]
    #             if counter > max_counter:
    #                 max_counter = counter
    #             counter = 1
    #     if counter > max_counter:
    #         max_counter = counter
    #     return max_counter

    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res

    
            
        




            

        