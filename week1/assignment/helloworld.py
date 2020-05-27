#!/usr/bin/env python3

import re

#print("Hello world!")

""" handler = open('mbox-short.txt')
print(handler.read()) """

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+',x)
print(y)