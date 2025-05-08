class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            result.append(bin(i).count('1'))
        return result