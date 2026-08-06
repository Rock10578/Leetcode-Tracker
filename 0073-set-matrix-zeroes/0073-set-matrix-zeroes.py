class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        Zerolocations = list()
        for i in range(m):
            if 0 in matrix[i]:
                for j in range(n):
                    if matrix[i][j] == 0:
                       Zerolocations.append([i,j])
        
        for x,y in Zerolocations:
            matrix[x] = [0]*n
            j = 0
            while j < m:
                matrix[j][y] = 0
                j += 1