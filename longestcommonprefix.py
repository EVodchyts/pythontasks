from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        i = 0
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                i += 1
            else:
                break
        
        return strs[0][:i]
        

def main():
    test = Solution()
    print(test.longestCommonPrefix(["flower","flow","flight"]))
    print(test.longestCommonPrefix(["dog","racecar","car"]))

if __name__ == "__main__":
    main()