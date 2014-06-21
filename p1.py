#!/usr/bin/env python2
# -*- coding: utf-8 -*-

sum(map(lambda n: n if not(n%3 and n%5) else 0, range(1,1000)))