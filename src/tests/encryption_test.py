import unittest
from src.message import Message
from src.key import Key
from secrets import randbits


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()
        self.key = Key()

    def test_encrypt_decrypt_encrypt_1024(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is the
        maximum for this key length, 103 characters."""
        self.encrypt_decrypt_encrypt(1024, 103)

    # Testing the 2048 bit key takes 10 to 40 seconds.
    # def test_encrypt_decrypt_encrypt_2048(self):
    #     """Tests encryption with a 2048 bit key. The length of the encrypted text is the
    #     maximum for this key length, 205 characters."""
    #     self.encrypt_decrypt_encrypt(2048, 205)

    def encrypt_decrypt_encrypt(self, bits: int, length: int):
        with open("src/tests/data/" + "text-" + str(length) + ".txt") as file:
            text = ""
            for row in file:
                text += row
        key = self.key.create_key(bits)
        integer = self.msg.text_to_integer(text)
        encrypted = self.msg.encrypt(integer, key["e"], key["n"])
        decrypted = self.msg.decrypt(encrypted, key["d"], key["n"])
        message = self.msg.integer_to_text(decrypted)

        self.assertEqual(text, message)
