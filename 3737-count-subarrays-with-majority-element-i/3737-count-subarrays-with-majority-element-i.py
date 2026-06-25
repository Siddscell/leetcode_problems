from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Instead of directly checking if target is the majority in every subarray,
        # convert the array into:
        #
        #   target      -> +1
        #   everything else -> -1
        #
        # Now for any subarray:
        #
        # sum = (#target) - (#other elements)
        #
        # If target is the majority:
        #
        #     #target > #others
        #
        # which is exactly the same as:
        #
        #     (#target - #others) > 0
        #
        # So the original problem becomes:
        # "Count subarrays whose transformed sum is greater than 0."

        n = len(nums)

        # Prefix sums can range from -n to +n.
        # BIT only works with positive indices, so shift everything by an offset.
        offset = n + 1
        size = 2 * n + 5

        bit = [0] * size

        def update(idx):
            # Insert one occurrence of this prefix sum.
            while idx < size:
                bit[idx] += 1
                idx += idx & -idx

        def query(idx):
            # Returns how many stored prefix sums have index <= idx.
            cnt = 0
            while idx > 0:
                cnt += bit[idx]
                idx -= idx & -idx
            return cnt

        ans = 0
        pref = 0

        # Prefix sum before starting the array is 0.
        # This is important because subarrays can start from index 0.
        update(offset + 1)

        for num in nums:

            # Build the transformed prefix sum.
            if num == target:
                pref += 1
            else:
                pref -= 1

            # Convert prefix sum into a valid BIT index.
            idx = pref + offset + 1

            # Let current prefix sum be P.
            #
            # For any previous prefix sum X:
            #
            # subarray_sum = P - X
            #
            # We want subarray_sum > 0
            #
            # => P > X
            #
            # So count how many previous prefix sums are STRICTLY smaller
            # than the current one.
            ans += query(idx - 1)

            # Store current prefix sum so future subarrays can use it.
            update(idx)

        return ans