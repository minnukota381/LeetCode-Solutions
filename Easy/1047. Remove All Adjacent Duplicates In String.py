class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl= []

        for char in s:
            if sl and sl[-1] == char:
                sl.pop()
            else:
                sl.append(char)

        return "".join(sl)

        