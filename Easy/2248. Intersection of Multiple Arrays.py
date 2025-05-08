class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        c = set(nums[0])

        for i in range(1, len(nums)):
            cs = set(nums[i])
            c = c.intersection(cs)
        
        r=list(c)
        r.sort()
        return r
        