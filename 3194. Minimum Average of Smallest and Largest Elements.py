class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while nums != []:
            minimum = min(nums)
            maximum = max(nums)
            nums.remove(minimum)
            nums.remove(maximum)
            averages.append((minimum+maximum)/2)
        return min(averages)


'''
Input: nums = [1,2,3,7,8,9]
Output: 5.0

Input: nums = [1,9,8,3,10,5]
Output: 5.5
'''
