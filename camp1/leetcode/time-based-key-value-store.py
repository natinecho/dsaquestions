class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value,timestamp])
 

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key in self.data:
            temp = self.data[key]
            l = 0
            r = len(temp)-1
            while l<=r:
                m = (l+r)//2
                if temp[m][1] > timestamp:
                    r = m - 1
                elif temp[m][1] == timestamp:
                    return temp[m][0]
                else:
                    ans = temp[l][0]
                    l = m + 1

            return ans

        else:
            return ''
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)