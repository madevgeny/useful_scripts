#!/usr/bin/python3

import sys
import os
from PIL import Image
from multiprocessing import Pool

def check(fileName):
	try:
		im = Image.open(fileName)
		im.verify()
		im.close()
	except Exception as e:
		return False

	return True

def main(videoDir, nFrames):
	missedFrames = []
	images = [os.path.join(videoDir, "cmimg%04d.png" % i) for i in range(1, nFrames + 1)]

	with Pool() as p:
		res = p.map(check, images)

		for i, v in enumerate(res):
			if not v:
				missedFrames.append(i + 1)

	if not missedFrames:
		print('Everything is ok!')
		return

	st = -1
	en = -1
	missedFrameRanges = []
	for i in missedFrames:
		if st < 0:
			st = i
		if en < 0:
			en = i

		d = i - en
		if d <= 1:
			en = i
		else:
			missedFrameRanges.append((st, en))
			st = -1
			en = -1

	if en > 0:
		missedFrameRanges.append((st, en))
		
	for i in missedFrameRanges:
		print(i)

if __name__ == '__main__':
	if 0:
		if len(sys.argv) != 5:
			print("Usage: " + sys.argv[0] + "video_dir n_frames")
			sys.exit(1)

		main(*sys.argv[1:])
	else:
		main('/home/evgeny/sync/render', 72000)
