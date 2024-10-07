import unittest
from src.prime import Prime


class TestKey(unittest.TestCase):
    def setUp(self):
        self.prime = Prime()

    def test_miller_rabin(self):
        # primes is a list of prime numbers 2-541
        primes = self.open_file("first_100_primes.csv")
        # Start from prime number 5, because the smallest argument Miller-Rabin
        # can take is 4
        j = 2
        for i in range(4, 541 + 1):
            prime = False
            if int(primes[j]) == i:
                # i is in primes so it is a prime number
                prime = True
                j += 1

            x = self.prime.miller_rabin(i)
            self.assertEqual(x, prime)

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
        # First we load the first 100 primes
        primes = self.open_file("first_100_primes.csv")
        # Now primes contains prime numbers 2 - 541. We now want to check that
        # trial_division identifies all primes and rejects all other numbers
        # in range 2 - 541.
        self.check_primes_trial_division(primes)

    def test_trial_division2(self):
        # First we load the list of primes
        primes = self.open_file("primes_81001-82000.csv")
        # Now primes contains prime numbers 1034233 - 1048129. We now want to check that
        # trial_division identifies all primes and rejects all other numbers
        # in that range.
        self.check_primes_trial_division(primes)

    def open_file(self, file_name: str):
        with open("src/tests/data/" + file_name) as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.replace(" ", "")
                primes = row.split(",")
        return primes

    def check_primes_trial_division(self, primes: list):
        """Check the trial_division algorithm. Compares a list of
        predetermined prime numbers to the answers given by the algorithm.
        Arguments:
        primes: a list of primes that is known to be correct
        trial_division: set True if trial division is tested and False if Miller Rabin
        is tested
        Returns:
        Nothing. Asserts that the anwers are equal."""
        j = 0
        for i in range(int(primes[0]), int(primes[-1]) + 1):
            prime = False
            if int(primes[j]) == i:
                # i is in primes so it is a prime number
                prime = True
                j += 1

            x = self.prime.trial_division(i)
            self.assertEqual(x, prime)

    def test_erastothenes_sieve(self):
        # primes is a list of prime numbers 2 - 7919
        primes = self.open_file("first_1000_primes.csv")
        primes = [int(prime) for prime in primes]
        test_primes = self.prime.eratosthenes_sieve(primes[-1] + 1)
        self.assertEqual(test_primes, primes)
