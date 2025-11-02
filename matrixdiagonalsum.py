from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        for i in range(len(mat)):
            r += mat[i][i]
            r += mat[i][len(mat) - 1 - i]

        return r - (mat[len(mat) // 2][len(mat) // 2] if len(mat) % 2 else 0)
    
    
def main():
    test = Solution()
    print(test.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(test.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))

if __name__ == "__main__":
    main()