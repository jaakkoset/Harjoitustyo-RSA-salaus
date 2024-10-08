import unittest
from src.message import Message
from src.prime import Prime
from src.key import Key
from secrets import randbits


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.msg = Message()
        self.prime = Prime()
        self.key = Key()

    def test_encrypt_decrypt_encrypt_1024(self):
        """Tests encryption with a 1024 bit key. The length of the encrypted text is the
        maximum for this key length, 103 characters."""
        self.encrypt_decrypt_encrypt(1024, 103)

    def test_encrypt_decrypt_encrypt_2048(self):
        """Tests encryption with a 2048 bit key. The length of the encrypted text is the
        maximum for this key length, 205 characters."""
        self.encrypt_decrypt_encrypt(2048, 205)

    def encrypt_decrypt_encrypt(self, bits: int, length: int):
        with open("src/tests/data/" + "text-" + str(length) + ".txt") as file:
            text = ""
            for row in file:
                text += row
        key = self.create_key(bits)
        integer = self.msg.text_to_integer(text)
        encrypted = self.msg.encrypt(integer, key["e"], key["n"])
        decrypted = self.msg.decrypt(encrypted, key["d"], key["n"])
        message = self.msg.integer_to_text(decrypted)

        self.assertEqual(text, message)

    def create_key(self, bits: int) -> dict:

        # 1. Choose two primes p and q
        p = self.prime.random_prime(bits)
        q = self.prime.random_prime(bits)
        # 2. Calculate n = pq
        n = p * q

        # 3. Calculate lambda(n) := ln using Charmichael function.
        # Since p and q are primes the problem reduces to ln = lcm(p-1, q-1),
        # where lcm means least common multiple.
        ln = self.key.lcm(p - 1, q - 1)

        # 4. Choose e that is coprime with ln.
        # We will use default value e = 65537
        e = 65537
        if ln % e == 0:
            # There is a very small chance that ln is divisble by e.
            raise RuntimeError("When creating keys, lambda(n) was divisible by e")

        # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
        d = self.key.multiplicative_inverse(e, ln)

        return {"p": p, "q": q, "n": n, "e": e, "ln": ln, "d": d}
