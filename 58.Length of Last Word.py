class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=s.strip().split(" ")
        return len(m[-1])
        