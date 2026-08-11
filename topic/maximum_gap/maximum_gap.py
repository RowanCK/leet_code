from typing import List, Optional, Tuple

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        maxVal = max(nums)
        minVal = min(nums)

        bucketSize = max(
            1,
            (maxVal - minVal) // (len(nums) - 1)
        )

        bucketCount = (maxVal - minVal) // bucketSize + 1
        buckets: List[Optional[Tuple[int, int]]] = [None] * bucketCount

        for num in nums:
            bucketIndex = (num - minVal) // bucketSize
            bucket = buckets[bucketIndex]

            if bucket is None:
                buckets[bucketIndex] = (num, num)
            else:
                buckets[bucketIndex] = (
                    min(bucket[0], num),
                    max(bucket[1], num)
                )

        maxGap = 0
        prevMax: Optional[int] = None

        for bucket in buckets:
            if bucket is None:
                continue

            currentMin, currentMax = bucket

            if prevMax is not None:
                maxGap = max(maxGap, currentMin - prevMax)

            prevMax = currentMax

        return maxGap
