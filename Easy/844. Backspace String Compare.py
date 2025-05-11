class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hm = []
        mh = []

        for i in s:
            if i == '#':
                if hm:
                    hm.pop()
            else:
                hm.append(i)

        for i in t:
            if i == '#':
                if mh:
                    mh.pop()
            else:
                mh.append(i)

        return hm == mh