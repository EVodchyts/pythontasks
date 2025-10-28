from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        return all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(1, len(arr)))

    
def main():
    test = Solution()
    print(test.canMakeArithmeticProgression([3,5,1]))

if __name__ == "__main__":
    main()