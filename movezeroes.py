from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
        return nums

        
    
def main():
    test = Solution()
    print(test.moveZeroes([0,1,0,3,12]))
    print(test.moveZeroes([0,0,1]))#[1,0,0]
    print(test.moveZeroes([2, 1]))#[1,0,0]


if __name__ == "__main__":
    main()