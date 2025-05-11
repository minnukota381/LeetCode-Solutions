class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=[]
        for i in s:
            if i.isalpha():
                l.append(i)

        l.reverse()

        li=0
        r=[]
        for i in s:
            if i.isalpha():
                r.append(l[li])
                li+=1
            else:
                r.append(i)

        return "".join(r)

        