class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        if len(a) > len(b):
            while len(b) != len(a):
                b = '0' + b
        else:
            while len(b) != len(a):
                a = '0' + a
        
        carry = 0
        for x, y in zip(a[::-1], b[::-1]):
            total = int(x) + int(y) + carry
            res.append(str(total % 2))
            carry = total // 2
        if carry != 0 : res.append('1')
        
        return ''.join(res[::-1])
    
def main():
    test = Solution()
    
    print(test.addBinary("11", "1")) #100
    print(test.addBinary("0", "0")) #0
    print(test.addBinary("1010", "1011")) #10101
    print(test.addBinary("1111", "1111")) #11110

if __name__ == "__main__":
    main()