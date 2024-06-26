class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        n = len(arr)
        i = 1
        
        while i<n and arr[i]>arr[i-1]:
            i = i+1
        
        if i==1 or i==n:
            return False
        
        while i<n and arr[i]<arr[i-1]:
            i = i+1
        
        return i==n
        

'''
Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true
'''
