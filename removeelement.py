from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # лічильник "чистих" елементів
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    
def main():
    test = Solution()
    print(test.removeElement([3,2,2,3], 3))
    print(test.removeElement([0,1,2,2,3,0,4,2], 2))

if __name__ == "__main__":
    main()