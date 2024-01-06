class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        empty=[]
        for i in s:
            if i.isalnum():
                empty.append(i.lower())
        new = "".join(empty)

        return new==new[::-1]

        