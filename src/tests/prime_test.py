import unittest
from prime import Prime


class TestPrime(unittest.TestCase):
    """Tests other functions than miller-rabin."""

    def setUp(self):
        self.prime = Prime()

    def test_factor_twos(self):
        """factor_twos returns s and d in n = 2^s * d, when given an argument n. When
        factor_twos is used in the program, n is always even."""
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

    def test_trial_division_small(self):
        """Tests trial division with numbers between 2 and 541. Checks that trial
        division accepts all primes and rejects all composites in that range."""
        primes = self.open_file("first_100_primes.csv")
        self.check_primes_trial_division(primes)

    def test_trial_division_large(self):
        """Tests trial division with numbers between 1034233 and 1048129. Checks that
        trial division accepts all primes and rejects all composites in that range."""
        primes = self.open_file("primes_81001-82000.csv")
        self.check_primes_trial_division(primes)

    def check_primes_trial_division(self, primes: list):
        """
        Helper function for the trial_division tests. Compares a list of
        predetermined prime numbers to the answers given by the trial by division
        algorithm. Asserts that trial division identifies all the numbers in the list
        as primes and numbers not in the list as composites.

        Arguments:
        primes: a list of primes that is known to be correct.
        """
        # j points the next prime in the list
        j = 0
        # i is a number between the first and last prime
        for i in range(int(primes[0]), int(primes[-1]) + 1):
            # assume i is not prime
            prime = False
            if int(primes[j]) == i:
                # i is in primes so it is a prime number
                prime = True
                j += 1

            x = self.prime.trial_division(i)
            self.assertEqual(x, prime)

    def test_random_prime(self):
        """Test random_prime by comparing the results with trial_division. Tests 50
        random primes that are up to 30 bits long."""
        for _ in range(50):
            x = self.prime.random_prime(30)
            y = self.prime.trial_division(x)
            self.assertTrue(y, f"random_prime generated a non prime number {x}")

    def test_erastothenes_sieve(self):
        """Test erastothenes_sieve by calculating primes up to 7919 and
        comparing the result with a predetermined list"""
        # primes is a list of prime numbers between 2 - 7919
        primes = self.open_file("first_1000_primes.csv")
        primes = [int(prime) for prime in primes]
        test_primes = self.prime.eratosthenes_sieve(primes[-1] + 1)
        self.assertEqual(test_primes, primes)

    def open_file(self, file_name: str):
        """Reads files with prime numbers and returns the primes in a list. Works
        with files where the primes are in one row and separated by a comma."""
        with open("src/tests/data/" + file_name) as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.replace(" ", "")
                primes = row.split(",")
        return primes
