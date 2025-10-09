class Solution:
    def romanToInt(self, s: str):
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        counter = 0
        previous = 0
        for c in s[::-1]:
            value = d[c]
            if value < previous:
                counter -= value
            else:
                counter += value
            previous = value
        return counter
    
def main():
    test = Solution()
    print(test.romanToInt("III"))
    print(test.romanToInt("LVIII"))
    print(test.romanToInt("MCMXCIV"))

if __name__ == "__main__":
    main()