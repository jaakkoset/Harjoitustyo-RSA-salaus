from key import Key
from prime import Prime
from message import Message
from random import randint
import time


class Program:
    def __init__(self):
        self.key = Key()
        self.message = Message()

        # n and e are the public keys and d is the secret key.
        # p, q and ln are used to create the keys and are unneeded afterwards.
        self.keys = {"p": None, "q": None, "n": None, "e": None, "ln": None, "d": None}

        self.message = {"text": None, "integer": None, "encrypted": None}

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
                self.keys = self.key.create_key(1024)

            elif cmd == "2":
                p = int(input("1. alkuluku: "))
                q = int(input("2. alkuluku: "))
                print("Luo e satunnaisesti painamalla enter. Muuten kirjoita luku.")
                e = input("e: ")

            elif cmd == "3":
                self.print_key_info()

            elif cmd == "4":
                if self.no_key():
                    continue
                print("Kirjoita salattava viesti")
                m = str(input())
                self.message.encrypt(m, self.key.e, self.key.n)
                print()
                print("Viesti salattuna")
                print(self.message["encrypted"])

            elif cmd == "5":
                if self.no_key():
                    continue
                print("Anna purettava viesti")
                c = input()
                print()
                try:
                    c = int(c)
                    m = self.message.decrypt(c, self.key.d, self.key.n)
                    print("Purettu viesti")
                    print(m)
                except:
                    print("Salatut viestit ovat kokonaislukuja.")

            elif cmd == "6":
                print()
                print("Teksti")
                print(self.message.plain_text)
                print()
                print("Salaamaton kokonaisluku")
                print(self.message.integer)
                print()
                print("Salattu kokonaisluku")
                print(self.message.encrypted)

            elif cmd == "q":
                break

    def print_key_info(self):
        print()
        print("d.  Pituus ", len(str(self.key.d)))
        print(self.key.d)
        print("n.  Pituus ", len(str(self.key.n)))
        print(self.key.n)
        print("e.  Pituus ", len(str(self.key.e)))
        print(self.key.e)
        print("p.  Pituus ", len(str(self.key.p)))
        print(self.key.p)
        print("q.  Pituus ", len(str(self.key.q)))
        print(self.key.q)
        print("ln. Pituus", len(str(self.key.ln)))
        print(self.key.ln)

    def no_key(self) -> bool:
        """Checks that no keys exist."""
        if not self.key.d:
            print()
            print("Avainta ei ole luotu.")
            return True
        return False


if __name__ == "__main__":
    Program()
