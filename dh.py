#!/usr/bin/env python
import random
import base64
from Crypto.Cipher import AES
from Crypto import Random

BS = 16 # blockSize of 16

class DH(object):
    def __init__(self, name, prime, base):
        self.name = name
        self.__privateKey = largeRandomNumber()
        self.publicKey = pow(base, self.__privateKey, prime)
        
    def sharedKey(self, publicKey, prime):
        self.sharedKey = pow(publicKey, self.__privateKey, prime)
        print "Shared key by " + str(self.name) + ":\t" + str(self.sharedKey)
        
    def encrypt(self, message):
        message = message.zfill((len(message)/BS+1)*BS) # zerofill message to multiple of BS
        key = str(self.sharedKey).zfill(BS) # zerofill key to BS

        iv = Random.new().read(BS) # initialization vector
        aes = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(aes.encrypt(message))
        
    def decrypt(self, cipher):
        cipher = base64.b64decode(cipher) # base64 decode the cipher
        key = str(self.sharedKey).zfill(BS) # zerofill key to BS
        
        iv = cipher[:BS] # initialization vector
        aes = AES.new(key, AES.MODE_CBC, iv)
        return aes.decrypt(cipher[BS:])

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

    print "Shared prime number: \t" + str(prime)
    print "Base:\t\t\t" + str(rootModulo)
    print ""

    alice = DH(name="Alice", prime=prime, base=rootModulo)
    bob = DH(name="Bob", prime=prime, base=rootModulo)

    alice.printDetails()
    bob.printDetails()
    print ""

    alice.sharedKey(publicKey=bob.publicKey, prime=prime)
    bob.sharedKey(publicKey=alice.publicKey, prime=prime)
    print ""
    
    print "Eve, a adversary, has been eavesdropping, here's what she knows:"
    print "Prime:\t\t\t" + str(prime)
    print "Base:\t\t\t" + str(rootModulo)
    print "Alice's public key:\t" + str(alice.publicKey)
    print "Bob's public key:\t" + str(bob.publicKey)
    print ""
    
    print "There's no way for Eve to calculate shared key because of the discrete logarithm problem"
    print ""
    
    message = "ATTACK THE FORT!"
    print "Alice's message:\t" + message
    
    cipher = alice.encrypt(message=message)
    print "Cipher text\t\t" + base64.b64encode(cipher)
    
    message1 = bob.decrypt(cipher=cipher)
    print "Bob's decryption:\t" + message1
    
if __name__ == "__main__":
    main()

