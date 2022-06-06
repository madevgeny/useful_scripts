#!/usr/bin/env python

import sys

"""
Менее 1 млн рублей
От 1 до 4 млн
От 4 млн
0,035%
0,03%
0,025%

Менее 5 млн рублей
От 5 до 10 млн
От 10 млн
0,04%
0,025%
0,02%
"""


def fee1(turnover):
	if turnover == 0:
		return 0

	if turnover < 1.0e6:
		return turnover * (0.035 / 100)
	if turnover > 4.0e6:
		return turnover * (0.025 / 100)

	return turnover * (0.03 / 100)

def fee2(turnover):
	if turnover == 0:
		return 0

	if turnover < 5.0e6:
		return turnover * (0.04 / 100)
	if turnover > 10.0e6:
		return turnover * (0.02 / 100)

	return turnover * (0.025 / 100)


def main():
	eve1 = [fee1(200000), 0, 0]
	eve2 = [fee2(200000), 0, 0]	

	tim1 = [fee1(500000), 0, fee1(5e6)]
	tim2 = [fee2(500000), 0, fee2(5e6)]	

	ale1 = [fee1(8e6), fee1(12e6), fee1(25e6)]
	ale2 = [fee2(8e6), fee2(12e6), fee2(25e6)]

	print(f"{eve1} {eve2}")
	print(f"{tim1} {tim2}")
	print(f"{ale1} {ale2}")

if __name__ == '__main__':
	main()

