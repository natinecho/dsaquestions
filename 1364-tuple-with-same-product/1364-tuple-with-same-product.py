class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = {}

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]*nums[j] in products:
                    products[nums[i]*nums[j]] += 1
                else:
                    products[nums[i]*nums[j]] = 1

        
        ans = 0
        print(products)

        for val in products.values():
            ans += ((val * (val - 1))//2)* 8
        
        return ans



        