#!/usr/bin/env python
import random

class DH(object):
    def __init__(self, name, prime, base):
        self.name = name
        self.__privateKey = largeRandomNumber()
        self.publicKey = pow(base, self.__privateKey, prime)
    def sharedKey(self, publicKey, prime):
        sharedKey = pow(publicKey, self.__privateKey, prime)
        print "Secret key computed by " + str(self.name) + ":\t" + str(sharedKey)
        return sharedKey
    def printDetails(self):
        print str(self.name) + "'s private key:\t" + str(self.__privateKey)
        print str(self.name) + "'s public key:\t" + str(self.publicKey)
        
def largePrimeNumber():
    primeFound = False
    while primeFound == False:
        n = random.randint(100000000, 1000000000)
        if n % 2 != 0:
            for x in range(3, int(n**0.5), 2):
                if n % x ==0:
                    break
        else:
            primeFound = True
    return n
        
def largeRandomNumber():
    return random.randint(100000000, 1000000000)

def main():
    prime = largePrimeNumber()
    rootModulo = 3

    print "Generated shared prime number: " + str(prime)
    print "Primitive root modulo: " + str(rootModulo)

    alice = DH(name="Alice", prime=prime, base=rootModulo)
    bob = DH(name="Bob", prime=prime, base=rootModulo)

    alice.printDetails()
    bob.printDetails()

    aliceSharedKey = alice.sharedKey(publicKey=bob.publicKey, prime=prime)
    bobSharedKey = bob.sharedKey(publicKey=alice.publicKey, prime=prime)
    
if __name__ == "__main__":
    main()

