from random import randint

class Program:
    def __init__(self):
        self.prime_q = None
        self.prime_p = None
        self.program()

    def program(self):
        while True:
            print()
            print("Komennot")
            print(" 1 Luo uudet satunnaiset alkuluvut.")
            print(" 2 Katso alkuluvut.")
            print(" q Lopeta ohjelma.")

            cmd = input("Anna komento: ")
            if cmd == "q":
                break
            elif cmd == "1":
                self.prime_p = Prime().random_prime()
                self.prime_q = Prime().random_prime()
            elif cmd == "2":
                print()
                print("q: ", self.prime_q)
                print("p: ", self.prime_p)
                

    def create_key(self):
        pass

class Prime:
    def __init__(self):
        pass

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
                #print(nro, "on jaollinen luvulla", i)
                return False
            i += 1
        return True

    # returns the next prime beginning from p
    def next_prime(self, p:int):
        while True:
            if self.trial_division(p):
                return p
            p += 1

    # returns a random prime number between a and the first prime after b
    def random_prime(self, a=10**12, b=10**13):
        n = randint(a, b)
        prime = self.next_prime(n)
        return prime


Program()