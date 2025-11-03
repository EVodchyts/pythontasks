from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            top += 1

            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for column in range(right, left - 1, -1):
                    res.append(matrix[bottom][column])
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
    
    
def main():
    test = Solution()
    print(test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == "__main__":
    main()