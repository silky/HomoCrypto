#!/usr/bin/python

import sys
def main():
	count=0

	word="God"
	start=True

	for i in sys.stdin:
	#if start:
	#	word=i.strip()
		line=i.strip().split()
		for j in line:
			if word==j:
				count+=1

	print count

main()