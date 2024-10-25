from message import Message
from create_key import CreateKey


class Program:
    def __init__(self):
        self.encryption = Message()
        self.create = CreateKey()

        # n and e are the public keys and d is the secret key.
        # p, q and ln are used to create the keys and are unneeded afterwards.
        self.keys = {"p": None, "q": None, "n": None, "e": None, "ln": None, "d": None}

        self.message = {"text": None, "integer": None, "cipher": None}
        # Maximum length for messages
        self.max_len = 0

        # self.program()

    def program(self):
        while True:
            print()
            print("Komennot")
            print(" 1 Luo satunnainen salausavain.")
            print(" 2 Luo oma salausavain.")
            print(" 3 Tulosta salausavaimen osat.")
            print(" 4 Salaa viesti.")
            print(" 5 Pura viestin salaus.")
            print(" 6 Tulosta viestit.")
            print(" q Lopeta ohjelma.")

            cmd = input("Anna komento: ")

            if cmd == "1":
                self.cmd1_random_key()

            elif cmd == "2":
                self.cmd2_own_key()

            elif cmd == "3":
                self.cmd3_print_keys()

            elif cmd == "4":
                self.cmd4_encrypt()

            elif cmd == "5":
                self.cmd5_decrypt()

            elif cmd == "6":
                self.cmd6_print_messages()

            elif cmd == "q":
                break

    def cmd1_random_key(self):
        self.keys = self.create.create_key(1024)
        self.set_max_len()

    def cmd2_own_key(self):
        print("Anna 1. alkuluku: ")
        p = input()
        print("Anna 2. alkuluku: ")
        q = input()
        print("Anna eksponentti e tai käytä oletusarvoa 65537 painamalla enter:")
        e = input()
        print()
        x = self.create.create_own_key(p, q, e)
        if not x:
            print("Avaimen luonti epäonnistui")
        else:
            self.keys = x
            self.set_max_len()
            print("Avain luotu.")

    def cmd3_print_keys(self):
        print()
        if not self.keys["d"]:
            print("Avainta ei ole määritelty")
        else:
            for key in ["d", "n", "e", "p", "q", "ln"]:
                print(
                    f"{key}  Pituus: desimaalina {len(str(self.keys[key]))} / "
                    f"bitteinä {len(str(bin(self.keys[key]))) - 2}"
                )
                print(self.keys[key])
                print()

            print("Viestin suurin sallittu pituus:")
            print(self.max_len)

    def cmd4_encrypt(self):
        if not self.no_key():
            message, integer, cipher = self.encrypter()
            print()
            if not message:
                print("Viestin salaus epäonnistui")
            else:
                self.message["text"] = message
                self.message["integer"] = integer
                self.message["cipher"] = cipher
                print("Viesti salattuna")
                print(self.message["cipher"])

    def encrypter(self):
        """
        Asks the user to type in a message, then turns the message into
        an integer and encrypts the integer. Returns the message, integer
        and cipher in a tuple. Gives values None to all of these, if
        encryption fails.

        Returns:
        A tuple (message, integer, cipher) when encryption is successful,
        and a tuple (None, None, None) if encryption fails.
        """
        check = True
        print("Kirjoita salattava viesti")
        message = input()
        if message == "":
            print("Viesti ei voi olla tyhjä merkkijono")
            check = False
        if len(message) > self.max_len:
            print(
                f"\nViesti on liian pitkä. Pituus on {len(message)}.",
                f"\nSuurin sallittu pituus on: ",
                f"\n(avaimen n pituus bitteinä) // 8 = {self.max_len}",
            )
            check = False
        if check:
            integer = self.encryption.text_to_integer(message)

        if check:
            cipher = self.encryption.encrypt(integer, self.keys["e"], self.keys["n"])
            return message, integer, cipher

        return None, None, None

    def cmd5_decrypt(self):
        message = None
        if not self.no_key():
            message = self.decrypter()
        if message:
            print("Purettu viesti")
            print(message)

    def decrypter(self):
        """Decrypts an encrypted integer and turns it into text. Returns
        the resulting text or None if decryption fails."""
        print("Anna purettava viesti")
        cipher = input()
        print()
        check = True
        try:
            cipher = int(cipher)
        except:
            print("Purettavan viestin täytyy olla kokonaisluku.")
            check = False

        if check:
            message = self.encryption.decrypt(cipher, self.keys["d"], self.keys["n"])
            message = self.encryption.integer_to_text(message)
            return message
        return None

    def cmd6_print_messages(self):
        print()
        if not self.message["text"]:
            print("Viestiä ei ole luotu")
        else:
            print("Teksti")
            print(self.message["text"])
            print()
            print("Salaamaton kokonaisluku")
            print(self.message["integer"])
            print()
            print("Salattu kokonaisluku")
            print(self.message["cipher"])

    def no_key(self) -> bool:
        """Checks that no keys exist."""
        if not self.keys["p"]:
            print()
            print("Avainta ei ole luotu.")
            return True
        return False

    def set_max_len(self):
        """Sets the maximum possible message length with the current key. Maximum
        message length is the lenght of the key n in bits divided by 8."""
        binary = bin(self.keys["n"])
        length = len(str(binary))
        # Binary representation has 0b written in the beginning. That is why
        # we must subtract 2 from the length.
        self.max_len = (length - 2) // 8


if __name__ == "__main__":
    Program().program()
