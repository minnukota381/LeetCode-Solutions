class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <0:
            num+=2**32
        return hex(num)[2:]
        