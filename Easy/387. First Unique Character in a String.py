class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)

        for i, char in enumerate(s):
            if count[char]==1:
                return i
        return -1
        