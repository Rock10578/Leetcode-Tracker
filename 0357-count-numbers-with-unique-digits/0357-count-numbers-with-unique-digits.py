class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def recursiveCalculation(n):
            if n==0:
                return 1
            elif n==1:
                return 10
            else:
                x = 9
                for i in range(9,9-n+1,-1):
                    if i == 0:
                        break
                    x *= i
                return x + recursiveCalculation(n-1)
        return recursiveCalculation(n)