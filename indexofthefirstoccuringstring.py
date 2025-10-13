class Solution:
    def strStr(self, haystack: str, needle: str):
        x, y = len(haystack), len(needle)

        if y == 0:
            return -1
        
        for i in range(x - y + 1):
            if haystack[i:i+y] == needle:
                return i
        return -1

def main():
    test = Solution()
    print(test.strStr("brrsadf", "sad"))

if __name__ == "__main__":
    main()