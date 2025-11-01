class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0                  # позиція
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # N, E, S, W
        i = 0                        # індекс напрямку (0 = North)
        for move in instructions:
            direction = directions[i]
            if move == 'G':
                dx, dy = direction
                x += dx
                y += dy
            elif move == 'L':
                i = (i - 1) % 4
            else:
                i = (i + 1) % 4
                
        return (x, y) == (0, 0) or i != 0

def main():
    test = Solution()
    print(test.isRobotBounded("GGLLGG"))
    print(test.isRobotBounded("GG"))
    print(test.isRobotBounded("GL"))
    print(test.isRobotBounded("GLGLGLGL"))
    
if __name__ == "__main__":
    main()