from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # need to use the fact that it's sorted
        idx = 1
        dups = 0
        comparison_val = nums[0]
        while idx < len(nums):
            val = nums[idx]
            if val == -101:
                idx += 1
                continue
            if val == comparison_val:
                # duplicate
                dups += 1
                nums.pop(idx)
                nums.append(-101)
            else:
                comparison_val = val
                idx += 1
        return len(nums) - dups


if __name__ == "__main__":
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    print(k, nums)
    assert k == 5, "num unique"
    assert nums == [0, 1, 2, 3, 4, -101, -101, -101, -101, -101], "unique array"
