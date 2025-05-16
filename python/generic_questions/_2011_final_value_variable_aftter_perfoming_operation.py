from typing import List
class Solution:
    @staticmethod
    def finalValueAfterOperations(operations: List[str]) -> int:
        values = {'--X' : -1,
                  'X--' : -1,
                  'X' : 0,
                  'X++' : 1,
                  '++X' : 1} 
        output= 0
        for operation in operations:
            output += values[operation]
        return output
    
print(Solution.finalValueAfterOperations(["X++","++X","--X","X--"]))
            