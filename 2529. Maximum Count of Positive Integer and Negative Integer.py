class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos=0
        neg=0
        for i in nums:
            if i>0:
                pos+=1
            elif i==0:
                pass
            else:
                neg+=1
        return max(pos,neg)
