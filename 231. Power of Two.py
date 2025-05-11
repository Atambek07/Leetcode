class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:

            k = int(n ** 0.5)
            arr = []
            for i in range(k + 2):
                if (2 ** i) == n:
                    arr.append(True)
                else:
                    arr.append(False)
            arr = set(arr)
            if len(arr) != 1:
                return True
            else:
                return False
