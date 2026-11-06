class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).casefold()
        print(s)

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True