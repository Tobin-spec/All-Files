class Solution:
    def isValid(self, s: str) -> bool:
        if '(' in s and ')' in s:
            print("true")
        elif '[' in s and ']' in s:
            print("true")
        elif '{' in s and '}' in s:
            print("true")
        else:
            print("false")

solution = Solution()
solution.isValid(str(input()))
