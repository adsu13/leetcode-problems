class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:
            partition_nums1 = (left + right) // 2
            partition_nums2 = total_left - partition_nums1
            max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1]
            max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if (m + n) % 2 == 1:
                    return max(max_left_nums1, max_left_nums2)
                else:
                    return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
            elif max_left_nums1 > min_right_nums2:
                right = partition_nums1 - 1
            else:
                left = partition_nums1 + 1
        raise ValueError("Input arrays are not sorted or invalid")