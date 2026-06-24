from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        current_max = current_min = max_product = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])
            max_product = max(max_product, current_max)

        return max_product
