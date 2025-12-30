class Solution(object):
    def findNonMinOrMax(self, nums):
        # If fewer than 3 elements, no valid answer
        if len(nums) < 3:
            return -1

        min_val = min(nums)
        max_val = max(nums)

        for n in nums:
            if n != min_val and n != max_val:
                return n
