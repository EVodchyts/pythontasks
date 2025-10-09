from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            if target - value in d:
                return [index, d[target - value]]
            d[value] = index
        return []

def main():
    test = Solution()
    print(test.twoSum([2,7,11,15], 9))
    print(test.twoSum([3,2,4], 6))
    print(test.twoSum([3, 3], 6))

if __name__ == "__main__":
    main()