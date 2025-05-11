

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = dividend / divisor
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        return int(result)


