class Solution:
    def countArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        if n == 0:
            return 0
        if k >= n:
            return 0
        prev_dp = [[0] * (m + 1) for _ in range(k + 1)]
        for num in range(1, m + 1):
            prev_dp[0][num] = 1
        for i in range(1, n):
            curr_dp = [[0] * (m + 1) for _ in range(k + 1)]
            for matches in range(0, k + 1):
                for last in range(1, m + 1):
                    if prev_dp[matches][last] == 0:
                        continue
                    if matches + 1 <= k:
                        curr_dp[matches + 1][last] = (curr_dp[matches + 1][last] + prev_dp[matches][last]) % MOD
                    curr_dp[matches][last] = (curr_dp[matches][last] + prev_dp[matches][last] * (m - 1)) % MOD
            prev_dp = curr_dp
        total = 0
        for num in range(1, m + 1):
            total = (total + prev_dp[k][num]) % MOD
        return total