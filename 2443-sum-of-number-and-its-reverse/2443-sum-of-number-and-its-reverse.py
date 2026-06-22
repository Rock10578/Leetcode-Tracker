class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num in [0,2,11]:
            return True
        elif num == 1:
            return False
        for y in range(1,num-1):
            x = num-y
            if x == int("".join(reversed(str(y)))):
                return True
        return False