#_2294_partition_array_such_that_maximum_difference_is_k
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        min_val = nums[0]
        for num in nums[1:]:
            if num - min_val > k:
                res += 1
                min_val = num
        return res