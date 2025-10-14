class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()      
        left = 0         
        max_len = 0       

        for right in range(len(s)):
            while s[right] in seen:     
                seen.remove(s[left])
                left += 1
            seen.add(s[right])          
            max_len = max(max_len, right - left + 1)

        return max_len

def main():
    test = Solution()
    print(test.lengthOfLongestSubstring("abcabcbb"))
    print(test.lengthOfLongestSubstring("bbbbb"))
    print(test.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()