from typing import List
class Solution:
    @staticmethod
    def findWordsContaining(words: List[str], x: str) -> List[int]:
        output = []
        for i in range(len(words)):
            if(x in words[i]):
                output.append(i)
        return output