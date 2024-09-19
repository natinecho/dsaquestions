class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        n = columnNumber


        while n > 0:
            val = (n % 26) - 1 if n % 26 != 0 else 25
            arr.append(chr(65 + val ))

            # print(n, n % 26)
            if n % 26 == 0:
                n = (n//26) - 1
            else:
                n //= 26

        # print(arr)

        
        return "".join(arr[::-1])