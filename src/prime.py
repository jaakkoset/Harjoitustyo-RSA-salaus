from random import randint
from secrets import randbits


class Prime:
    """This class is used to generate prime numbers for encryption keys.

    The method random_prime generates a random prime using the Miller-Rabin algorithm.
    The argument bits determines how long the prime number will be in bits."""

    def __init__(self) -> None:
        # 301st prime is 1933
        # 500th prime is 3571
        self.sieve = self.eratosthenes_sieve(1933)

    def miller_rabin(self, n: int) -> bool:
        """Returns true when number is probably prime and false otherwise.
        Uses the Miller-Rabin algorithm.
        Arguments:
        n: an integer >= 4
        Returns:
        True when n is probably prime and False always when it is not prime"""

        if n < 4:
            raise ValueError(
                "Miller-Rabin can only accept values greater than or equal to 4."
            )
        k = 20
        s, d = self.factor_twos(n - 1)
        # Check s to make sure we don't waste time checking even numbers. When s = 0,
        # n-1 is odd, and n must be even.
        if s == 0:
            return False

        for _ in range(k):
            a = randint(2, n - 2)
            x = pow(a, d, n)
            for _ in range(s):
                y = pow(x, 2, n)
                if y == 1 and x != 1 and x != n - 1:
                    return False
                x = y
            if y != 1:
                return False
        return True

    def factor_twos(self, n):
        """For a given integer n, solves s and d in n = 2^s * d
        and returns a tuple (s, d)."""
        s = 0
        while n % 2 == 0:
            s += 1
            n = n // 2
        return s, n

    def trial_division(self, nro: int) -> bool:
        """Returns true when the argument is prime and false otherwise. This is the
        simplest algorithm to test whether a given number is prime but it is
        inefficient. That is why it is only used to test the method random_prime
        with small values."""

        i = 2
        while i * i <= nro:
            if nro % i == 0:
                return False
            i += 1
        return True

    def random_prime(self, bits: int):
        """Returns a random prime number using Miller-Rabin algorithm. The length
        of the prime is determined in terms of bits."""
        while True:

            # Make sure n has the number of bits as the argument bits defines.
            # randbits() returns numbers that are less than or equal to the given bit
            # length. The while loop makes sure the number is always exactly the given
            # bit length.
            n = 0
            while n < 2 ** (bits - 1):
                n = randbits(bits)
                # Make sure n is not even
                if n % 2 == 0:
                    n += 1

            # Try dividing n with the first 300 primes, so that we don't give
            # the Miller-Rabin algorithm poor prime candidates.
            check = True
            for s in self.sieve:
                if n % s == 0:
                    check = False

            if check:
                if self.miller_rabin(n):
                    return n

    def eratosthenes_sieve(self, n: int) -> list:
        """Calculates all primes up to n.
        Arguments:
        n: the last value we want to check for primality
        Returns:
        primes: list of prime numbers between 0 and n"""
        # The list primes should start from index 2 and end at n. The first two True values are
        # therefore unneeded, but created to simplify the usage of indeces.
        primes = [True for _ in range(n + 1)]
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
