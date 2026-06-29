from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        # Check every pattern.
        # If it appears anywhere inside 'word', increase the answer.
        for pattern in patterns:
            if pattern in word:
                count += 1

        return count