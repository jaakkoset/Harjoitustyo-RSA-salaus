import unittest
from message import Message
from generator import Generator


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()
        self.generator = Generator()

    def test_encryption_1024_big(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is 101
        characters. 1024 bit key should be able to encrypt 102 or 103 characters, but
        for some reason these tests now fail."""
        text = self.open_file(103)
        self.encrypt_decrypt_encrypt(1024, text)

    def test_encryption_1024_medium(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is 50
        characters."""
        text = "abcdefghijklmnopqrstuvwxyzåäö 012456789,.!%&/()=?"
        self.encrypt_decrypt_encrypt(1024, text)

    def test_encryption_1024_quantum(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is
        1 character."""
        text = "a"
        self.encrypt_decrypt_encrypt(1024, text)

    # # Testing the 2048 bit key takes between 1 to 20 seconds.
    # def test_encrypt_decrypt_encrypt_2048(self):
    #     """Tests encryption with a 2048 bit key. The length of the encrypted text is the
    #     maximum for this key length, 204 characters."""
    #     self.encrypt_decrypt_encrypt(2048, 205)

    def encrypt_decrypt_encrypt(self, bits: int, text: str):
        key = self.generator.create_key(bits)
        # if len(str(key["n"])) < 309:
        #    raise ValueError("less than 309 digits in n:", len(str(key["n"])))
        integer = self.msg.text_to_integer(text)
        encrypted = self.msg.encrypt(integer, key["e"], key["n"])
        decrypted = self.msg.decrypt(encrypted, key["d"], key["n"])
        message = self.msg.integer_to_text(decrypted)

        self.assertEqual(text, message)

    def open_file(self, text_length: int):
        with open("src/tests/data/" + "text-" + str(text_length) + ".txt") as file:
            text = ""
            for row in file:
                text += row
        return text
