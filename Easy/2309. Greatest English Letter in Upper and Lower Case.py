class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = set(s)

        for i in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if i in ss and i.lower() in ss:
                return i

        return ""
