class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix) 
        for i in range(m-1):
            x = i+1
            for j in range(x,m):
                if i!=j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(m):
            matrix[i] = matrix[i][::-1]