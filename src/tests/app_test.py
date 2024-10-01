import unittest
from src.app import Prime

class TestPrime(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_eratosthenes_sieve_up_to_271(self):
        prime = Prime()
        list = prime.eratosthenes_sieve(271)
        self.assertEqual(list, prime.first_58_primes)

    def test_factor_twos(self):
        prime = Prime()
        a = prime.factor_twos(1408)
        b = prime.factor_twos(512)
        c = prime.factor_twos(6272)
        d = prime.factor_twos(2)
        self.assertEqual(a, (7, 11))
        self.assertEqual(b, (9, 1))
        self.assertEqual(c, (7, 49))
        self.assertEqual(d, (1, 1))
