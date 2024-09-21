from random import randint
import time

class Program:
    def __init__(self):
        self.key = Key()
        self.program()

    def program(self):
        while True:
            print()
            print("Komennot")
            print(" 1 Luo satunnainen salausavain.")
            print(" 2 Luo oma salausavain.")
            print(" 3 Tulosta salausavaimen osat.")
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

    def print_key_info(self):
        print()
        print("d: ", self.key.secret_key_d)
        print("n: ", self.key.public_key_n)
        print("e: ", self.key.public_key_e)
        print("p: ", self.key.prime_p)
        print("q: ", self.key.prime_q)
        print("ln:", self.key.ln)
                        
class Key:
    def __init__(self):
        self.secret_key_d = None
        self.public_key_n = None
        self.public_key_e = None
        self.prime_p = None
        self.prime_q = None
        self.ln = None

    def create_key(self, p=None, q=None, e=None):

        start = time.time() # CLOCKING

        # 1. Choose two primes p and q
        if not p:
            self.prime_p = Prime().random_prime()
            self.prime_q = Prime().random_prime()
        else:
            self.prime_p = p
            self.prime_q = q

        # 2. Calculate n = pq
        self.public_key_n = self.prime_p * self.prime_q

        end = time.time() # CLOCKING
        print("Vaiheet 1 ja 2") # CLOCKING
        print(round(end - start, 10)) # CLOCKING
        start = time.time() # CLOCKING

        # 3. Calculate lambda(n) := ln using Charmichael function.
        # Since p and q are primes the problem reduces to ln = lcm(p-1, q-1),
        # where lcm means least common multiple.
        self.ln = self.lcm(self.prime_p - 1, self.prime_q - 1)

        end = time.time() # CLOCKING
        print("Vaihe 3") # CLOCKING
        print(round(end - start, 10)) # CLOCKING
        start = time.time() # CLOCKING

        # 4. Choose e that is coprime with ln
        if not e:
            self.public_key_e = self.choose_e(self.ln)
        else:
            self.public_key_e = e

        end = time.time() # CLOCKING
        print("Vaihe 4") # CLOCKING
        print(round(end - start, 10)) # CLOCKING

        start = time.time() # CLOCKING

        # 5. determine d, the modular multiplicative inverse of e mod lambda(n)
        self.secret_key_d = self.determine_d(self.public_key_e, self.ln)

        end = time.time() # CLOCKING
        print("Vaihe 5") # CLOCKING
        print(round(end - start, 10)) # CLOCKING

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
                self.public_key_e = e
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