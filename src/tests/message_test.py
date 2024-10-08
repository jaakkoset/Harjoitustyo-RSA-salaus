import unittest
from message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()

    def test_encrypt(self):
        # Example values from Wikipedia:
        # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
        example = {"plain_text": 65, "e": 17, "n": 3233, "cipher": 2790}
        x = self.msg.encrypt(example["plain_text"], example["e"], example["n"])
        self.assertEqual(x, example["cipher"])

    def test_decrypt(self):
        # Example values from Wikipedia:
        # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
        example = {"chiper": 2790, "d": 413, "n": 3233, "plain_text": 65}
        x = self.msg.decrypt(example["chiper"], example["d"], example["n"])
        self.assertEqual(x, example["plain_text"])

    def test_text_to_integer(self):
        examples = [
            {"text": "abcxyzåäö", "answer": 397398399120121122229228246},
            {"text": "AÖ", "answer": 365214},
            {"text": '19.!"()', "answer": 349357346333334340341},
        ]
        for e in examples:
            x = self.msg.text_to_integer(e["text"])
            self.assertEqual(x, e["answer"])

    def test_integer_to_text(self):
        examples = [
            {"integer": 397398399120121122229228246, "answer": "abcxyzåäö"},
            {"integer": 365214, "answer": "AÖ"},
            {"integer": 349357346333334340341, "answer": '19.!"()'},
            {"integer": 365214, "answer": "AÖ"},
        ]
        for e in examples:
            x = self.msg.integer_to_text(e["integer"])
            self.assertEqual(x, e["answer"])

    def test_text_to_integer_to_text(self):
        """Tests both text_to_integer and integer_to_text by converting a text into an
        integer and back to text. Tested text is 1337 characters long."""
        with open("src/tests/data/" + "rsa-text.txt") as file:
            text = ""
            for row in file:
                text += row

        integer = self.msg.text_to_integer(text)
        new_text = self.msg.integer_to_text(integer)
        self.assertEqual(text, new_text)
