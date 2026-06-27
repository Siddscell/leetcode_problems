from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count how many times each number appears.
        freq = Counter(nums)

        ans = 1  # at least one number can always form [x]

        for x, cnt in freq.items():
            # Special case:
            # 1 is different because 1^2 = 1, 1^4 = 1, ...
            # So a valid subset made only of 1s must have odd length.
            if x == 1:
                # Use the biggest odd number <= cnt
                ans = max(ans, cnt if cnt % 2 == 1 else cnt - 1)
                continue

            # For x > 1, build the chain:
            # x -> x^2 -> x^4 -> x^8 -> ...
            #
            # Every value except the last one must appear at least 2 times,
            # because the pattern uses them on both sides.
            #
            # The last value only needs to exist once.
            length = 1
            cur = x

            while True:
                nxt = cur * cur

                # If the next power is not present, the chain stops here.
                if nxt not in freq:
                    break

                # If cur is going to be used as a middle value,
                # it must appear at least twice.
                if freq[cur] < 2:
                    break

                cur = nxt
                length += 1

            # If the chain has 'length' distinct values,
            # the final subset size is:
            # 2 * length - 1
            # Example:
            # [x, x^2, x^4, x^2, x] -> length = 3 -> size = 5
            ans = max(ans, 2 * length - 1)

        return ans