from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [x if x != val else -1 for x in nums]
        # the above is nice but not "in place"

        # looping solution, no llm assistance
        k = 0
        idx = 0
        while idx < len(nums):
            x = nums[idx]
            if x == val:
                del nums[idx]
                nums.append(-1)
            elif x != -1:
                nums[idx] = x
                k += 1
                idx += 1
            else:
                idx += 1

        return k


if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 2, 3]
    result = [2, 2, "", ""]
    k = s.removeElement(nums, 3)
    print(nums, k)
    assert k == 2, k
    assert nums == [2, 2, -1, -1], nums
