class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        r=0
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            sum=0
            while n>0:
                r=n%10
                sum=sum+r*r
                n=n//10
            n=sum
        if n==1:
            return True
        else:
            return False