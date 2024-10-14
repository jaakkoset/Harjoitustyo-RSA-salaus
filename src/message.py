import base64


class Message:
    """This class has methods to encrypt and decrypt messages"""

    def encrypt(self, message: int, e: int, n: int):
        """Encrypts a message using keys e and n."""
        return pow(message, e, n)

    def decrypt(self, cipher: int, d: int, n: int):
        """Decrypts a ciphered message using keys d and n."""
        return pow(cipher, d, n)

    def text_to_integer(self, text: str):
        """Turns text into an integer using UTF-8 encoding.
        UTF-8 is roughly speaking the same as extended ASCII"""
        # Turn the text into a bytes-like object and define the encoding as UTF-8.
        text = bytes(text, "utf-8")
        # Give each character its hexadecimal UTF-8 value and concatenate them into one
        # integer.
        base16_text = base64.b16encode(text)
        # Turn the hexadecimal integer into a decimal number
        base16_text = int(base16_text, 16)
        return base16_text

    def integer_to_text(self, integer: int):
        """Turns integers back to text."""
        # Turn the integer into a hexadecimal
        base16 = hex(integer)
        # Turn it into a string
        base16 = str(base16)
        # Hexadecimals have 0x in the beginning, so we remove that.
        base16 = base16[2:]
        # Decode the hexadecimal into UTF-8 characters. This returns a byte-like
        # object.
        text = base64.b16decode(base16, casefold=True)
        # Turn the answer into string
        text = str(text, "utf-8")
        return text
