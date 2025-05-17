from typing import List
class Solution:
    @staticmethod
    def shuffle(nums: List[int], n: int) -> List[int]:
        Xs = []
        Ys = []
        output = []
        for i in range(len(nums)):
            if(i < n):
                Xs.append(nums[i])
            if(i >= n):
                Ys.append(nums[i])
        for j in range(len(Xs)):
            output.append(Xs[j])
            output.append(Ys[j])
        return output