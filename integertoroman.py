class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result += symbols[i]
        return result
    
def main():
    test = Solution()
    print(test.intToRoman(3)) # III
    print(test.intToRoman(56)) #LVI
    print(test.intToRoman(1994)) #"MCMXCIV"

if __name__ == "__main__":
    main()