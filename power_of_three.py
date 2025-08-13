class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_power_of_three = 1162261467
        return n > 0 and max_power_of_three % n == 0
