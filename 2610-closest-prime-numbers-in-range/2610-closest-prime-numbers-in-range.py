class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        

        def Sieve(l,r):
            primes = [1]*(r + 1)
            primes[0],primes[1] = 0,0

            for i in range(2,isqrt(r + 1) + 1):
                if primes[i] == 1:
                    ll = i * i
                    while ll < (r + 1):
                        primes[ll] = 0
                        ll += i
            
            return [val for val in range(l,r + 1) if primes[val] == 1]


        prime = Sieve(left,right)

        minn = [-1,-1]
        minn_diff = float("inf")


        for i in range(1,len(prime)):
            if prime[i] - prime[i -1] < minn_diff:
                minn = [prime[i - 1], prime[i]]
                minn_diff = prime[i] - prime[i -1] 

        
        return minn





        