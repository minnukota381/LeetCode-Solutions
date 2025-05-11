class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=""
        for i in range(len(s)):
            if s[i]=='i':
                r=r[::-1]
            else:
                r+=s[i]
        return r