class Solution:

    # 2 3 4 5 10 20

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        max_counter = -1
        counter = 0
        start = None
        for i in range(len(nums)):
            if start == None:
                start = nums[i]
                counter = 1
            else:
                if nums[i] == start + counter:
                    counter += 1
                else:
                    start = nums[i]
                    if counter > max_counter:
                        max_counter = counter
                    counter = 1
        if counter > max_counter:
            max_counter = counter
        return max_counter


            

        