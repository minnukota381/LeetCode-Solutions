class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]

        for i in nums:
            if i%2==0:
                ls.append(i)
        
        if not ls:
            return -1
        
        frq=Counter(ls)
        maxfrq = max(frq.values())
        small = float('inf')

        for i in frq:
            if frq[i]==maxfrq:
                if i<small:
                    small=i
        
        return small