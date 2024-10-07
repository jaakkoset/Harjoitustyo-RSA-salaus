class Message:
    """This class has methods to encrypt and decrypt messages"""

    def encrypt(self, message: int, e: int, n: int):
        """Encrypts a message using keys e and n."""
        return pow(message, e, n)

    def decrypt(self, cipher: int, d: int, n: int):
        """Decrypts a ciphered message using keys d and n."""
        return pow(cipher, d, n)

    def text_to_integer(self, text):
        """Turns text into an integer."""
        # Finds the ASCII-value for each character and concatenates the values.
        # If ASCII-value is less that 100, a 3 is added on the left side of the number
        # so that all characters get a value three digits long. Largest ASCII-value is
        # 255, so this creates no problems.
        integer = ""
        for character in text:
            a = ord(character)
            if a > 255:
                raise ValueError(f"A non-ASCII character used: {character}")
            if a < 100:
                a = "3" + str(a)
            integer = integer + str(a)
        return int(integer)

    def integer_to_text(self, integer):
        """Turns integers back to text."""
        text = ""
        integer = str(integer)
        for i in range(0, len(integer) - 2, 3):
            ascii = ""
            if int(integer[i]) != 3:
                ascii = ascii + integer[i]
            ascii = ascii + integer[i + 1] + integer[i + 2]
            text = text + chr(int(ascii))
        return text
