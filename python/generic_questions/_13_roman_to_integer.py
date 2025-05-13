class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        output = 0
        roman_values = {'I': 1, 
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
                output -= roman_values[s[i]]
            else:
                output += roman_values[s[i]]
        
        return output