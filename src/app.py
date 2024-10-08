from key import Key
from prime import Prime
from message import Message
from generator import Generator


class Program:
    def __init__(self):
        # self.key = Key()
        self.encryption = Message()
        # self.prime = Prime()
        self.generator = Generator()

        # n and e are the public keys and d is the secret key.
        # p, q and ln are used to create the keys and are unneeded afterwards.
        self.keys = {"p": None, "q": None, "n": None, "e": None, "ln": None, "d": None}

        self.message = {"text": None, "integer": None, "encrypted": None}
        # Maximum length for messages
        self.max_len = 0

        self.program()

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
                self.cmd3_key_info()

            elif cmd == "4":
                if self.no_key():
                    continue
                self.cmd4_encrypt()

            elif cmd == "5":
                if self.no_key():
                    continue
                self.cmd5_decrypt()

            elif cmd == "6":
                self.cmd6_messages()

            elif cmd == "q":
                break

    def cmd1_random_key(self):
        self.keys = self.generator.create_key(1024)
        self.set_max_len()

    def cmd2_own_key(self):
        print("Anna 1. alkuluku: ")
        p = input()
        print("Anna 2. alkuluku: ")
        q = input()
        print("Anna eksponentti e tai käytä oletusarvoa 65537 painamalla enter:")
        e = input()
        print()
        x = self.generator.create_own_key(p, q, e)
        if not x:
            print("Avaimen luonti epäonnistui")
        else:
            self.keys = x
            self.set_max_len()
            print("Avain luotu.")

    def cmd3_key_info(self):
        print()
        if not self.keys["d"]:
            print("Avainta ei ole määritelty")
        else:
            print("d.  Pituus ", len(str(self.keys["d"])))
            print(self.keys["d"])
            print("n.  Pituus ", len(str(self.keys["n"])))
            print(self.keys["n"])
            print("e.  Pituus ", len(str(self.keys["e"])))
            print(self.keys["e"])
            print("p.  Pituus ", len(str(self.keys["p"])))
            print(self.keys["p"])
            print("q.  Pituus ", len(str(self.keys["q"])))
            print(self.keys["q"])
            print("ln. Pituus ", len(str(self.keys["ln"])))
            print(self.keys["ln"])

    def cmd4_encrypt(self):
        print("Kirjoita salattava viesti")
        check = True
        message = str(input())
        integer = self.encryption.text_to_integer(message)
        if integer // 3 < self.max_len:
            print(
                f"Viesti on liian pitkä \nPituus on {len(str(integer))}",
                f"\nSuurin sallittu pituus on {self.max_len}",
            )
            check = False
        if check:
            encrypted = self.encryption.encrypt(integer, self.keys["e"], self.keys["n"])
            self.message["text"] = message
            self.message["integer"] = integer
            self.message["encrypted"] = encrypted
            print()
            print("Viesti salattuna")
            print(self.message["encrypted"])
        else:
            print("Viestin salaus epäonnistui")

    def cmd5_decrypt(self):
        print("Anna purettava viesti")
        cipher = input()
        print()
        check = True
        try:
            cipher = int(cipher)
        except:
            print("Salatut viestit ovat kokonaislukuja.")
            check = False

        if check:
            message = self.encryption.decrypt(cipher, self.keys["d"], self.keys["n"])
            message = self.encryption.integer_to_text(message)
            print("Purettu viesti")
            print(message)

    def cmd6_messages(self):
        print()
        if not self.message["text"]:
            print("Viestiä ei ole määritelty")
        else:
            print("Teksti")
            print(self.message["text"])
            print()
            print("Salaamaton kokonaisluku")
            print(self.message["integer"])
            print()
            print("Salattu kokonaisluku")
            print(self.message["encrypted"])

    def no_key(self) -> bool:
        """Checks that no keys exist."""
        if not self.keys["p"]:
            print()
            print("Avainta ei ole luotu.")
            return True
        return False

    def set_max_len(self):
        self.max_len = len(str(self.keys["n"])) // 3


if __name__ == "__main__":
    Program()
