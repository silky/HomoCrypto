#!/usr/bin/python

from circuits import *
import sys

def main():
	count = [0]
	for i in sys.stdin:
		try:
			i = map(int, i[2:-2].split(","))
			count = Add16(count,i)
		except:
			continue

	print count
main()
