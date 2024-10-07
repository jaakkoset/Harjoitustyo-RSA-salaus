import unittest
from src.prime import Prime


class TestKey(unittest.TestCase):
    def setUp(self):
        self.prime = Prime()

    def test_factor_twos(self):
        """factor_twos returns s and d in n = 2^s * d,
        when given an argument n. In operation n is always even."""
        examples = [
            # Small even number
            {"number": (2**3 * 3), "factors": (3, 3)},
            {"number": (24), "factors": (3, 3)},
            # Small odd number
            {"number": (2**3 * 3 + 1), "factors": (0, 25)},
            # Large even number
            {
                "number": (2**401 * 1971598874681685108651803),
                "factors": (401, 1971598874681685108651803),
            },
            # Large odd number.
            {
                "number": (2**401 * 1971598874681685108651803 + 1),
                "factors": (0, 2**401 * 1971598874681685108651803 + 1),
            },
        ]
        for e in examples:
            x = self.prime.factor_twos(e["number"])
            self.assertEqual(x, e["factors"])

    def test_trial_division(self):
        # First we load first 100 primes
        with open("src/tests/data/first_100_primes.csv") as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.replace(" ", "")
                primes = row.split(",")
        # Now primes contains prime numbers 2 - 541. We now want to check that
        # trial_division identifies all primes and rejects all other numbers
        # in range 2 - 541.
        j = 0
        for i in range(2, int(primes[-1]) + 1):
            prime = False
            if int(primes[j]) == i:
                # i is in primes so it is a prime number
                prime = True
                j += 1

            x = self.prime.trial_division(i)
            self.assertEqual(x, prime)
