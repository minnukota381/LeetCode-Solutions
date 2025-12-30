class Solution(object):
    def thirdMax(self, nums):
        first = second = third = None

        for n in nums:
            # Skip duplicates
            if n == first or n == second or n == third:
                continue

            if first is None or n > first:
                third = second
                second = first
                first = n
            elif second is None or n > second:
                third = second
                second = n
            elif third is None or n > third:
                third = n

        # If third max doesn't exist, return max
        return third if third is not None else first
