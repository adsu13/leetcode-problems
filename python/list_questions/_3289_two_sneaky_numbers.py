from typing import List
class Solution:
    @staticmethod
    def getSneakyNumbers(nums: List[int]) -> List[int]:
        seen_elements = set()
        repeated_elements = set()
        for i in nums:
            if(i in seen_elements):
                repeated_elements.add(i)
            else:
                seen_elements.add(i)
        return list(repeated_elements)
print(Solution.getSneakyNumbers([0,3,2,1,3,2]))