class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in nums:
            if nums.count(i)==1:
                ls.append(i)

        return ls
# Time complexity: O(n^2)