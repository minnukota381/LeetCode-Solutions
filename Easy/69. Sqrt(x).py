class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r=0,x
        ans=0
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            elif m*m<x:
                l=m+1
                ans=m
            else:
                r=m-1
        return ans
        