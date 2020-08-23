class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        b = self.x
        self.rev = 0
        while b > 0:
            a = b % 10
            self.rev = self.rev * 10 + a
            b = b // 10
        if x == self.rev:
            print("true")
        else:
            print("false")


solution = Solution()
solution.isPalindrome(int(input()))

       
