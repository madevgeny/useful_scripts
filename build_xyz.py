#!/usr/bin/env python

import sys

def code_gen(res):
	return str(res)

def main():
	src = ['x', 'y', 'z']

	for i in src:
		print(code_gen([i]))

	for i in src:
		for j in src:
			print(code_gen([i, j]))

	for i in src:
		for j in src:
			for k in src:
				print(code_gen([i, j, k]))

if __name__ == '__main__':
	if len(sys.argv) != 1:
		print("Usage: " + sys.argv[0] + " src_dir dst_dir")
		sys.exit(1)

	main(*sys.argv[1:])

