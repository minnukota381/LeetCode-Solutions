class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0

        # for num in nums:
        #     if nums.count(num)==1:
        #         return num

        a = 0
        for num in nums:
            a ^= num
        return a