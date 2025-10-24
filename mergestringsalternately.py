from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([x + y for x, y in zip_longest(word1, word2, fillvalue='')])


def main():
    test = Solution()
    print(test.mergeAlternately("abc", "pqr"))
    print(test.mergeAlternately("abcd", "pq"))

if __name__ == "__main__":
    main()