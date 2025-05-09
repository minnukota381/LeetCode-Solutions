class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        r = []

        for i in range(n):
            r.append(nums[i])
            r.append(nums[i+n])
            
        return r
        