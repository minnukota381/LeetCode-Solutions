class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = set()

        for num in nums:
            if num > 0:
                unique.add(num)
        
        return len(unique)
