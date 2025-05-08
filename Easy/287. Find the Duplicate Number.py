class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq=Counter(nums)
        for i in nums:
            if freq[i]>=2:
                return i
        