class Key:
    """This class offers functions necessary in key creation"""

    def lcm(self, a, b):
        """Calculates the least common multiple of a and b."""
        # lcm(a, b) = abs(ab) / gcd(a,b)
        # gcd means greatest common divisor and can be calculated with the euclidean algorithm
        gcd = self.euclidean_algorithm(a, b)
        absolute = abs(a * b)
        ln = absolute // gcd
        return ln

    def euclidean_algorithm(self, a, b):
        """Euclidean algorithm solves the greatest common divisor gcd."""
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    def multiplicative_inverse(self, e: int, ln: int) -> int:
        """
        Determines the secret key d using a reduced version of the extended
        euclidian algorithm. Here d is the modular multiplicative inverse of
        e modulo lambda(n), meaning de = 1 (mod lambda(n)). This can be solved
        efficiently using the extended Euclidean algorithm. Because e and
        lambda(n) are coprime, the Bezout identity (ax + by = gcd(a,b)) reduces to

        e*d + ln*y = gcd(e, ln)
        e*d + ln*y = 1
        e*d - 1 = (-y)ln
        e*d = 1 (mod ln).

        Using this reduced version of the extended Euclidian algorithm, we calculate
        only the coefficient d, which is all we need (the extended Euclidean algorithm
        would also return y and gcd).

        Arguments:
        e: Exponent e
        ln: The result lambda(n) from Carmichael function

        Returns:
        d: The secret key d
        """
        d = 0
        new_d = 1
        r = ln
        newr = e

        while newr != 0:
            quotient = r // newr

            var = d
            d = new_d
            new_d = var - quotient * new_d

            var = r
            r = newr
            newr = var - quotient * newr

        if r > 1:
            raise ValueError("e and ln are not coprime")
        if d < 0:
            d = d + ln

        return d

    def extended_euclidian_algorithm(self, a, b):
        """Extended Euclidian algorithm solves the gcd of a and b as well as the
        coefficients x and y of Bezout's identity ax + by = gcd(a,b).
        In creating keys this method is replaced by the method multiplicative_inverse
        and is only to test it and the method euclidean_algorithm.
        """
        # r stands for remainder.
        old_r, r = a, b
        # s and r will be the Bezout's coefficients
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            quotient = old_r // r

            # calculate the remainder of old_r / r
            var = r
            r = old_r - quotient * var
            old_r = var

            # calculate the Bezout's coefficients.
            # At the end of the algorithm Bezout's coefficients are old_s and old_t.
            var = s
            s = old_s - quotient * s
            old_s = var

            var = t
            t = old_t - quotient * t
            old_t = var

        return {"coefficients": (old_s, old_t), "gcd": (old_r)}
