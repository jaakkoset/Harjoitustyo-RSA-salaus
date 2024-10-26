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
        """Test that all parts of a random 1024 bit key are correct"""
        # The key is in a dictionary {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}
        key = self.create.create_key(1024)
        self.check_key(key)

    def check_key(self, key):
        """Helper function. Check that all parts of the key are correct"""
        # Check p and q are primes
        a = self.prime.miller_rabin(key["p"])
        b = self.prime.miller_rabin(key["q"])
        self.assertTrue(a and b)
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

    def test_create_own_key_small(self):
        """Test creating an own key with example values."""
        example = {"p": 61, "q": 53, "n": 3233, "e": 17, "ln": 780, "d": 413}
        # When we give p, q and e to create_own_key, other values should be the same
        # as in the example key.
        key = self.create.create_own_key(61, 53, 17)
        for k in example:
            self.assertEqual(example[k], key[k])

    def test_create_own_key_big(self):
        """Test creating an own key with randomly generated big primes"""
        p = self.prime.random_prime(512)
        q = self.prime.random_prime(512)
        key = self.create.create_own_key(p, q, "")
        self.check_key(key)

    def test_create_own_key_default_e(self):
        """Test that e gets its default value when an empty string is given as an
        argument"""
        key = self.create.create_own_key(61, 53, "")
        self.assertEqual(key["e"], 65537)

    # def test_create_own_key_(self):
