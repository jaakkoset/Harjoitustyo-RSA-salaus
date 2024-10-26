import unittest
from create_key import CreateKey


class TestCreateKey(unittest.TestCase):
    def setUp(self):
        self.create = CreateKey()

    def test_create_own_key(self):
        """Test creating own key with example values."""
        example = {"p": 61, "q": 53, "n": 3233, "e": 17, "ln": 780, "d": 413}
        key = self.create.create_own_key(61, 53, 17)
        for k in example:
            self.assertEqual(example[k], key[k])
