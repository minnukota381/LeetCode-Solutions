class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]

        for i in s:
            if i == '*':
                l.pop()
            else:
                l.append(i)

        return "".join(l)
        