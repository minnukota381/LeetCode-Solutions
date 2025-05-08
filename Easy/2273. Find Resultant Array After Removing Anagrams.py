class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        ls=[]
        prev=None
        for i in words:
            sort="".join(sorted(i))
            if sort!=prev:
                ls.append(i)
                prev=sort
        return ls

        