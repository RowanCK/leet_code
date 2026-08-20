from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))

        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        str_nums.sort(key=cmp_to_key(compare))

        result = "".join(str_nums)
        return "0" if result[0] == "0" else result


# Method 2: Using sort with a custom key
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         nums = list(map(str, nums))
#         nums.sort(key=lambda x: x * 10, reverse=True)
#         return str(int(''.join(nums)))
