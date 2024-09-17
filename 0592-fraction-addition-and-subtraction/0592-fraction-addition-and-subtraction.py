class Solution:
    def Calc(self,ss1,ss2,sign1,sign2):
        s1 = ss1.split("/")
        s2 = ss2.split("/")

        num1 = int(s1[0]) * int(s2[1])
        num2 = int(s1[1]) * int(s2[0])

        denom = int(s2[1]) * int(s1[1])

        ans = 0
        sign = "+"
        if sign1 == "+" and sign2 == "+":
            ans = num1  + num2 
        elif sign1 == "-" and sign2 == "-":
            ans = num1  + num2
            sign = "-"
        else:
            if sign1 == "-":
                ans = - num1 + num2
            else:
                ans = num1 - num2

        temp = gcd(ans,denom)

        if ans < 0:
            sign = "-"
            ans = abs(ans)

        return sign + str(ans//temp) + "/"+ str(denom//temp)

    def fractionAddition(self, expression: str) -> str:
        ans = "+0/1"
        if expression[0] != "-":
            expression = "+" + expression

        i = 0
        while i < len(expression):
            temp = expression[i]
            i += 1

            while i < len(expression) and (expression[i] != "+" and expression[i] != "-"):
                temp += expression[i]
                i += 1

            ans = self.Calc(ans[1:],temp[1:],ans[0],temp[0])


        return ans if ans[0] == "-" else ans[1:]
             


        