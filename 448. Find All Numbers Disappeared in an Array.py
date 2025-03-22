class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=set(nums)
        ls=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                ls.append(i)
        return ls
        # return list(set(range(1, len(nums) + 1)) - set(nums))
        