import unittest
from src.key import Key


class TestKey(unittest.TestCase):
    def setUp(self):
        self.key = Key()

    def test_lcm(self):
        examples = [
            (2, 10, 10),
            (10, 2, 10),
            (5, 7, 35),
            (100, 17, 1700),
            (271, 63, 17073),
            (44, 12, 132),
        ]
        for e in examples:
            x = self.key.lcm(e[0], e[1])
            self.assertEqual(x, e[2])

    def test_euclidean_algorithm(self):
        examples = [
            (2, 10, 2),
            (10, 2, 2),
            (5, 7, 1),
            (100, 10, 10),
            (271, 63, 1),
            (44, 12, 4),
        ]
        for e in examples:
            x = self.key.euclidean_algorithm(e[0], e[1])
            self.assertEqual(x, e[2])

    def test_euclidean_algorithm2(self):
        """Compares the results from the euclidian_algorithm and the
        extended_euclidian_algorithm"""
        examples = [
            (
                4409871243509762459762509187234560872102187465 * 10**2001,
                108176508625087621085612087608721364320198262 * 10**200,
            ),
            (
                8217958194584379475987451215660981642576128065219876358021630947109182098214375,
                9875219145140987324087623598712905876453508612385682658263416205361982659821659821658216360983,
            ),
        ]
        for e in examples:
            x = self.key.euclidean_algorithm(e[0], e[1])
            y = self.key.extended_euclidian_algorithm(e[0], e[1])
            self.assertEqual(x, y["gcd"])

    def test_extended_euclidean_algorithm(self):
        examples = [
            (2, 10, 2, (1, 0)),
            (240, 46, 2, (-9, 47)),
        ]
        for e in examples:
            # extended_euclidean_algorithm returns a dictionary
            # {"coefficients": (x, y), "gcd": (gcd)}.
            x = self.key.extended_euclidian_algorithm(e[0], e[1])
            self.assertEqual(x["gcd"], e[2])
            self.assertEqual(x["coefficients"], e[3])

    def test_extended_euclidean_algorithm2(self):
        """Checks that the equation ax + by = gcd(a,b) holds."""
        examples = [
            (240, 46),
            (242130, 412321166),
        ]
        for e in examples:
            # extended_euclidean_algorithm returns a dictionary
            # {"coefficients": (x, y), "gcd": (gcd)}.
            x = self.key.extended_euclidian_algorithm(e[0], e[1])
            left = e[0] * x["coefficients"][0] + e[1] * x["coefficients"][1]
            right = x["gcd"]
            self.assertEqual(left, right)

    def test_multiplicative_inverse(self):
        """Tests the multiplicative_inverse by checking that de - 1 is divisible by ln.
        This is equivalent to testing that ed mod ln = 1.
        e and ln must be coprime."""
        # Use the default value of 65537 for e
        e = 65537
        # Find ln > e, that is not divisible by e
        lns = [e * 10**200 + 1, 98761234598765796143875]
        for ln in lns:
            if ln % e == 0:
                raise ValueError("ln is divisible by e")
            d = self.key.multiplicative_inverse(e, ln)
            de = d * e
            self.assertEqual(de % ln, 1)
