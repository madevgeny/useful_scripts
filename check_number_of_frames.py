#!/usr/bin/python3

import sys
import os

def main(videoDir, nFrames):
	nMissedFrames = 0
	for i in range(1, nFrames + 1):
		fileName = "cmimg%04d.png" % i
		if not os.path.isfile(os.path.join(videoDir, fileName)):
			print(f"File {fileName} is missed.")
			nMissedFrames += 1
		else:
			print(fileName)
	if nMissedFrames:
		print(f'Todal {nMissedFrames} files')

if __name__ == '__main__':
	if 0:
		if len(sys.argv) != 5:
			print("Usage: " + sys.argv[0] + "video_dir n_frames")
			sys.exit(1)

		main(*sys.argv[1:])
	else:
		main('/backup/render/rotating_cube/render_cube/', 36000)
