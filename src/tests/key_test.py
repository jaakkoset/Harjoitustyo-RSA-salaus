import unittest
import pytest
from key import Key


class TestKey(unittest.TestCase):
    def setUp(self):
        self.key = Key()

    def test_least_common_multiple(self):
        """Test least_common_multiple with small values"""
        # least_common_multiple is given a and b and it should return lcm
        examples = [
            {"a": 2, "b": 10, "lcm": 10},
            {"a": 10, "b": 2, "lcm": 10},
            {"a": 5, "b": 7, "lcm": 35},
            {"a": 100, "b": 17, "lcm": 1700},
            {"a": 271, "b": 63, "lcm": 17073},
            {"a": 44, "b": 12, "lcm": 132},
        ]
        for e in examples:
            x = self.key.least_common_multiple(e["a"], e["b"])
            self.assertEqual(
                x, e["lcm"], f"Values of a and b: a = {e['a']}, b = {e['b']}"
            )

    def test_euclidean_algorithm_small(self):
        """Test Euclidean algorithm with small values"""
        # euclidean_algorithm is given a and b and it should return gcd
        examples = [
            {"a": 2, "b": 10, "gcd": 2},
            {"a": 10, "b": 2, "gcd": 2},
            {"a": 5, "b": 7, "gcd": 1},
            {"a": 100, "b": 10, "gcd": 10},
            {"a": 271, "b": 63, "gcd": 1},
            {"a": 44, "b": 12, "gcd": 4},
        ]
        for e in examples:
            x = self.key.euclidean_algorithm(e["a"], e["b"])
            self.assertEqual(
                x, e["gcd"], f"Values of a and b: a = {e['a']}, b = {e['b']}"
            )

    def test_euclidean_algorithm_large(self):
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

    def test_extended_euclidean_algorithm_equation(self):
        """Check that the extended Euclidean algorithm finds the solution for the
        equation ax + by = gcd(a,b), when given integers a and b."""
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

    def test_multiplicative_inverse_small(self):
        """Tests the multiplicative_inverse by checking that de - 1 is divisible by ln.
        This is equivalent to testing that ed mod ln = 1.
        e and ln must be coprime. Tested values for ln are small."""
        # Use the default value of 65537 for e
        e = 65537
        # Find ln > e, that is not divisible by e
        for ln in range(e + 1, e + 40):
            if ln % e == 0:
                raise ValueError("e and ln are not coprime")
            d = self.key.multiplicative_inverse(e, ln)
            de = d * e
            self.assertEqual(de % ln, 1)

    def test_multiplicative_inverse_big(self):
        """Tests the multiplicative_inverse by checking that de - 1 is divisible by ln.
        This is equivalent to testing that ed mod ln = 1.
        e and ln must be coprime. Tested values for ln are around the size as used in
        the program."""
        # Use the default value of 65537 for e
        e = 65537
        # Determine ln > e, that is not divisible by e
        start = 10**303 * e + 1
        # Test in total 65535 values
        for ln in range(start, start + 65536):
            if ln % e == 0:
                raise ValueError("e and ln are not coprime")
            d = self.key.multiplicative_inverse(e, ln)
            de = d * e
            self.assertEqual(de % ln, 1)

    def test_multiplicative_inverse_error_small(self):
        """Test that multiplicative_inverse raises an error when arguments e and ln
        are not coprime. Because we always use a value for e that is prime, e and ln
        are not coprime if and only if ln is a multiple of e. This test uses small
        values for the multiples."""
        # Use the default value of 65537 for e
        e = 65537
        # Make multiples for ln
        for multiple in range(2, 100):
            with pytest.raises(Exception):
                self.key.multiplicative_inverse(e, multiple * e)

    def test_multiplicative_inverse_error_big(self):
        """Test that multiplicative_inverse raises an error when arguments e and ln
        are not coprime. Because we always use a value for e that is prime, e and ln
        are not coprime if and only if ln is a multiple of e. This test uses big
        values for the multiples, which are around the same size used in the program.
        """
        # Use the default value of 65537 for e
        e = 65537
        # Make multiples for ln
        start = 10**303
        for multiple in range(start, start + 100):
            with pytest.raises(Exception):
                self.key.multiplicative_inverse(e, multiple * e)
