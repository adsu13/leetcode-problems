class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1
        k -= 1
        while k > 0:
            count = 0
            curr = result
            next_node = result + 1
            while curr <= n:
                count += min(n + 1, next_node) - curr
                curr *= 10
                next_node *= 10
            
            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1
        return result