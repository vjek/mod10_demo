#!/usr/bin/python
import random
#create 00 - 99 array. shuffle it. print out a-z0-9+4 extra adjacent, for one time pad encryption use
#also create letters to print next to values

dictionary = range(0,99)
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ,._?"

random.shuffle(dictionary)
x=0
print "custom dictionary below"
for letter in letters:
  print "%02d" % dictionary[x], letter
  x=x+1
print "standard dictionary below"
x=1
for letter in letters:
  print "%02d" % x, letter
  x=x+1
