class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y, m, d = map(int, date.split('-'))

        return bin(y)[2:] + "-" + bin(m)[2:] + "-" + bin(d)[2:]


        