class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        binary = ''.join([str(i) for i in nums])
        ones = binary.split('0')
        max = 0
        for i in ones:
            length = len(i)
            if length > max:
                max = length
        return max

'''
Input: nums = [1,0,1,1,0,1]
Output: 2
'''
