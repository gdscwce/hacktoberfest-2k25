# ==============================================
# Project: Minimum Flips to Make a OR b Equal to c
# Language: Python 3
# Description:
#   Given three integers a, b, c, return the minimum number of bit flips
#   required in a and b so that (a OR b) == c.
# ==============================================

class BitFlipper:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if (bitA | bitB) != bitC:
                if bitC == 1:
                    flips += 1
                else:
                    flips += bitA + bitB  # flip both if needed

            a >>= 1
            b >>= 1
            c >>= 1

        return flips


if __name__ == "__main__":
    flipper = BitFlipper()

    print("=============================================")
    print("   MINIMUM FLIPS TO MAKE a OR b EQUAL TO c")
    print("=============================================")

    a, b, c = 2, 6, 5
    print(f"Input: a = {a}, b = {b}, c = {c}")
    print("Minimum Flips Needed:", flipper.minFlips(a, b, c))

    print("\nProgram completed successfully!")
