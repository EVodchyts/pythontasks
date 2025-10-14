from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       res = []
       for i in s.split(' '):
           if i.isalpha():
              res.append(i)
       return len(res[-1])

    
def main():
    test = Solution()
    print(test.lengthOfLastWord("   fly me   to   the moon  "))
    print(test.lengthOfLastWord("luffy is still joyboy"))
    print(test.lengthOfLastWord("Hello World "))

if __name__ == "__main__":
    main()