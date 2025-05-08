class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        cr=Counter(ransomNote)
        cm=Counter(magazine)

        for c in cr:
            if cr[c]>cm[c]:
                return False
        return True