import unittest
import pytest
from message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()
        # All printable ascii characters with \ escaped
        self.ascii = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"""

    def test_encrypt(self):
        """Encrypt the integer 65 with given keys and assert that the encrypted
        integer is 2790."""
        # Example values from Wikipedia:
        # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
        example = {"plain_text": 65, "e": 17, "n": 3233, "cipher": 2790}
        x = self.msg.encrypt(example["plain_text"], example["e"], example["n"])
        self.assertEqual(x, example["cipher"])

    def test_decrypt(self):
        """Decrypt the integer 2790 with given keys and assert that the
        decrypted message is 65."""
        # Example values from Wikipedia:
        # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
        example = {"chiper": 2790, "d": 413, "n": 3233, "plain_text": 65}
        x = self.msg.decrypt(example["chiper"], example["d"], example["n"])
        self.assertEqual(x, example["plain_text"])

    def test_text_to_integer(self):
        """Test text to integer conversion with all ascii characters and ääkköset"""
        examples = [
            {"text": self.ascii, "answer": None},
            {"text": "åäöÅÄÖ", "answer": None},
            {"text": "\\", "answer": None},
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
        """Test integer to text conversion with all ascii characters and ääkköset"""
        examples = [
            {"integer": None, "answer": self.ascii},
            {"integer": None, "answer": "åäöÅÄÖ"},
            {"integer": None, "answer": "\\"},
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

    def test_text_integer_text(self):
        """Test both text_to_integer and integer_to_text by converting a text into an
        integer and back to text. Tested text is 1342 characters long."""
        with open("src/tests/data/" + "rsa-text.txt") as file:
            text = ""
            for row in file:
                text += row

        integer = self.msg.text_to_integer(text)
        new_text = self.msg.integer_to_text(integer)
        self.assertEqual(text, new_text)

    def test_text_integer_text_newlines(self):
        """Test both text_to_integer and integer_to_text by converting a text into an
        integer and back to text. Tested text has 1337 characters and 9 newlines."""
        with open("src/tests/data/" + "rsa-text_with_newlines.txt") as file:
            text = ""
            for row in file:
                text += row

        integer = self.msg.text_to_integer(text)
        new_text = self.msg.integer_to_text(integer)
        self.assertEqual(text, new_text)

    def test_text_to_integer_empty_string(self):
        "Test that text_to_integer raises an error when it is given an empty string"
        with pytest.raises(ValueError):
            self.msg.text_to_integer("")

    def test_text_to_integer_non_ascii(self):
        """Test that text_to_integer raises an error with characrters that have an
        Unicode code point value more than 255."""
        for i in range(256, 266):
            with pytest.raises(ValueError):
                character = chr(i)
                self.msg.text_to_integer(character)

    def test_integer_to_text_digits_error(self):
        """Test that integer_to_text raises an error when the hexadecimal representation
        of the argument integer has an odd amount of digits."""
        arguments = ["F", "111", "ABC", "89ABC"]
        for arg in arguments:
            with pytest.raises(ValueError):
                integer = int(arg, 16)
                self.msg.integer_to_text(integer)
