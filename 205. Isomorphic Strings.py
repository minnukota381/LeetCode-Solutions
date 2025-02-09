class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

        # return [s.index(c) for c in s] == [t.index(c) for c in t]
        # return map(s.find, s) == map(t.find, t)