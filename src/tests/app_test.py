import unittest
from src.app import Prime

class TestPrime(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    #def test_eratosthenes_sieve(self):
    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")
