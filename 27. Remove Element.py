class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        k=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k