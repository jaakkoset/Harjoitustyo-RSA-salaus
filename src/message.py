class Message:
    """This class has methods to encrypt and decrypt messages"""

    def __init__(self):
        self.plain_text = None
        self.integer = None
        self.encrypted = None

    def encrypt(self, message, e, n):
        """Encrypts message using keys e and n."""
        self.plain_text = message
        message = self.text_to_integer(message)
        self.integer = message
        self.encrypted = pow(int(message), e, n)

    def decrypt(self, c, d, n):
        """Decrypts message c using keys d and n."""
        m = pow(c, d, n)
        return self.integer_to_text(m)

    def text_to_integer(self, text):
        """Turns text into an integer."""
        # Finds the ASCII-value for each character and concatenates the values.
        # If ASCII-value is less that 100, a 3 is added on the left side of the number
        # so that all characters get a value three digits long. Largest ASCII-value is
        # 255, so this creates no problems.
        integer = ""
        for character in text:
            a = ord(character)
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
