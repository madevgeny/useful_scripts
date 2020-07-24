#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def main(srcDir, destDir):
	srcDir = os.path.abspath(srcDir)
	destDir = os.path.abspath(destDir)

	srcFileList = set([os.path.basename(f).lower() for f in os.listdir(srcDir) if os.path.isfile(os.path.join(srcDir, f))])
	destFileList = set([os.path.basename(f).lower() for f in os.listdir(destDir) if os.path.isfile(os.path.join(destDir, f))])

	print(srcFileList, '\n')
	print(destFileList, '\n')
	intersect = srcFileList.intersection(destFileList)
	print(intersect)

	toDelete = [os.path.join(destDir, x) for x in intersect]

	for i in toDelete:
		os.remove(i)

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: " + sys.argv[0] + "src_dir dst_dir")
		sys.exit(1)

	main(*sys.argv[1:])
