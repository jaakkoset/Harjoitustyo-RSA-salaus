import unittest
from message import Message
from create_key import CreateKey


class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.msg = Message()
        self.create = CreateKey()

    def test_encryption_1024_big(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is 128
        characters, which is the maximum for this key length."""
        text = self.open_file(128)
        self.encrypt_decrypt(1024, text)

    def test_encryption_1024_medium(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is 50
        characters."""
        text = "abcdefghijklmnopqrstuvwxyzåäö 012456789,.!%&/()=?"
        self.encrypt_decrypt(1024, text)

    def test_encryption_1024_quantum(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is
        1 character."""
        text = "a"
        self.encrypt_decrypt(1024, text)

    def test_encryption_2048(self):
        """Tests encryption with a 2048 bit key. The length of the encrypted text is the
        maximum for this key length, 256 characters."""
        text = self.open_file(256)
        self.encrypt_decrypt(2048, text)

    def encrypt_decrypt(self, bits: int, text: str):
        """Helper function. Encrypts the given text and then decrypts it. Then asserts
        that that the message has remained the same."""
        key = self.create.create_key(bits)
        integer = self.msg.text_to_integer(text)
        encrypted = self.msg.encrypt(integer, key["e"], key["n"])
        decrypted = self.msg.decrypt(encrypted, key["d"], key["n"])
        message = self.msg.integer_to_text(decrypted)

        self.assertEqual(message, text)

    def open_file(self, text_length: int):
        """Opens files text-128.txt and text-256.txt"""
        with open("src/tests/data/" + "text-" + str(text_length) + ".txt") as file:
            text = ""
            for row in file:
                text += row
        return text
