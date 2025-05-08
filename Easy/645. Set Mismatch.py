class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ms = []

        for i in nums:
            if nums.count(i) == 2:
                ms.append(i)
                break

        n = len(nums)
        for i in range(1, n + 1):
            if i not in nums:
                ms.append(i)
                break

        return ms
