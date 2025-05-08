class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rti = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        t = 0
        prev = 0
        for x in s[::-1]:
            curr = rti[x]
            if curr < prev:
                t -= curr
            else:
                t += curr
            prev = curr
        return t
        