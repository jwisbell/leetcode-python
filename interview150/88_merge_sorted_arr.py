from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """ My slow solution O(m*n)"""
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        num_inserted = 0
        for val in nums2:
            inserted = False
            for i, x in enumerate(nums1):
                if val <= x:
                    inserted = True
                    num_inserted += 1
                    nums1.insert(i, val)
                    break
            if not inserted:
                nums1.insert(m + num_inserted, val)
                num_inserted += 1
        # clear trailing 0s
        while len(nums1) > n + m and nums1[-1] == 0:
            _ = nums1.pop()

        """LLM Aided solution O(m+n)"""
        """i, j, k = m - 1, n - 1, m + n - 1

        # suggestion to start from the end
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # handle remaining elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        """


if __name__ == "__main__":
    s = Solution()
    nums1 = [-1, -1, 0, 0, 0, 0]
    nums2 = [-1, 0]
    s.merge(nums1, 4, nums2, 2)
    assert nums1 == [-1, -1, -1, 0, 0, 0], "test"
