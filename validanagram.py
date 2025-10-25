class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for c in set(t):
            if t.count(c) != s.count(c):
                return False
        return True

def main():
    test = Solution()
    print(test.isAnagram("anagram", "nagaram"))
    print(test.isAnagram("a", "aa"))
    print(test.isAnagram("ccac", "aacc"))

if __name__ == "__main__":
    main()        