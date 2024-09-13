from random import randint

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
                self.key_components = self.key.create_key()
            
            elif cmd == "2":
                p = int(input("1. alkuluku: "))
                q = int(input("2. alkuluku: "))
                print("Jos et anna e:tä paina enter. Muuten kirjoita luku.")
                e = input("e: ")
                if e == "":
                    self.key_components = self.key.create_key(p,q)
                else:
                    e = int(e)
                    self.key_components = self.key.create_key(p,q,e)

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
        # 1. Choose two primes p and q
        if not p:
            self.choose_primes()
        else:
            self.prime_p = p
            self.prime_q = q
        # 2. Calculate n = pq
        self.public_key_n = self.prime_p * self.prime_q
        # 3. Calculate lambda(n) = ln using Charmichael function
        self.carmichael_function()
        # 4. Choose e that is coprime with ln
        if not e:
            self.choose_e()
        else:
            self.public_key_e = e

    def choose_primes(self):
        self.prime_p = Prime().random_prime()
        self.prime_q = Prime().random_prime()
    
    # Carmichael function calculates lambda(n) = lcm(p-1, q-1)
    # lcm(a, b) = abs(ab) / gcd(a,b)
    def carmichael_function(self):
        gcd = self.euclidean_algorithm()
        absolute = abs((self.prime_p - 1) * (self.prime_q - 1))
        self.ln = absolute // gcd

    # Euclidean algorithm solves the greatest common divisor gcd
    def euclidean_algorithm(self):
        a = self.prime_p - 1
        b = self.prime_q - 1
        while True:
            if a > b:
                a = a % b
            else:
                b = b % a
            if a == 0:
                return b
            if b == 0:
                return a
    
    # e is coprime with ln if e is prime and it does not divide ln
    def choose_e(self):
        while True:
            e = Prime().random_prime(1, self.ln)
            if self.ln % e != 0:
                self.public_key_e = e
                break

class Prime:
    # Used for testing
    first_58_primes = [
            2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,
            61,67,71,73,79,83,89,97,101,103,107,109,113,127,
            131,137,139,149,151,157,163,167,173,179,181,191,
            193,197,199,211,223,227,229,233,239,241,251,257,
            263,269,271,] 

    # tests whether a given number is prime
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