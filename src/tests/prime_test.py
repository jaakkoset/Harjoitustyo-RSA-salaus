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
