#!/usr/bin/env python2
# -*- coding: utf-8 -*-
max_i = max_j = 0
for i in range(999,99,-1):
  if max_j > i:
    break
  for j in range(i,99,-1):
    if i*j > max_i*max_j and str(i*j) == str(i*j)[::-1]:
      max_i,max_j = i,j
      break
max_i*max_j #906609