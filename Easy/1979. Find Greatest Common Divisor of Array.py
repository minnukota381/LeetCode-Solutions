class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ls=[]
        minNum=min(nums)
        maxNum=max(nums)
        for i in range(1,minNum+1):
            if minNum%i==0 and maxNum%i==0:
                ls.append(i)
        return max(ls)
            