class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        L = int(area**0.5)

        while area%L!=0:
            L-=1

        W = area//L

        return [W,L]
        