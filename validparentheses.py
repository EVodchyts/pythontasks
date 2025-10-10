class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        if len(s) % 2 != 0:
            return False
        
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        return not stack
    
def main():
    test = Solution()
    print(test.isValid("([}}])"))
    print(test.isValid("]"))
    print(test.isValid("){"))
    print(test.isValid("()"))
    print(test.isValid("()[]{}"))
    print(test.isValid("(]"))
    print(test.isValid("([])"))

if __name__ == "__main__":
    main()