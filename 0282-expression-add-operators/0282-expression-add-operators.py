class Solution:
    def addOperators(self, num: str, target: int):
        res = []

        def backtrack(expr, pos):
            if pos == len(num):
                if eval(expr) == target:
                    res.append(expr)

            
            for i in range(pos + 1, len(num) + 1):
                temp = num[pos:i]
                if len(temp) > 1 and temp[0] == '0':
                    continue

                if pos == 0:
                    backtrack(temp, i)
                else:
                    backtrack(expr + '+' + temp, i)
                    backtrack(expr + '-' + temp, i)
                    backtrack(expr + '*' + temp, i)

        backtrack("", 0)
        return res

    # def addOperators(self, num: str, target: int) -> List[str]:
    #     res = []

    #     def backtrack(expr, pos, prev, val):
    #         if pos == len(num):
    #             if val == target:
    #                 res.append(expr)
    #             return
            
    #         for i in range(pos + 1, len(num) + 1):
    #             temp = num[pos:i]
    #             # Skip numbers with leading zeros
    #             if len(temp) > 1 and temp[0] == '0':
    #                 continue
    #             curr_num = int(temp)

    #             if pos == 0:
    #                 # First number, pick without any operator
    #                 backtrack(temp, i, curr_num, curr_num)
    #             else:
    #                 # Addition
    #                 backtrack(expr + '+' + temp, i, curr_num, val + curr_num)
    #                 # Subtraction
    #                 backtrack(expr + '-' + temp, i, -curr_num, val - curr_num)
    #                 # Multiplication
    #                 backtrack(expr + '*' + temp, i, prev * curr_num, val - prev + prev * curr_num)

    #     backtrack("", 0, 0, 0)
    #     return res