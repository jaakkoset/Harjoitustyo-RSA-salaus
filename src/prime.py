from random import randint


class Prime:
    """This class is used to generate prime numbers for encryption keys"""

    def miller_rabin(self, n) -> bool:
        """Function returns true when number is probably prime and false otherwise.
        Uses the Miller-Rabin algorithm"""
        k = 40
        s, d = self.factor_twos(n - 1)
        if s == 0:
            # Make sure we don't waste time checking even numbers.
            # When s = 0 then n-1 is odd, and then n must be even.
            raise ValueError("Even number given to Miller-Rabin")
        for i in range(k):
            a = randint(2, n - 2)
            x = pow(a, d, n)
            for j in range(s):
                y = pow(x, 2, n)
                if y == 1 and x != 1 and x != n - 1:
                    return False
                x = y
            if y != 1:
                return False
        return True

    def factor_twos(self, n):
        """For the given integer n solves s and d in n = 2^s * d
        and returns a tuple (s, d)."""
        s = 0
        while n % 2 == 0:
            s += 1
            n = n // 2
        return s, n

    def trial_division(self, nro: int) -> bool:
        """Returns true when the given number is prime and false otherwise.
        This is the simplest algorithm to test whether a given number is prime.
        It is inefficient with large numbers."""
        i = 2
        while i * i <= nro:
            if nro % i == 0:
                return False
            i += 1
        return True

    def random_prime_trial_division(self, a=10**7, b=10**8):
        """Function returns a smallish random prime number between a and b using trial division."""
        while True:
            n = randint(a, b)
            if self.trial_division(n):
                return n

    def random_prime(self, a=10**399, b=10**400):
        """Function returns a random prime number between a and b using Miller-Rabin."""
        while True:

            n = randint(a, b)
            if n % 2 != 0:
                n += 1

            if self.miller_rabin(n):
                return n

    def eratosthenes_sieve(self, n):
        """Function calculates all primes up to n."""
        # The list primes should start from index 2 and end at n. The first two True values are
        # therefore unneeded, but created to simplify the usage of indeces.
        primes = [True for i in range(n + 1)]
        primes[0] = "NA"
        primes[1] = "NA"
        i = 2
        while i * i <= n:
            if primes[i]:
                j = i**2
                while j <= n:
                    primes[j] = False
                    j += i
            i += 1

        primes = [i for i in range(2, n + 1) if primes[i]]
        return primes
