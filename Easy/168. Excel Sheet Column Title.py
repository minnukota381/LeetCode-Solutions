class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        r=[]
        while columnNumber>=1:
            columnNumber-=1
            r.append(chr(columnNumber%26+ord('A')))
            columnNumber //= 26
        
        return ''.join(r[::-1])
        