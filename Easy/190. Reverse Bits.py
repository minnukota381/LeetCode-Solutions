class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary=bin(n)[2:].zfill(32)
        rev=binary[::-1]
        return int(rev,2)

        