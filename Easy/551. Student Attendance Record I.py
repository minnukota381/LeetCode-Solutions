class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        hell = Counter(s)

        if hell['A']>=2:
            return False

        if 'LLL' in s:
            return False

        return True


        