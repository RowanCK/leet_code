from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}
        for idx, value in enumerate(nums):
            remain = target - value

            if remain in exist:
                return [exist[remain], idx]

            exist[value] = idx
