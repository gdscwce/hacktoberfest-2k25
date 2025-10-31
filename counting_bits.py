# ==============================================
# Project: Counting Bits
# Language: Python 3
# Description:
#   For every number i in range(0, n),
#   return the count of 1's in the binary representation of i.
# ==============================================

from typing import List

class BitCounter:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            # Use dynamic programming relation:
            # result[i] = result[i >> 1] + (i & 1)
            result[i] = result[i >> 1] + (i & 1)
        return result


if __name__ == "__main__":
    counter = BitCounter()

    print("=============================================")
    print("             COUNTING BITS PROJECT")
    print("=============================================")

    n = 10
    print(f"Input: n = {n}")
    print("Output:", counter.countBits(n))

    print("\nProgram completed successfully!")
