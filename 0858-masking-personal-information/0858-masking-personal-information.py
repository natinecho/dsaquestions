class Solution:
    def maskPII(self, s: str) -> str:
        
        #if email
        if s[0].isalpha():
            ans = []
            ss = s.split("@")
            ans.append(ss[0][0].lower() + "*****" + ss[0][-1].lower() + "@")
            # temp = ss[1].split(".")
            ans.append(ss[1].lower())

            return "".join(ans)

        digits = ""

        for c in s:
            if c.isdigit():
                digits += c
        
        ans = ["***-***-","+*-***-***-","+**-***-***-","+***-***-***-"]

        return ans[len(digits)  % 10] + digits[-4:]





                    
        