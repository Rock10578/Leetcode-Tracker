class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()
        if numRows >= 1:  result.append([1])
        if numRows >= 2:  result.append([1,1])
        for i in range(3,numRows+1):
            temp = [1]
            lastArr = result[-1]
            for x in range(len(lastArr)-1):
                temp.append(lastArr[x]+lastArr[x+1])
            temp.append(1)
            result.append(temp)
        return result