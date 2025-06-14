class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        def backtrack(index, current_combination):
            if index == len(digits):
                combinations.append(''.join(current_combination))
                return
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            for letter in letters:
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                current_combination.pop()
        backtrack(0, [])
        return combinations