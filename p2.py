#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def fib(a,b,l = []):
  l.append(a)
  return fib(b,a+b,l) if 4000000 >= b else sum([l[i] for i in range(1,len(l),3)])
fib(1,2) #4613732