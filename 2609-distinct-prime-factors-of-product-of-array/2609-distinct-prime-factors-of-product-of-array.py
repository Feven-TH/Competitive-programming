class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        for n in nums:
            while n % 2 == 0:
                primes.add(2)
                n //= 2

            for i in range(3, int(sqrt(n))+1, 2):
                while n % i == 0:
                    primes.add(i)
                    n //= i
            if n > 2:
                primes.add(n)
        
        return len(primes)