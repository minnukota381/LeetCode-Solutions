class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        frq=Counter(s)
        lsEven=[]
        lsOdd=[]
        for i in s:
            if frq[i]%2==0:
                lsEven.append(frq[i])
            else:
                lsOdd.append(frq[i])

        return max(lsOdd)-min(lsEven)