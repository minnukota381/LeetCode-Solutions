class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s1 =set()
        s2=set()
        for i in range(len(word)):
            if word[i].islower():
                s1.add(word[i])
            else:
                s2.add(word[i].lower())
        return len(s1&s2)