class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_prefix = ""
        
        for i in range(len(strs) -1):
            for h in strs[i]:
                if h in strs[i] and strs[i + 1]:
                    common_prefix += h

        return common_prefix
        print(commn_prefix)

solution = Solution()
solution.longestCommonPrefix(["flower","flow","flight"])
