class Solution:
    def isValid(self, s: str) -> bool:
        reverse = s[::-1]
        print(reverse)

        if s == reverse:
            print("true")
        else:
            print("false")

solution = Solution()
solution.isValid(str(input()))
