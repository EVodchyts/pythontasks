from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in operations:
            if x == '+':
                record.append(record[-1] + record[-2])
            elif x == 'C':
                del record[-1]
            elif x == 'D':
                record.append(record[-1] * 2)
            else:
                record.append(int(x))
            
        return sum(record)
    
 
def main():
    test = Solution()
    print(test.calPoints(["5","2","C","D","+"]))


if __name__ == "__main__":
    main()