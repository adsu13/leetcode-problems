class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        prefix = ""
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != current_char:
                    return prefix
            prefix += current_char
        return prefix