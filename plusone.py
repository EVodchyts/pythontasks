from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        reminder = 1

        for i in digits[::-1]:
            total = i + reminder
            result.append(total % 10)
            reminder = total // 10
        
        if reminder:
            result.append(reminder)

        return result[::-1]
    
def main():
    test = Solution()
    print(test.plusOne([1,2,9]))
    print(test.plusOne([1,2,9,9,9]))
    print(test.plusOne([9]))


if __name__ == "__main__":
    main()