class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        q=int("".join(map(str,digits)))+1
    
        return list(map(int,str(q)))
        