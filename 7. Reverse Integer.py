class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x<0 else 1
        x=abs(x)
        rs = int(str(x)[::-1])*s
        
        if rs < -2**31 or rs > 2**31 - 1:
            return 0

        return rs