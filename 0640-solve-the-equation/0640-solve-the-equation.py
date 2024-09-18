class Solution:
    def solveEquation(self, equation: str) -> str:
        splited = equation.split("=")

        def check(arr):
            i = 0
            Xl = 0
            num = 0
            while i < len(arr):
                temp = arr[i]
                i += 1 

                while i < len(arr) and arr[i] != "+" and arr[i] != "-":
                    temp += arr[i]
                    i += 1 

                if "x" in temp:
                    val = temp.split("x")
                    if not val[0]:
                        Xl += 1
                    elif val[0][0] == "+":
                        if val[0][1:] != "":
                            Xl += int(val[0][1:])
                        else:
                            Xl += 1
                    elif val[0][0] == "-":
                        if val[0][1:] != "":
                            Xl -= int(val[0][1:])
                        else:
                            Xl -= 1
                    else:
                        Xl += int(val[0])
                else:
                    if temp[0] == "+":
                        num += int(temp[1:]) 
                    elif temp[0] == "-":
                        num -= int(temp[1:])
                    else:
                        num += int(temp)

            return num,Xl

        num,xl = check(splited[0])
        num2,xr = check(splited[1])

        xl -= xr
        num2 -= num

        if xl < 0:
            xl = abs(xl)
            num2 = -num2

        val = gcd(xl,num2)

        # print(xl,num2)
        if xl == num2 and xl == 0:
            return "Infinite solutions"
        
        if xl == 0:
            return "No solution"


        return f'{xl // val}x={num2 // val}' if xl // val > 1 else f'x={num2 // val}'
