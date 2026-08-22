class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k %= n  # Handle cases where k is greater than n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
