#!/usr/bin/python3

import sys
import os
from PIL import Image

def main(videoDir, nFrames):
	missedFrameRanges = []
	brokenFrames = []
	first = True
	for i in range(1, nFrames + 1):
		fileName = os.path.join(videoDir, "cmimg%04d.png" % i)
		if not os.path.isfile(fileName):
			if first:
				missedFrameRanges.append((i, -1))
				first = False
			else:
				missedFrameRanges[-1] = (missedFrameRanges[-1][0], i)
			#print(f"File {fileName} is missed.")
		else:
			first = True

			try:
				im = Image.open(fileName)
			except Exception as e:
				brokenFrames.append(i)

	for i in missedFrameRanges:
		print(i)

	print('Broken frames: ', brokenFrames)

if __name__ == '__main__':
	if 0:
		if len(sys.argv) != 5:
			print("Usage: " + sys.argv[0] + "video_dir n_frames")
			sys.exit(1)

		main(*sys.argv[1:])
	else:
		main('/backup/render/', 72000)
