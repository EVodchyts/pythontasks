class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


def main():
    test = Solution()
    
    print(test.countOdds(3, 7))
    print(test.countOdds(8, 10))
    print(test.countOdds(8, 12))
    print(test.countOdds(800445804, 979430543))

if __name__ == "__main__":
    main()