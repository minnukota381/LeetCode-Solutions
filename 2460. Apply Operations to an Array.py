class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)

        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0

        r = []
        zc=0
        for i in range(n):
            if nums[i]!=0:
                r.append(nums[i])
            else:
                zc+=1
        for i in range(zc):
            r.append(0)

        return r
        