from prime import Prime
from key import Key
from time import time


class CreateKey:
    """
    This class has two methods for generating encryption keys.

    Method create_key generates an ecryption key with random values.

    Method create_own_key allows the user to create an enryption key with prime numbers
    and an exponent e of their own choice.
    """

    def __init__(self) -> None:
        self.prime = Prime()
        self.key = Key()

    def create_key(self, bits: int) -> dict:
        """
        Creates an encryption key with random values. The length of the key in bits is
        determined by the argument bits.

        Arguments:
        bits: length of the key in bits

        Returns:
        A dictionary containing all parts of the encryption keys"""
        # 1. Choose two primes p and q
        n = 0
        start = time()
        # The while-loop makes sure the enryption key length (length of n) is exactly
        # the number of bits as the argument bits asks for.
        print()
        print("Parittomia lukuja kokeiltu alkuluvun tuottamiseksi:")
        while n < 2 ** (bits - 1):
            # If key length is bits, then p and q should have a length of bits // 2
            p = self.prime.random_prime(bits // 2)
            q = self.prime.random_prime(bits // 2)

            # 2. Calculate n = pq
            n = p * q

        end = time()
        print()
        print()
        print("vaiheet 1-2", round(end - start, 5))
        # i tells how many pairs of primes had to be tested before an n of the desired
        # length was found.

        # 3. Calculate lambda(n) := ln using Charmichael function.
        # Since p and q are primes the problem reduces to ln = lcm(p-1, q-1),
        # where lcm means least common multiple.
        start = time()
        ln = self.key.least_common_multiple(p - 1, q - 1)
        end = time()
        print("vaihe 3", round(end - start, 5))

        # 4. Choose e that is coprime with ln.
        # We will use the default value of e = 65537. There is a small chance that
        # 65537 and ln are not coprime. In that case method multiplicative_inverse
        # in key.py raises an error.
        e = 65537

        # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
        start = time()
        d = self.key.multiplicative_inverse(e, ln)
        end = time()
        print("vaihe 5", round(end - start, 5))

        return {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}

    def create_own_key(self, p: int, q: int, e: int) -> dict | None:
        """This method allows the creation of own encryption keys.

        Arguments:
        p: a prime number
        q: a prime number
        e: an optional argument. Must be coprime with lambda(p*q) from the Carmichael function. Using e = (p-1)(q-1) should be fine too.

        Returns:
        A dictionary containing all parts of the encryption keys or None
        if any arguments are invalid"""
        check = True
        # Check p, q and e
        if e == "":
            e = 65537
        try:
            p = int(p)
            q = int(q)
            e = int(e)
        except:
            print("p, q ja e voivat olla vain kokonaislukuja")
            check = False

        if check:
            if not self.check_pq(p, q):
                check = False

        if check:
            # 2. Calculate n = pq
            n = p * q

            # 3. Calculate ln := lambda(n)
            ln = self.key.least_common_multiple(p - 1, q - 1)

            # 4. Check that e and ln are coprime.
            if not self.check_e_ln(e, ln):
                check = False

        if check:
            # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
            d = self.key.multiplicative_inverse(e, ln)

        if check:
            return {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}
        return None

    def check_pq(self, p: int, q: int) -> bool:
        """Check that p and q are primes and greater than 3"""
        check = True
        if p < 4:
            print("p ei voi olla pienempi kuin 4")
            check = False
        if q < 4:
            print("q ei voi olla pienempi kuin 4")
            check = False
        if not self.prime.miller_rabin(p):
            print("p ei ole alkuluku")
            check = False
        if not self.prime.miller_rabin(q):
            print("q ei ole alkuluku")
            check = False

        return check

    def check_e_ln(self, e: int, ln: int) -> bool:
        """Check that e and ln are coprime (not divisible with each other)"""
        check = True
        if e < 3:
            print("e ei voi olla pienempi kuin 3")
            check = False

        x = self.key.euclidean_algorithm(e, ln)
        if x != 1:
            print(
                f"e ja ln eivät ole keskenään jaottomat:",
                f"\ngcd(e, ln) = {x} \ne = {e} \nln = {ln} \n",
            )
            check = False

        return check
