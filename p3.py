#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from mypy import isPrime as Prime # method to judge num if prime
def getLargestPrime(n):
  for i in range(n if n%2 else n-1,1,-2):
    if (n%i is 0) and Prime.isPrime(i):
      return i
getLargestPrime(600851475143/2)