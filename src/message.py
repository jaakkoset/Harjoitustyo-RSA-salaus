class Message:
    """This class has methods to encrypt and decrypt messages and to turn text into
    integers and back to text."""

    def encrypt(self, message: int, e: int, n: int):
        """Encrypts a message using keys e and n."""
        return pow(message, e, n)

    def decrypt(self, cipher: int, d: int, n: int):
        """Decrypts a ciphered message using keys d and n."""
        return pow(cipher, d, n)

    def text_to_integer(self, text: str):
        """Turns text into an integer using Unicode code points up to the value
        of 255. This includes all extended ASCII characters."""
        if text == "":
            raise ValueError("An empty string cannot be turned into an integer")
        hexadecimal = "0x"
        for character in text:
            # Find the Unicode code point
            value = ord(character)
            if value > 255:
                raise ValueError(
                    f"A non ASCII character found: {character} (value {value})"
                )
            # turn the value into a hexadecimal
            value = hex(value)
            # remove the 0x in the beginning of the hexadecimal
            value = str(value)[2:]
            # hexadecimals must have two digits
            if len(value) < 2:
                value = "0" + value
            if len(value) > 2:
                print("hexadecimal value:")
                print(value)
                raise ValueError(f"Too large hexadecimal value: {value}")

            hexadecimal += value

        # turn the hexadecimal into a decimal integer
        integer = int(hexadecimal, 16)
        return integer

    def integer_to_text(self, integer: int):
        """Turns integers back to text."""
        hexadecimal = hex(integer)
        # remove the 0x in the beginning of the hexadecimal
        hexadecimal = str(hexadecimal)[2:]
        text = ""
        # One character has a Unicode code point of two hexadecimal digits, so we
        # look two digits at a time.
        for i in range(0, len(hexadecimal), 2):
            if i + 1 > len(hexadecimal) - 1:
                raise ValueError(
                    f"Index error in integer_to_text. i: {i}",
                    f"len(hexadecimal): {len(hexadecimal)}",
                )
            value = hexadecimal[i] + hexadecimal[i + 1]
            # turn the hexadecimal into a decimal
            value = int(value, 16)
            if value > 255:
                raise ValueError(
                    f"A non ASCII character found: {chr(value)} (value {value})"
                )
            character = chr(value)
            text += character

        return text
