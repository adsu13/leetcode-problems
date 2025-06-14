#_2566_maximum_difference_by_remapping_a_digit
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_digit = None
        for c in s:
            if c != '9':
                max_digit = c
                break
        if max_digit is None:
            max_num = num
        else:
            max_num = int(s.replace(max_digit, '9'))
        min_digit = s[0]
        min_num = int(s.replace(min_digit, '0'))
        return max_num - min_num