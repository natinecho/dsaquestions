class FrequencyTracker:

    def __init__(self):
        self.di = {}
        self.frequency = {}     

    def add(self, number: int) -> None:
        if number in self.di and  self.di[number] in self.frequency:
            self.frequency[self.di[number]] -= 1
            if self.frequency[self.di[number]] == 0:
                del(self.frequency[self.di[number]])       


        self.di[number] = self.di.get(number,0) + 1
        self.frequency[self.di[number]] = self.frequency.get(self.di[number],0) + 1
        # print("add",number,self.di, self.frequency)
        

    def deleteOne(self, number: int) -> None:
        if number in self.di:
            self.frequency[self.di[number]] -= 1

            if self.frequency[self.di[number]] == 0:
                del(self.frequency[self.di[number]])       

            self.di[number] -= 1

            if self.di[number] == 0:
                del(self.di[number])    

        if  number in self.di:
            self.frequency[self.di[number]] = self.frequency.get(self.di[number],0) + 1

        # print("delete",number,self.di, self.frequency)

    def hasFrequency(self, frequency: int) -> bool:
        # print("frequency",frequency, self.di, self.frequency)
        return frequency in self.frequency
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)