class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0] #XY axis
        for i in moves:
            if i == 'U':
                start[1] += 1
            elif i == 'D':
                start[1] += -1
            elif i == 'L':
                start[0] += -1
            else:
                start[0] += 1

        return start == [0, 0]


def main():
    test = Solution()
    print(test.judgeCircle("UD"))
          
if __name__ == "__main__":
    main()               