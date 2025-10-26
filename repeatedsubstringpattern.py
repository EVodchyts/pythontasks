class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
    
def main():
    test = Solution()
    print(test.repeatedSubstringPattern("abab"))
    print(test.repeatedSubstringPattern("aba"))
          
if __name__ == "__main__":
    main()       