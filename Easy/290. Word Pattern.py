class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

        