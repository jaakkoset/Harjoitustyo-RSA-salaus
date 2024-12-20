import unittest
import pytest
from prime import Prime
import re


class TestPrime(unittest.TestCase):
    """Tests for the Miller-Rabin algorithm"""

    def setUp(self):
        self.prime = Prime()
        self.file = OpenFile()
        self.mersenne_primes = [
            2**61 - 1,
            2**31 - 1,
            2**89 - 1,
            2**107 - 1,
            2**127 - 1,
            2**521 - 1,
            2**607 - 1,
            2**1279 - 1,
            2**2203 - 1,
        ]

    def test_miller_rabin_less_than_4(self):
        """Test that Miller-Rabin raises a ValueError when it is given a value less
        than four."""
        # Test values -1 to 3
        for i in range(-1, 4):
            with pytest.raises(ValueError):
                self.prime.miller_rabin(i)

    def test_miller_rabin_small(self):
        """Test Miller-Rabin with small values of 4-541"""
        # primes is a list of prime numbers 2-541
        primes = self.file.open_file_comma("first_100_primes.csv")
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

    def test_miller_rabin_medium(self):
        """Test Miller-Rabin with values between 961 748 941 and 961 766 053.
        That is 800 primes and 17 112 values in total"""

        # Primes is a list of primes
        primes = self.file.open_file_space("primes50.txt", 100)
        j = 0
        for i in range(int(primes[0]), int(primes[-1]) + 1):
            # assume i is not prime, unless it is found from the list primes
            prime = False
            if int(primes[j]) == i:
                # i is on the list primes so it is a prime number
                prime = True
                j += 1

            # test what Miller-Rabin algorithm says about i
            test = self.prime.miller_rabin(i)
            # Sometimes rarely Miller-Rabin may misidentify a prime number as a
            # composite number. It should never, however, claim that a composite
            # number is a prime number.
            msg = (
                f"Tested number: {i}"
                f"\nThe tested number was prime: {prime}"
                f"\nMiller-Rabin claimed it was a prime: {test}"
            )
            self.assertEqual(test, prime, msg)

    def test_miller_rabin_mersenne_primes(self):
        """Test Miller-Rabin using nine large Mersenne primes."""
        mersenne_primes = self.mersenne_primes
        for prime in mersenne_primes:
            x = self.prime.miller_rabin(prime)
            self.assertTrue(
                x, "Miller-Rabin claimed that a Mersenne prime is not prime"
            )

    def test_miller_rabin_composites_from_mersenne_primes(self):
        """Test Miller-Rabin with composites created from Mersenne primes.
        The composites are created by multiplying pairs of Mersenne primes."""
        mersenne_primes = self.mersenne_primes
        for i in range(len(mersenne_primes)):
            for j in range(i + 1, len(mersenne_primes)):
                composite = mersenne_primes[i] * mersenne_primes[j]
                test = self.prime.miller_rabin(composite)
                self.assertFalse(test, "Miller-Rabin claimed that a composite is prime")

    def test_miller_rabin_rsa_challenge_composites(self):
        """Test Miller-Rabin with 45 large composite numbers from the RSA-challenge.
        The numbers are in the rsa-challenge.txt file."""
        numbers = self.file.open_file_rsa_challenge()
        # Make sure 45 numbers were copied
        if len(numbers) != 45:
            raise RuntimeError(
                "Wrong amount of numbers were copied from rsa-challenge.txt"
            )
        for number in numbers:
            self.assertFalse(self.prime.miller_rabin(number))

    def test_miller_rabin_rsa_challenge_primes(self):
        """Test Miller-Rabin with 46 large primes. The primes are the known
        solutions for the the RSA-challenge. 23 of the RSA-challenge
        numbers have been solved."""
        numbers = self.file.open_file_space("rsa-challenge_solutions.txt", 46)
        # Make sure 46 primes were copied
        if len(numbers) != 46:
            raise RuntimeError(
                "Wrong amount of primes were copied from rsa-challenge_solutions.txt"
            )
        for number in numbers:
            self.assertTrue(self.prime.miller_rabin(int(number)))

    def test_miller_rabin_512_bit(self):
        """Test Miller-Rabin with two consecutive 512 bit primes and with the 396
        composite numbers that are between them."""
        primes = self.file.open_file_space("two_512_bit_primes.txt", 2)
        # Make sure 2 primes were copied
        if len(primes) != 2:
            raise RuntimeError(
                "Wrong amount of primes were copied from two_512_bit_primes.txt"
            )
        # Change the primes from type string into type integer
        primes = [int(p) for p in primes]
        i = 0
        number = primes[0]
        while i < 2:
            prime = False
            if number == primes[i]:
                # if number is in the list, it is a prime
                prime = True
                i += 1
            self.assertEqual(prime, self.prime.miller_rabin(number))
            number += 1


class OpenFile:
    """Methods for opening files. These should probably be in a module,
    but Pytest does not find my modules and I don't know how to fix it."""

    def open_file_comma(self, file_name: str) -> list:
        """Read files of numbers and return them in a list. Works with files where
        the numbers are in one row and separated by a comma.

        Returns:
        A list of numbers. The numbers are in string format."""
        with open("src/tests/data/" + file_name) as file:
            for row in file:
                row = row.replace("\n", "")
                row = row.replace(" ", "")
                primes = row.split(",")
        return primes

    def open_file_space(self, file_name: str, rows: int) -> list:
        """Read files of numbers and return them in a list. Works
        with files where the numbers are separated by a space. The argument rows
        determines how many rows are read and saved from the file.

        Returns:
        A list of numbers. The numbers are in string format."""
        primes = ""
        with open("src/tests/data/" + file_name) as file:
            i = 0
            for row in file:
                row = row.replace("\n", "")
                primes = primes + row

                i += 1
                if i > rows - 1:
                    break

        primes = primes.split()
        return primes

    def open_file_rsa_challenge(self) -> list:
        """Open the file rsa-challenge.txt and return the numbers in it in a list.
        The file contains 45 large composite numbers from the RSA-challenge. The file
        is not in an easily readable format. The copied numbers are checked using a
        checksum that is provided in the file. Also the lengths of the numbers are
        checked.

        Returns:
        A list of integers."""
        numbers = []
        with open("src/tests/data/rsa-challenge.txt") as file:
            i = 0

            for row in file:
                # Rows must start 'RSA-' followed by 3-4 digits and ' ='
                regex = "^(RSA-[1-9]([0-9]{2}) =)"
                string = row[0:11]
                if re.search(regex, string):
                    number = ""
                    i = 10
                    # Copy the composite number digit by digit
                    for character in row[10:]:
                        if re.search("[0-9]", character):
                            number += character
                            i += 1
                        else:
                            break

                    # Find out the length in digits and the checksum. They are at the
                    # end of the row in the form of (617 digits, checksum = 909408).
                    # i points before them.
                    digits = ""
                    checksum = ""
                    row_end = row[i:]

                    # Find where the number digits begins
                    begin = row_end.find("(")
                    # Copy the number digit
                    for character in row_end[begin + 1 :]:
                        if re.search("[0-9]", character):
                            digits += character
                        else:
                            break

                    # Find where checksum begins
                    begin = row_end.find("checksum = ")
                    # Copy the number checksum
                    for character in row_end[begin + 11 :]:
                        if re.search("[0-9]", character):
                            checksum += character
                        else:
                            break

                    self.check_number(number, digits, checksum)
                    numbers.append(int(number))

        return numbers

    def check_number(self, number, digits, checksum):
        """Raise an error if open_file_rsa_challenge has made a mistake in copying
        a number"""
        try:
            int(number)
        except:
            raise ValueError("'number' was not an integer")
        try:
            digits = int(digits)
        except:
            raise ValueError("'digits' was not an integer")
        try:
            checksum = int(checksum)
        except:
            raise ValueError("'checksum' was not an integer")

        if not len(number) == digits:
            raise ValueError("Copied number had wrong amount of digits")
        if not int(number) % 991889 == checksum:
            raise ValueError("Copied number had an incorrect checksum")
