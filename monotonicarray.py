from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        asc = all(nums[i] >= nums[i - 1] for i in range(1, len(nums)))
        desc = all(nums[i] <= nums[i - 1] for i in range(1, len(nums)))
        return asc or desc
    
def main():
    test = Solution()
    print(test.isMonotonic([0,1,0,3,12]))
    print(test.isMonotonic([0,1,3,12]))
    print(test.isMonotonic([1,2,2,3]))
    print(test.isMonotonic([6,5,4,4]))


if __name__ == "__main__":
    main()