class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                lst.append("FizzBuzz")
            elif i%3==0:
                lst.append("Fizz")
            elif i%5==0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst

'''
Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''
