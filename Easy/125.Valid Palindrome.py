# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         empty=[]
#         for i in s:
#             if i.isalnum():
#                 empty.append(i.lower())
#         new = "".join(empty)

#         return new==new[::-1]

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=""
        s=s.lower()
        for x in s:
            if x.isalnum():
                st+=x

        return st==st[::-1]
          