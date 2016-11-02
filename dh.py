#!/usr/bin/env python
import random

class DH(object):
    def __init__(self):
        prime = self.largePrime()
        print prime
        
    def largePrime(self):
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
        
a = DH()
