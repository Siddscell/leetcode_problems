from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort first so we can build the final array from left to right.
        # The idea is to keep the numbers as small as possible,
        # because smaller values make it easier to satisfy abs diff <= 1.
        arr.sort()

        # The first element must become 1.
        arr[0] = 1

        # Walk through the array and fix each value.
        for i in range(1, len(arr)):
            # Current value should not be more than previous + 1.
            # If it is bigger, we decrease it.
            # If it is already small enough, we keep it.
            arr[i] = min(arr[i], arr[i - 1] + 1)

        # After this process, the last element is the maximum possible value.
        return arr[-1]