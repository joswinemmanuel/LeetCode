class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i!=j and arr[i]==2*arr[j]:
                    return True
        return False


'''
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
'''
