from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry = 1  # додаємо 1 до останнього елемента

        for i in digits[::-1]:
            total = i + carry
            result.append(total % 10)
            carry = total // 10  # 1 якщо було 10 або більше, інакше 0

        if carry:
            result.append(carry)

        return result[::-1]
    
def main():
    test = Solution()
    #print(test.plusOne([1,2,9]))
    #print(test.plusOne([1,2,9,9,9]))
    print(test.plusOne([9]))


if __name__ == "__main__":
    main()