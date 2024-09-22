from random import randint
import time

class Program:
    def __init__(self):
        self.key = Key()
        self.message = Message()
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
            if cmd == "q":
                break

            elif cmd == "1":
                self.key.create_key()
            
            elif cmd == "2":
                p = int(input("1. alkuluku: "))
                q = int(input("2. alkuluku: "))
                print("Luo e satunnaisesti painamalla enter. Muuten kirjoita luku.")
                e = input("e: ")
                if e == "":
                    self.key.create_key(p,q)
                else:
                    e = int(e)
                    self.key.create_key(p,q,e)

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
                print(self.message.encrypted)

            elif cmd == "5":
                if self.no_key():
                    continue
                print("Anna purettava viesti")
                c = input()
                m = self.message.decrypt(int(c), self.key.d, self.key.n)
                print()
                print("Purettu viesti")
                print(m)

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

    def print_key_info(self):
        print()
        print("d: ", self.key.d)
        print("n: ", self.key.n)
        print("e: ", self.key.e)
        print("p: ", self.key.p)
        print("q: ", self.key.q)
        print("ln:", self.key.ln)

    # Checks if no key exists.
    def no_key(self) -> bool:
        if not self.key.d:
            print()
            print("Avainta ei ole luotu.")
            return True
        return False


class Message:
    def __init__(self):
        self.plain_text = None
        self.integer = None
        self.encrypted = None

    def encrypt(self, message, e, n):
        #print("e:", e, " n:", n)
        self.plain_text = message
        message = self.text_to_integer(message)
        self.integer = message
        self.encrypted = pow(int(message), e, n)
        #return self.encrypted

    def decrypt(self, c, d, n):
        #print("d:", d, " n:", n)
        m = pow(c, d, n)
        #print("m:", m)
        #return m
        return self.integer_to_text(m)

    # Turns text into an integer.
    # Finds the ASCII-value for each character and concatenates them.
    # If ASCII-value is less that 100, a 3 is added on the left side of the number
    # so that all characters get a value three digits long. Largest ASCII-value is
    # 255, so this creates no problems.
    def text_to_integer(self, text):
        #integer = "1" V2
        integer = ""
        for character in text:
            a = ord(character)
            if a < 100:
                #a = "0" + str(a) V2
                a = "3" + str(a)
            integer = integer + str(a)
        return int(integer)
    
    # Turns integers back to text.
    def integer_to_text(self, integer):
        text = ""
        integer = str(integer)
        #for i in range(1, len(integer) - 1 , 3): V2
        for i in range(0, len(integer) - 2 , 3):
            ascii = ""
            if int(integer[i]) != 3:
                ascii = ascii + integer[i]
            ascii = ascii + integer[i+1] + integer[i+2]
            #print("ascii:",ascii)
            text = text + chr(int(ascii))
        return text


class Key:
    def __init__(self):
        # d is the secret key
        self.d = None
        # n and e are the public keys
        self.n = None
        self.e = None
        # p, q and ln are used to create the keys
        self.p = None
        self.q = None
        self.ln = None

    def create_key(self, p=None, q=None, e=None):

        print() # CLOCKING
        start = time.time() # CLOCKING

        # 1. Choose two primes p and q
        if not p:
            self.p = Prime().random_prime()
            self.q = Prime().random_prime()
        else:
            self.p = p
            self.q = q

        # 2. Calculate n = pq
        self.n = self.p * self.q

        end = time.time() # CLOCKING
        self.print_clock(start, end, "1-2") # CLOCKING
        start = time.time() # CLOCKING

        # 3. Calculate lambda(n) := ln using Charmichael function.
        # Since p and q are primes the problem reduces to ln = lcm(p-1, q-1),
        # where lcm means least common multiple.
        self.ln = self.lcm(self.p - 1, self.q - 1)

        end = time.time() # CLOCKING
        self.print_clock(start, end, 3) # CLOCKING
        start = time.time() # CLOCKING

        # 4. Choose e that is coprime with ln
        if not e:
            self.e = self.choose_e(self.ln)
        else:
            self.e = e

        end = time.time() # CLOCKING
        self.print_clock(start, end, 4) # CLOCKING
        start = time.time() # CLOCKING

        # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
        self.d = self.determine_d(self.e, self.ln)

        end = time.time() # CLOCKING
        self.print_clock(start, end, 5) # CLOCKING

    def print_clock(self, start, end, step):
        print("Vaihe", str(step))
        print(round(end - start, 5))

    # lcm(a, b) = abs(ab) / gcd(a,b)
    # gcd means greatest common divisor and can be calculated with the euclidean algorithm
    def lcm(self, a, b):
        gcd = self.euclidean_algorithm(a,b)
        absolute = abs(a * b)
        ln = absolute // gcd
        return ln

    # Euclidean algorithm solves the greatest common divisor gcd
    def euclidean_algorithm(self, a,b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return a
        
    # choose e that is coprime with ln. 
    # This is assured when e is prime and it does not divide ln.
    def choose_e(self, ln):
        while True:
            e = Prime().random_prime(2, ln)
            if self.ln % e != 0:
                self.e = e
                break
        return e

    def determine_d(self, e, ln):
        d = self.multiplicative_inverse(e, ln)
        return d

    # This is a reduced version of the extended euclidian algorithm.
    # It is based on the fact that e and ln are coprime (here a and b).
    def multiplicative_inverse(self, a, b):
        t = 0;     
        newt = 1
        r = b
        newr = a

        while newr != 0:
            quotient = r // newr

            var = t
            t = newt
            newt = var - quotient * newt

            var = r
            r = newr 
            newr = var - quotient * newr

        if r > 1:
            print("a ei ole kääntyvä")
        if t < 0:
            t = t + b

        return t

    # Can be used for testing.
    # Function multiplicative_inverse can be used instead of this.
    def extended_euclidian_algorithm(self, a, b):
        # remainder = r
        old_r, r = a, b
        # s and r will be the Bezout's coefficients
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            # quotient = q
            q = old_r // r
            
            # calculate the remainder of old_r / r
            var = r
            r = old_r - q * var
            old_r = var

            # calculate the Bezout's coefficients.
            # At the end of the algorithm Bezout's coefficients are old_s and old_t
            # and quotients by the gcd are t and s (which are useless for our purposes).
            var = s
            s = old_s - q * s
            old_s = var

            var = t
            t = old_t - q * t
            old_t = var
        
        return {"Bezout coefficients": (old_s, old_t), "greatest common divisor": (old_r), "quotients by the gcd": (t, s)}


class Prime:
    # Used for testing
    first_58_primes = [
            2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
            61,67,71,73,79,83,89,97,101,103,107,109,113,127,
            131,137,139,149,151,157,163,167,173,179,181,191,
            193,197,199,211,223,227,229,233,239,241,251,257,
            263,269,271,] 

    # This is the simplest algorithm to test whether a given number is prime.
    # It is inefficient with large numbers.
    def trial_division(self, nro: int) -> bool: 
        i = 2
        while i*i <= nro:
            if nro % i == 0:
                return False
            i += 1
        return True

    # returns a random prime number between a and b
    def random_prime(self, a=10**6, b=10**7):
        while True:
            n = randint(a, b)
            if self.trial_division(n):
                return n
    

Program()