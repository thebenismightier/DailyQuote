#!/usr/bin/env python
# Benny Ng
# bennyng@umich.edu
# github.com/thebenismightier

import random

QUOTES_FN = 'quotes.txt'

def get_quote():
	''' Returns a 'random' quote from a quote base file as a string. '''
	f = open(QUOTES_FN, 'r')
	lines = f.readlines()
	
	random.seed()
	rand_idx = random.randrange(0, len(lines))
	
	return lines[rand_idx]


if __name__ == '__main__':
	print get_quote()