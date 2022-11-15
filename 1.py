import math
import sys
import os

print('Please enter variable:')


x=3.251
y=0.325
z=0.466 * (10 ** (-4))

try:
	x = float(input('input x: '))
	y = float(input('input y: '))
	z = float(input('input z: '))


except ValueError:
	print('You should input numbers!')
	sys.exit()
	