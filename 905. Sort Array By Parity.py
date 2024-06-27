class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            if i & 1 == 0:
                l.insert(0, i)
            else:
                l.append(i)
        return l


'''
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Input: nums = [0]
Output: [0]
'''
