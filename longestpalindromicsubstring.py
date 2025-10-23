class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Коли строка пуста - повертаємо пусту строку
        if len(s) == 0: return ''
        
        def expand(s, left, right) -> int:
            '''
            Цикл виконується поки лівий індекс більше ніж початок строки, а права менше за довжину строки і поки сусдні
            символи рівні один одному, повертає довжину цієї частини строки
            '''
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        start = 0
        end = 0

        '''
        В циклі ітеруємось по строці, викликаємо центрувальну функцію для even та odd випадків, знаходимо максимальну довжину для цих випадків
        і порівнюємо з різницею між стартом строки і кінцем строки
        '''
        for i in range(len(s)):
            odd = expand(s, i, i)
            even = expand(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

def main():
    test = Solution()
    print(test.longestPalindrome("babc"))
    print(test.longestPalindrome("cbabbba"))

if __name__ == "__main__":
    main()