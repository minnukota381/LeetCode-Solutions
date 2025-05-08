class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        
        for num in nums:
            div = set()
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    div.add(i)
                    div.add(num // i)
                if len(div) > 4:
                    break  
            if len(div) == 4:
                total_sum += sum(div)
        
        return total_sum
