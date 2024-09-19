class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ans = 0


        for i in range(len(columnTitle)):
            # val = ord(n % 26) - 1 if n % 26 != 0 else 25
            # arr.append(chr(65 + val ))
            ans *=  26
            ans += (ord(columnTitle[i]) - 65) + 1

            # print(n, n % 26)
            # if n % 26 == 0:
            #     n = (n*26) - 1
            # else:
            #     n //= 26

        # print(arr)

        
        return ans