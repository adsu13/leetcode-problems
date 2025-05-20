from typing import List
class Solution:
    @staticmethod
    def getConcatenation(nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(nums[i])
        for j in range(len(nums)):
            output.append(nums[j])
        return output