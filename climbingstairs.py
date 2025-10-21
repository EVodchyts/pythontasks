class Solution:
    def climbStairs(self, n: int):
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one

def main():
    test = Solution()
    
    print(test.climbStairs(10))
    print(test.climbStairs(45))

if __name__ == "__main__":
    main()