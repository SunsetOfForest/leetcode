class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                temp = matrix[i][len(matrix[0])-1-j]
                matrix[i][len(matrix[0])-1-j] = matrix[j][len(matrix[0])-1-i]
                matrix[j][len(matrix[0])-1-i] = temp
