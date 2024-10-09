from prime import Prime
from key import Key
from time import time


class Generator:
    """This class is for generating encryption keys"""

    def __init__(self) -> None:
        self.prime = Prime()
        self.key = Key()

    def create_key(self, bits: int) -> dict:
        """Creates an encryption key with random values. The length of the
        key in bits is determined by the argument bits.
        Arguments:
        bits: length of the key in bits
        Returns:
        A dictionary containing all parts of the encryption keys"""
        # 1. Choose two primes p and q
        start = time()
        p = self.prime.random_prime(bits)
        q = self.prime.random_prime(bits)
        end = time()
        print()
        print("vaihe 1", round(end - start, 5))

        # 2. Calculate n = pq
        start = time()
        n = p * q
        end = time()
        print("vaihe 2", round(end - start, 5))

        # 3. Calculate lambda(n) := ln using Charmichael function.
        # Since p and q are primes the problem reduces to ln = lcm(p-1, q-1),
        # where lcm means least common multiple.
        start = time()
        ln = self.key.lcm(p - 1, q - 1)
        end = time()
        print("vaihe 3", round(end - start, 5))

        # 4. Choose e that is coprime with ln.
        # We will use the default value of e = 65537.
        start = time()
        e = 65537
        if ln % e == 0:
            # There is a very small chance that ln is divisble by e.
            raise RuntimeError("When creating keys, lambda(n) was divisible by e")
        end = time()
        print("vaihe 3", round(end - start, 5))

        # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
        start = time()
        d = self.key.multiplicative_inverse(e, ln)
        end = time()
        print("vaihe 5", round(end - start, 5))

        return {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}

    def create_own_key(self, p: int, q: int, e: int = 65537) -> dict | None:
        """This method allows the creation of own encryption keys.
        Arguments:
        p: a prime number
        q: a prime number
        e: an optional argument. Must be coprime with lambda(n) from the Carmichael function
        Returns:
        A dictionary containing all parts of the encryption keys or None
        if any arguments are invalid"""
        check = True
        # Check p, q and e
        try:
            p = int(p)
            q = int(q)
            e = int(e)
        except:
            print("p, q ja e voivat olla vain kokonaislukuja")
            check = False

        if check:
            if not self.check_pqe(p, q, e):
                check = False

            if check:
                # 2. Calculate n = pq
                n = p * q

                # 3. Calculate lambda(n) := ln
                ln = self.key.lcm(p - 1, q - 1)

                # 4. Check that e and ln are coprime.
                if not self.check_e_ln(e, ln):
                    check = False

            if check:
                # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
                d = self.key.multiplicative_inverse(e, ln)

        if not check:
            return None
        return {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}

    def check_pqe(self, p, q, e) -> bool:
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

    def check_e_ln(self, e, ln) -> bool:
        check = True
        if e < 2:
            print("e ei voi olla pienempi kuin 2")
            check = False

        x = self.key.euclidean_algorithm(e, ln)
        if x != 1:
            print(
                f"\ne ja ln eivät ole keskenään jaottomat:",
                f"\ngcd(e, ln) = {x} \ne = {e} \nln = {ln} \n",
            )
            check = False

        return check
