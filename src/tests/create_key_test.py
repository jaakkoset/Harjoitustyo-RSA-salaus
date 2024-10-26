import unittest
from create_key import CreateKey
from prime import Prime
from key import Key


class TestCreateKey(unittest.TestCase):
    def setUp(self):
        self.create = CreateKey()
        self.prime = Prime()
        self.key = Key()

    def test_create_key_1024(self):
        """Test that all parts of a 1024 bit key are correct"""
        # The key is in a dictionary {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}
        key = self.create.create_key(1024)
        # Check p and q are primes
        self.assertTrue(self.p_q_are_primes(key["p"], key["q"]))
        # Check n = p * q
        self.assertEqual(key["n"], key["p"] * key["q"])
        # Check ln = lcm(p-1, q-1) = abs((p-1)(q-1)) / gcd(p-1, q-1)
        a = key["p"] - 1
        b = key["q"] - 1
        ln = abs(a * b) // self.key.euclidean_algorithm(a, b)
        self.assertEqual(key["ln"], ln)
        # Check d is the modular multiplicative inverse of e mod lambda(n).
        # That is de - 1 is divisible by ln.
        self.assertTrue((key["d"] * key["e"] - 1) % key["ln"] == 0)

    def p_q_are_primes(self, p: int, q: int):
        """Helper function for test_create_key_1024. Check that p and q are primes"""
        a = self.prime.miller_rabin(p)
        b = self.prime.miller_rabin(q)
        if a and b:
            return True
        return False

    def test_create_own_key(self):
        """Test creating an own key with example values."""
        example = {"p": 61, "q": 53, "n": 3233, "e": 17, "ln": 780, "d": 413}
        key = self.create.create_own_key(61, 53, 17)
        for k in example:
            self.assertEqual(example[k], key[k])
