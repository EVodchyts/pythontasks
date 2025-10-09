class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = [c for c in str(x)]
        return input == input[::-1]

def main():
    test = Solution()
    print(test.isPalindrome(121) == True)
    print(test.isPalindrome(-121) == False)
    print(test.isPalindrome(10) == False)


if __name__ == "__main__":
    main()