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
            {"text": "abyzABYZ", "answer": None},
            {"text": "åäö", "answer": None},
            {"text": "ÅÄÖ", "answer": None},
            {"text": '019.!"() -', "answer": None},
            {"text": "a", "answer": None},
        ]
        # Create answers
        for e in examples:
            # First create the hexadecimal representation of the text
            hexadecimal = "0x"
            for character in e["text"]:
                hexadecimal += str(hex(ord(character)))[2:]
            # Turn the hexadecimal into a decimal integer
            answer = int(hexadecimal, 16)
            e["answer"] = answer

        for e in examples:
            x = self.msg.text_to_integer(e["text"])
            self.assertEqual(x, e["answer"])

    def test_integer_to_text(self):
        examples = [
            {"integer": None, "answer": "abyzABYZ"},
            {"integer": None, "answer": "åäö"},
            {"integer": None, "answer": "ÅÄÖ"},
            {"integer": None, "answer": '019.!"() -'},
            {"integer": None, "answer": "a"},
        ]
        # Create integers
        for e in examples:
            # First create the hexadecimal representation of the text
            hexadecimal = "0x"
            for character in e["answer"]:
                hexadecimal += str(hex(ord(character)))[2:]
            # Turn the hexadecimal into a decimal integer
            integer = int(hexadecimal, 16)
            e["integer"] = integer

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
