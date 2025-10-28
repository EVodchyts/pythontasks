from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        n_count = 0
        for i in nums:
            if i < 0:
                n_count += 1
        return 1 if n_count % 2 == 0 else -1
    
def main():
    test = Solution()
    print(test.arraySign([-1,-2,-3,-4,3,2,1]))


if __name__ == "__main__":
    main()