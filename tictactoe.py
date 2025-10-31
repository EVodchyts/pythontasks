from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [
            {(0,0),(0,1),(0,2)}, {(1,0),(1,1),(1,2)}, {(2,0),(2,1),(2,2)},  # рядки
            {(0,0),(1,0),(2,0)}, {(0,1),(1,1),(2,1)}, {(0,2),(1,2),(2,2)},  # стовпці
            {(0,0),(1,1),(2,2)}, {(0,2),(1,1),(2,0)}                        # діагоналі
        ]
        
        a_moves = {tuple(moves[i]) for i in range(0, len(moves), 2)}
        b_moves = {tuple(moves[i]) for i in range(1, len(moves), 2)}
        
        for w in wins:
            if w <= a_moves:
                return "A"
            if w <= b_moves:
                return "B"
        
        return "Draw" if len(moves) == 9 else "Pending"

    
def main():
    test = Solution()
    print(test.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(test.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(test.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
    print(test.tictactoe([[2,0],[1,0],[1,1],[0,2]]))

if __name__ == "__main__":
    main()